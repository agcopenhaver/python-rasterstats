import numpy as np
import numpy.ma as ma

def spatial_nGINI(y):
    y = y.compressed()
    y = (np.sort(y))
    w = np.full_like(y, 1)
    N = sum(w)
    C_i = np.cumsum(w)
    num_1  = float(sum(np.multiply(y,C_i)))
    num_2 = float(sum(y))
    num_3 = float(sum(np.multiply(y,w)))
    G_num = (2.0 / (N**2.0)) * num_1 - (1.0 / N) * num_2 - (1.0 / (N ** 2.0)) * num_3
    t_neg =  y[y<=0]
    T_neg = float(sum(t_neg))
    T_pos = float(sum(y) + abs(T_neg))
    n_RSV = float((2 * (T_pos + (abs(T_neg))) / N))
    mean_RSV = float((n_RSV / 2))
    G_RSV = float((1/mean_RSV)*G_num)
    return  G_RSV

