from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pickle

from compute_sta import compute_sta

FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']

# Since the data is sampled at 500 Hz, each sample is 2 ms.
sampling_period = 2  # in ms
# For a 300 ms window, we need 150 timesteps (300/2 = 150).
num_timesteps = 150

# Compute the spike-triggered average
sta = compute_sta(stim, rho, num_timesteps)

# Create a time axis for the STA plot
# This time vector represents the window before each spike.
time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')
plt.show()
