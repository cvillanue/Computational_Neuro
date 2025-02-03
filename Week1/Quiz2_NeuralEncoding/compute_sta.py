"""
Code to compute spike-triggered average.
"""

from __future__ import division
import numpy as np


def compute_sta(stim, rho, num_timesteps):
    """Compute the spike-triggered average from a stimulus and spike-train.

    Args:
        stim: stimulus time-series (1D numpy array)
        rho: spike-train time-series (1D numpy array, with spikes indicated by nonzero entries)
        num_timesteps: number of timesteps (samples) in the window preceding a spike

    Returns:
        spike-triggered average (1D numpy array) computed from the num_timesteps preceding each spike.
    """

    sta = np.zeros((num_timesteps,))

    # Find the indices of spikes that occur after the first num_timesteps samples.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps

    # Calculate the number of spikes (ignoring spikes before 300 ms)
    num_spikes = len(spike_times)
    print(num_spikes)

    # Check if there are any spikes to avoid division by zero.
    if num_spikes == 0:
        print("No spikes found after the initial {} timesteps.".format(num_timesteps))
        return sta

    # Accumulate the stimulus windows preceding each spike.
    for t in spike_times:
        sta += stim[t - num_timesteps:t]

    # Average the accumulated windows.
    sta /= num_spikes

    return sta
