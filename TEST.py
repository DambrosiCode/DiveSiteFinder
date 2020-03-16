# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:09:56 2020

@author: mattd
"""
from near_neigh import DiveFinder
import numpy as np

d = DiveFinder()
print(d.dive_loc(winter=40, n_neighbors=1))


