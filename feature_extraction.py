import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew

''' EXAMPLE
def func_max(data):
    return data.max()
'''

def func_rms(data):
    return #type here

def func_mean(data):
    return #type here

def func_std(data):
    return #type here
  
def func_peak2peak(data):
    return #type here

def func_kurtosis(data):
    return #type here

def func_skewness(data):
    return #type here

def func_crest_indicator(data):
    return #type here

def func_clearance_indicator(data):
    return #type here

def func_shape_indicator(data):
    return #type here

def func_impulse_indicator(data):
    return #type here
  
  
if __name__ == '__main__':
    rawdata = pd.read_csv('example_rawdata.csv')
    data = rawdata.iloc[:, 0]
   
    features = []
    features.appned(func_rms(data))
    features.appned(func_mean(data))
    features.appned(func_std(data))
    features.appned(func_peak2peak(data))
    features.appned(func_kurtosis(data))
    features.appned(func_skewness(data))
    features.appned(func_crest_indicator(data))
    features.appned(func_clearance_indicator(data))
    features.appned(func_shape_indicator(data))       
    features.appned(func_impulse_indicator(data))
    
    print(features)
