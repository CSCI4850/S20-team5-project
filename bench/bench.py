'''
Cruz Jean - bench.py
this module can be included in each model to fetch data, normalize,
and compute performance metrics in a uniform way for comparison.
'''

import yfinance as yf
import numpy as np

def getstock(name):
    '''
    gets the open prices for the given stock in studied range
    '''
    t = yf.Ticker(name)
    dat = t.history(start='1995-01-01', end='2020-03-01')
    return np.array(dat['Open'])[-3900:]
def getstocks(names):
    '''
    gets the open price info for all specified stocks in studied range
    '''
    return np.array([getstock(name) for name in names])

def normalize(dat, window_width, predict_dist):
    '''
    given a collection of stocks from getstocks(), prepares data for training.
    window_width is the number of data points for input.
    predict_dist is distance into future of prediction (e.g. 1 would be predict next value after input window).
    returns (input, expect, norm_scale)
    '''
    count = dat.shape[1] - window_width - predict_dist + 1
    x = np.array([dat[:,i:i+window_width]/dat[:,i,None] for i in range(count)])
    y = np.array([dat[:,i+window_width+predict_dist-1]/dat[:,i] for i in range(count)])
    s = dat[:,0:count]
    return x, y, s
