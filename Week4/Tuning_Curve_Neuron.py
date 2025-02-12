import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract stimulus values and neuron firing rate matrices
stim = data['stim']  # Stimulus values
neurons = {key: data[key] for key in data.keys() if key != 'stim'}


plt.figure(figsize=(10, 6))

for neuron_name, firing_rates in neurons.items():
    # Compute mean firing rate across trials for each stimulus value
    mean_firing_rates = np.mean(firing_rates, axis=0)
    plt.plot(stim, mean_firing_rates, marker='o', label=neuron_name) #plottinh

plt.xlabel("Stimulus Value")
plt.ylabel("Mean Firing Rate (Hz)")
plt.title("Tuning Curves of Neurons")
plt.legend()
plt.grid(True)
plt.show()
