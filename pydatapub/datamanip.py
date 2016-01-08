import numpy as np

def get_data(filename,
             use_columns=None,
             start=None,
             end=None,
             dtype='float'):

    # get specified columns
    if use_columns !=None:
        data = np.genfromtxt(filename, usecols = use_columns, dtype=dtype)
    else:
        data = np.genfromtxt(filename, dtype=dtype)

    columns = zip(*data[1:][start:end])
        
    return columns

