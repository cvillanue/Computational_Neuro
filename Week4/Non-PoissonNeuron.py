'''
Notes to self to fix mistakes:
The correct answer was Neuron 3 becasue it violated Poisson statistics in a more meaningful way.
High Fano factor (variability > mean) does not always mean non-Poisson.... instead, a neuron can deviate from Poisson behavior due to:
Bursting activity (firing in irregular, non-random patterns), Refractory period effects (reducing variance in a non-Poisson way)
and Non-stationarity in firing rates (changing firing patterns over time).

Even if Neuron 1 had a numerically higher deviation from 1, Neuron 3’s firing properties likely made it a better candidate.

'''

import pickle
import numpy as np

# Load the data
with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract neurons (excluding 'stim')
neurons = {key: data[key] for key in data.keys() if key != 'stim'}
fano_factors = {}

# Define time window T (assumed 1 second for firing rates in Hz)
T = 1

for neuron_name, firing_rates in neurons.items():
    # Convert firing rates to estimated spike counts
    spike_counts = firing_rates * T

    # Compute variance and mean over trials
    mean_spike_counts = np.mean(spike_counts, axis=1)
    var_spike_counts = np.var(spike_counts, axis=1)

    # Prevent division by zero by filtering zero mean values
    valid_indices = mean_spike_counts > 0
    if np.any(valid_indices):
        fano_factor = np.mean(var_spike_counts[valid_indices] / mean_spike_counts[valid_indices])
    else:
        fano_factor = 0

    fano_factors[neuron_name] = fano_factor

# Print Fano Factors
print("\nFano Factors of Neurons:")
for neuron, fano in fano_factors.items():
    print(f"{neuron}: {fano:.3f}")

# Find the neuron with the MOST STATISTICALLY MEANINGFUL deviation from Poisson
valid_fano_factors = {k: v for k, v in fano_factors.items() if not np.isnan(v)}

if valid_fano_factors:
    # Compute deviation from the expected Poisson value (1)
    poisson_deviation = {k: abs(np.log(v / 1)) for k, v in valid_fano_factors.items()}  # Log-normalized deviation

    # Instead of max absolute Fano Factor, pick the neuron with the most non-Poisson-like behavior
    non_poisson_neuron = max(poisson_deviation, key=poisson_deviation.get)

    print(f"\nNeuron {non_poisson_neuron} is likely NOT Poisson.")
else:
    print("\nAll neurons have zero firing rates or invalid data.")


