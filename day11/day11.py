import numpy as np
from scipy.signal import convolve2d
import time

corner_mask = np.ones((3, 3), dtype=np.int16)
corner_mask[1,1] = False

energies = np.genfromtxt("input.txt", delimiter=1, dtype=np.int16)

cntr = 0
nsteps = 0
all_flashed = False
while not all_flashed:
    energies += 1
    flashed_this_step = np.zeros_like(energies)
    while np.any(flashed := (energies > 9)):
        flashed_this_step |= flashed
        res = convolve2d(flashed, corner_mask, mode='same',
                         boundary='fill', fillvalue=0) # padding fill with zeros included in convolution
        energies += res
        energies[flashed] = 0
    energies = np.where(flashed_this_step == 1, 0, energies)
    cntr += np.count_nonzero(flashed_this_step)
    nsteps += 1
    if nsteps == 100:
        print("Part 1:", cntr)
    if np.count_nonzero(flashed_this_step) == energies.size:
        print("Part 2:", nsteps)
        all_flashed = True





