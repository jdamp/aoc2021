"""
The total fuel cost is given as Sum_i (|x_i - z|), where x_i is the inital position of crab i
and z the target position for all crabs (so in fact, simply taking the median of x_i would be enough)
In part two, this is given as Sum_i ((z-x_i)**2 + |z-x_i|)
"""
import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

@np.vectorize
def fuel_cost(z, x_i):
    return np.sum(np.abs(x_i-z))

@np.vectorize
def fuel_cost2(z, x_i):
    return np.sum(0.5*(np.abs(x_i-z)+(x_i-z)**2))

fuel_cost.excluded.add(1)
fuel_cost2.excluded.add(1)

x_i = np.loadtxt("input.txt", delimiter=",")

zmin = np.rint(minimize_scalar(fuel_cost, args=(x_i,)).x)
print(f"Fuel cost for part1: {fuel_cost(zmin, x_i)}")

zmin = np.rint(minimize_scalar(fuel_cost2, args=(x_i,)).x)
print(f"Fuel cost for part2: {fuel_cost2(zmin, x_i)}")