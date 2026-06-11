# Cassandra Copp
# CS 416P
# 10 JUNE 2026

import numpy as np
from sounddevice import OutputStream
import mido
import threading

# audio settings
sample_rate = 48000
block_size = 256
amplitude = .708

# envelope settings
attack_time = 0.01
release_time = 0.01
attack_n = int(attack_time * sample_rate)
release_n = int(release_time * sample_rate)

def note(midi):
    # convert midi value of note to to proper frequency
    return 440.0 * (2 ** ((midi-69)/12))

# keep track of values being receivied and played
state = {
    'freq': 0.0,
    'phase': 0.0,
    'envelope': 0.0,
    'stage': None
}

# prevent multiple access of state variables
lock = threading.Lock()

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# receives signal from keyboard and new frequency value, resets phase and stage
def key_on(midi):
    with lock:
        state['freq'] = note(midi)
        state['phase'] = 0.0
        state['stage'] = 'attack'
    print(f"playing {notes[midi % 12]}{(midi // 12) - 2} {state['freq']:.2f} hz")

# receives and transmits off signal from keyboard
def key_off():
    with lock:
        state['stage'] = 'release'

# creates new set of samples
def generate(n_frames):
    with lock:
        freq = state['freq']
        phase = state['phase']
        env = state['envelope']
        stage = state['stage']

    output = np.zeros(n_frames)

    for i in range(n_frames):
        if stage == 'attack':
            env = min(1.0, env + 1.0 / attack_n)
            if env >= 1.0:
                stage = 'sustain'
        elif stage == 'release':
            env = max(0.0, env - 1.0 / release_n)
            if env <= 0.0:
                stage = None
                freq = 0.0

        # do not continue playing if frequency falls below 0
        if freq > 0.0:
            output[i] = amplitude * env * (2.0 * phase - 1.0)
            phase += freq / sample_rate
            phase %= 1.0

    with lock:
        state['freq'] = freq
        state['phase'] = phase
        state['envelope'] = env
        state['stage'] = stage

    return output

# listens for input and writes data to outdata 
def audio_callback(outdata, frames, time, status):
    outdata[:, 0] = generate(frames)

# wait for input to come in from keyboard
def midi_listener():
    print("listening on IAC driver Bus 1")
    with mido.open_input('IAC Driver Bus 1') as port:
        for msg in port:
            if msg.type == 'note_on' and msg.velocity > 0:
                key_on(msg.note)
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                key_off()

midi_thread = threading.Thread(target=midi_listener, daemon=True)
midi_thread.start()

print("synth is awaiting signal from midi keyboard. use ctrl+c to turn off.")
with OutputStream(
    samplerate=sample_rate,
    blocksize=block_size,
    channels=1,
    dtype='float32',
    callback=audio_callback
):
    midi_thread.join()
