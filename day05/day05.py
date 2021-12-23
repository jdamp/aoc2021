import awkward as ak
import numpy as np
   
def count_points(x_all):
    """
    Generate all points on all the curves
    Since different curves can have different amounts of points, an awkward array is necessary
    """
    x1 = x_all[:, 0]
    x2 = x_all[:, 1]    
    n = np.abs(x2 - x1).max(axis=1) + 1
    arr = ak.Array([np.rint(np.linspace(x1[i,:], x2[i,:], n[i])) for i in range(x1.shape[0])])
    _, counts = np.unique(ak.flatten(arr), axis=0, return_counts=True)
    print((counts > 1).sum())

raw = np.fromregex("input.txt", "\d+", 2*[("", np.int32)])
x_all = raw.view(np.int32).reshape(-1, 2, 2)
# Selection to only include horizontal or vertical lines
line_selection = np.logical_or(*(x_all[:,1]-x_all[:,0] == 0).T)
count_points(x_all[line_selection])
count_points(x_all)
