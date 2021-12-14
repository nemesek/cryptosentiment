import numpy as np

def moving_average(a, n) :
    #print(type(a))
    #n = len(a)
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    val =  ret[n - 1:] / n
    return val

def rollavg_cumsum(a,n):
    'numpy.cumsum'
    #assert n%2==1
    cumsum_vec = np.cumsum(np.insert(a, 0, 0)) 
    val =  (cumsum_vec[n:] - cumsum_vec[:-n]) / n
    return val

def compute_z_score(values, value_to_check):
    sigma = np.std(values)
    val = float(value_to_check)
    mean = float(np.mean(values))
    # print(sigma)
    # print(mean)
    z = (val - mean)/sigma
    return z
    
