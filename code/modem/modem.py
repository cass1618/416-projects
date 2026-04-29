import numpy as np
from scipy.io.wavfile import read

sample_rate, data = read("test1.wav")
# 48000 Hz, int16

# convert 16-bit samples to floats and normalize
samples = data.astype(np.float64) / 32768.0

baud = 300 # transfer rate for Bell 103 (bits/second)

samples_per_bit = sample_rate // baud

num_chars = len(samples) // samples_per_bit // 10

print(num_chars)
