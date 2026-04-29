import numpy as np
from scipy.io.wavfile import read

sample_rate, data = read("test1.wav")
# 48000 Hz, int16

# convert 16-bit samples to floats and normalize
samples = data.astype(np.float64) / 32768.0

baud = 300 # transfer rate for Bell 103 (bits/second)

# find number of samples in each bit
samples_per_bit = sample_rate // baud

# find total number of bits
num_bits = len(samples) // samples_per_bit

# each 10 bits contains a character
num_chars = num_bits // 10

print(num_chars)

# create array of times for each bit
sample_times = np.arange(samples_per_bit)

mark_rate = 2225
space_rate = 2025

# compute reference tones for 2025 Hz (space) and 2225 Hz (mark)
cos_space = np.cos(2 * np.pi * space_rate * sample_times / sample_rate)
sin_space = np.sin(2 * np.pi * space_rate * sample_times / sample_rate)
cos_mark  = np.cos(2 * np.pi * mark_rate * sample_times / sample_rate)
sin_mark  = np.sin(2 * np.pi * mark_rate * sample_times / sample_rate)


bits = []

# loop over samples and examine each block of 160 samples
for i in range(len(samples) // samples_per_bit):
    block = samples[i * samples_per_bit: (i + 1) * samples_per_bit]

    # calculate power at space frequency
    Ispace = np.dot(block, cos_space)
    Qspace = np.dot(block, sin_space)
    Pspace = Ispace ** 2 + Qspace ** 2

    # calculate power at mark frequency
    Imark = np.dot(block, cos_mark)
    Qmark = np.dot(block, sin_mark)
    Pmark = Imark ** 2 + Qmark ** 2

    # compare each power to see which frequency it matches
    bit = 0 if Pspace > Pmark else 1
    bits.append(bit)


message = ""

# loop over each 10 bit frame
for n in range(num_chars):
    frame = bits[n *10: (n + 1) * 10]

    val = 0
    # convert the binary value to decimal
    for i in range(8):
        val |= frame[1 + i] << i

    # append the ascii char value to the string
    message += chr(val)

print(message)