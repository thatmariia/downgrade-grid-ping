import numpy as np


class SpikingFrequency:
    def __init__(self, ping_frequencies):
        self.ping_frequencies = ping_frequencies
        self.std = np.std(ping_frequencies)
