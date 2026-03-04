import numpy as np
import math 

a = 2 
b = 8 
n_samples = 50000

samples = np.random.uniform(a, b, n_samples)
x = np.linspace(a, b, 300)
pdf = np.ones_like(x) / (b - a)

print(np.ones((3, 4)))