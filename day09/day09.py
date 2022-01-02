import numpy as np
from scipy.ndimage import measurements

data = np.genfromtxt("input.txt", delimiter=1, dtype=np.int32)

# Pad the area around with 10 to ensure that border values can be
# found as minima in the same way as central values
pdata = np.pad(data, pad_width=1, constant_values=10)

xplus = np.roll(pdata, shift=1, axis=1)
xminus = np.roll(pdata, shift=-1, axis=1)
yplus = np.roll(pdata, shift=1, axis=0)
yminus = np.roll(pdata, shift=-1, axis=0)

# Create a boolean mask by comparing each point to its four neighbors
mask = ((pdata < xplus) & (pdata < xminus) & (pdata < yplus) & (pdata < yminus))
print("Part1: ", (pdata[mask]+1).sum())

# Part 2
# Find clusters of elements that are seperated by 9s
labels, n = measurements.label(data!=9)
labelstack = np.tile(labels, (n, 1)).reshape(n, *labels.shape)
mask = (labelstack==(np.arange(1, n+1, 1).reshape(-1, 1, 1)))
counts = np.count_nonzero(mask, axis=(1, 2))
# Partial sort with np.partition, then calculate the product of the three highest numbers
print("Part 2:", np.partition(counts, -3)[-3:].prod())