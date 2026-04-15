# Cassandra Copp
# CS 416
# 15 APR 2026

from scipy.io.wavfile import write
import numpy as np
import sounddevice as sd

# 1. Generate a sine wave with given specifications at 1/4 max amplitude and write to a .wav file

# specifications
channels_per_frame = 1 # mono
max_amplitude = 32767 # max signed value
sample_rate = 48000
duration = 1.0
frequency = 440
n = duration * sample_rate

# create an array containing 48,000 points of time within 1 second
sample_times = np.linspace(0., duration, int(sample_rate * duration), endpoint=False)

# calculate amplitude at each time point along the sine wave, for 1/4 max amplitide
samples = (1/4) * max_amplitude * np.sin(2. * np.pi * frequency * sample_times)

# # write the sample to a .wav file
write("sine.wav", sample_rate, samples.astype(np.int16))

# 2. Write an additional .wav file at half max amplitutde but clip all values greater than 1/4 max amplitude

quarter_amp = (1/4) * max_amplitude
samples_clipped = []

for time in sample_times:
    # calculate amplitude at time point along the sine wave, for 1/2 max amplitide
    val = (1/2) * max_amplitude * np.sin(2. * np.pi * frequency * time)
    # set value of sample to exclude all values outside the quarter amplitude range
    if val > quarter_amp: samples_clipped.append(quarter_amp)
    elif val < -quarter_amp: samples_clipped.append(-quarter_amp)
    else: samples_clipped.append(val)

# convert to a numpy array
samples_clipped = np.array(samples_clipped)

# write the clipped sample to a .wav file
write("clipped.wav", sample_rate, samples_clipped.astype(np.int16))

# 3. Play the clipped sine wave

# normalize the samples to prevent extreme loudness
samples_clipped_normalized = samples_clipped.astype(np.float32) / max_amplitude

# use sound device to play the sound and wait for it to finish before ending program
sd.play(samples_clipped_normalized, sample_rate)
sd.wait()