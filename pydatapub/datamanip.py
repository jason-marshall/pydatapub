import numpy as np

def get_data(filename,
             use_columns=None,
             start=None,
             end=None):

    # get specified columns
    if use_columns !=None:
        data = np.loadtxt(filename, usecols = use_columns)
    else:
        data = np.loadtxt(filename)

    columns = zip(*data[1:][start:end])
        
    return columns

