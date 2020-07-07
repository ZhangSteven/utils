# coding=utf-8
# 
# Utility functions to use with Pandas dataframe
# 
import pandas as pd
from functools import reduce



def dictToDataFrame(d):
    """
    [Dictionary] d => [DataFrame] df

    dictToDataFrame({'x': 88, 'y': 99})
    
        x   y
    0   88  99
    """
    keynValues = list(zip(*d.items()))
    return pd.DataFrame([keynValues[1]], columns=keynValues[0])



def dictListToDataFrame(ds):
    """
    [Iterator or List] ds => [DataFrame] df

    dictListToDataFrame([{'x': 88, 'y': 99}, {'x': 101, 'y': 120}])

        index   x   y
    0   0       88  99
    1   0       101 120
    """
    merge = lambda acc, el: pd.concat([acc, el])

    return reduce(merge, map(dictToDataFrame, ds)).reset_index()