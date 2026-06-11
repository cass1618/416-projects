# Cassandra Copp
# CS 416P
# 07 JUNE 2026

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
