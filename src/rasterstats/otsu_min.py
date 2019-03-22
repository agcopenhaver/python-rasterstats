import numpy as np
from skimage.filters import threshold_otsu

def otsu_min(y):
    y = y.compressed()
    y =  np.ma.masked_where(y < 1, y)
    if y.min() == y.max():
        return y.min()
    thresh = threshold_otsu(y)
    super_threshold_indices = y < thresh
    y[super_threshold_indices] = 0
    y = y[np.nonzero(y)]
    return np.min(y)


