import numpy as np
from itertools import ifilter

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

    columns = zip(*data[0:][start:end])
        
    return columns

def rolling_average(array,
                    average):

    array_average = np.zeros(len(array))

    for i in range(0,len(array)):
        dummy = 0.0
        count = 0
        for j in range(i-average,i+average+1):
            if j >= 0 and j < len(array):
                dummy += array[j]
                count+=1
        dummy = dummy/float(count)
        array_average[i] = dummy
    return array_average

def subtract_constant(array,
                      constant):

    new_array = np.zeros(len(array))

    for i in range(0,len(array)):
        new_array[i] = array[i] - constant

    return new_array

def mts_data(filename,
             use_columns=None,
             start=None,
             end=None,
             dtype='float'):

    with open(filename, 'rb') as inp:
        filtered_inp = ifilter(lambda x: not (x.startswith(' ') or x.startswith('M') or x.startswith('D') or x.startswith('S') or x.startswith('T')), inp)

        # get specified columns
        if use_columns !=None:
            data = np.genfromtxt(filtered_inp, usecols = use_columns, dtype=dtype)
        else:
            data = np.genfromtxt(filtered_inp, dtype=dtype)

        columns = zip(*data[0:][start:end])
        
    return columns

