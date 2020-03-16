# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:09:56 2020

@author: mattd
"""
from near_neigh import DiveFinder
import numpy as np

d = DiveFinder()
temps=['w',55,'34',56]
print(d.dive_loc(winter=temps[0], spring=temps[1], summer=temps[2], fall=temps[3], n_neighbors=1).iloc[0][0+1])


