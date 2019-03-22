import numpy as np
from skimage.filters import threshold_otsu

def otsu_min(y):
    y = y.compressed()
    print("oh heck")
    ymin = (y.min)
    ymax = (y.max)
    print(ymin)
    print(ymax)
    if ymin == ymax:
        return y.min()
    y =  np.ma.masked_where(y < 1, y)
    thresh = threshold_otsu(y)
    super_threshold_indices = y < thresh
    y[super_threshold_indices] = 0
    y = y[np.nonzero(y)]
    return np.min(y)


