import numpy as np
from skimage.filters import threshold_otsu

def otsu_min(y):
    y = y.compressed()
    print("oh heck")
    print(y.min)
    print(y.max)
    if y.min() == y.max():
        return y.min()
    y =  np.ma.masked_where(y < 1, y)
    thresh = threshold_otsu(y)
    super_threshold_indices = y < thresh
    y[super_threshold_indices] = 0
    y = y[np.nonzero(y)]
    return np.min(y)


