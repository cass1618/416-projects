# Cassandra Copp
# CS 416
# 3 JUNE 2026

from scipy.io.wavfile import write
from scipy.signal import sawtooth
import numpy as np
import sounddevice as sd
from random import choice, sample, random, randint

# select a random song structure
song_structures = ["AABB/CC", "ABAB/CD", "AB/CDDD"]
song_structure = choice(song_structures)

# select a random line structure
line_structures = [
    ["I","IV","ii","V"],
    ["I","vi","ii","V"],
    ["I","iii","IV","iv"],
    ["I","V","ii","V"],
    ["I","vi","IV","V"],
    ["IV","I","vi","IV"],
    ["I","V","vi","I"],
    ["I","IV","iv","I"],
    ["IV","V","I","I"],
    ["vi","IV","I","V"]
]
line_structure = choice(line_structures)

# randomly select tempo between 80 to 160 bpm
tempo = randint(80, 160)

# select random key in range A3 to A4
keys = ["A", "AS", "B", "C", "CS", "D", "DS", "E", "F", "FS", "G", "GS", "A4"]
key = choice(keys)
# find the midi value for the root note
root = 57 + keys.index(key)

# create 4 possible progressions
possible_lines = ['A', 'B', 'C', 'D']
progressions = sample(line_structures, len(possible_lines))
lines = dict(zip(possible_lines, progressions))

tones = {
    "I"  : [0, 4, 7],
    "ii" : [2, 5, 9],
    "iii": [4, 7, 11],
    "IV" : [5, 9, 12],
    "iv" : [5, 8, 12],
    "V"  : [7, 11, 14],
    "vi" : [9, 12, 16]
}

major_steps = [0,2,4,5,7,9,11]

# create a line of 8 notes that have a .8 chance of being in the chord
def melody(root, progression):
    # get notes in scale for selected key
    scale = [root + i for i in major_steps]
    line = []

    # randomly append notes to the melody with .8 chance to be in chord
    for chord_type in progression:
        chord = [root + i for i in tones[chord_type]]
        for _ in range(8):
            line.append(choice(chord) if random() < 0.8 else choice(scale))

    return line

# create a sawtooth wave representing each note played for given duration (default eighth note)
def note(midi, duration=.25):
    # convert key to proper frequency
    frequency = 440.0 * (2 ** ((midi-69)/12))
    # create an array containing 48,000 points of time within 1 second
    sample_times = np.linspace(0., duration, int(48000 * duration), endpoint=False)
    output = (.25 * sawtooth(2 * np.pi * frequency * sample_times)).astype(np.float32)
    return output

# put together 6 lines to make the song
song = []
for verse in song_structure.replace("/", ""):
    song.append(melody(root, lines[verse]))

# convert midi numbers in the melody into waves
def render(notes):
    duration = 60 / tempo / 2
    waves = []
    for n in notes:
        waves.append(note(n, duration))
    return np.concatenate(waves)

song_waves = []
for line in song:
    song_waves.append(render(line))

audio = np.concatenate(song_waves)

print(f"key: {key} tempo: {tempo} bpm")
print("progressions:")
for chord, progression in lines.items():
    print(chord, progression)
print(f"structure: {song_structure}")

sd.play(audio, 48000)
sd.wait()
