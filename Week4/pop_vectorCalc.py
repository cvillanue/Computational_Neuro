'''
Question: Decode the neural responses and recover the mystery stimulus vector by computing the population vector for these neurons.
You should use the maximum average firing rate (over any of the stimulus values in 'tuning.mat') for a neuron as the value of
rmax for that neuron. That is, rmax should be the maximum value in the tuning curve for that neuron.

What is the direction, in degrees, of the population vector?
**NEEDS TO BE FIXED lATER --- IM CONFUSED (02/25)
-callyn
'''

import pickle
import numpy as np


with open('pop_coding_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract firing rates and basis vectors - FIXED
'''
i had an error the first run because the elements in r[i] (firing rate vectors) and c[i] (basis vectors) have different shapes, 
and NumPy cannot perform element-wise multiplication between mismatched dimensions. heccc
'''
r = [np.array(data['r1']), np.array(data['r2']), np.array(data['r3']), np.array(data['r4'])]
c = [np.array(data['c1']), np.array(data['c2']), np.array(data['c3']), np.array(data['c4'])]

# Load the data
with open('pop_coding_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract firing rates and basis vectors
r = [np.array(data['r1']), np.array(data['r2']), np.array(data['r3']), np.array(data['r4'])]
c = [np.array(data['c1']), np.array(data['c2']), np.array(data['c3']), np.array(data['c4'])]

# Find r_max for each neuron (avoid division by zero)
r_max = [np.max(r_i) if np.max(r_i) > 0 else 1 for r_i in r]
print(f"\nMax firing rates per neuron (r_max): {r_max}")
# Compute the population vector V = sum( (mean(r_i) / r_max_i) * c_i )
V = np.sum([(np.mean(r[i]) / r_max[i]) * c[i] for i in range(4)], axis=0)
print(f"\nComputed Population Vector (V): {V}")


# Adjust to match the given convention (0° = north, 90° = east)
'''
*****REALLY IMPORTANT*****
The question states that 0° corresponds to the positive y-axis ("north"), and 90° corresponds to the positive x-axis ("east").
This is different from the standard Cartesian coordinate system, where 0° is typically along the x-axis.
ESSENTIALLY we need to rotate our computed angle by -90° to align with the given convention. fuck this is challenging lol 
'''

# Convert Cartesian to polar coordinates (SWAP x and y to match the problem's convention)
theta = np.arctan2(V[1], V[0]) * (180 / np.pi)

# Correct the orientation?? *this might be an issue??
theta_corrected = (-theta) % 360
theta_rounded = round(theta_corrected)
print(theta_rounded)
