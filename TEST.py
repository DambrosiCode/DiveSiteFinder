# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:09:56 2020

@author: mattd
"""
from near_neigh import DiveFinder
import numpy as np

d = DiveFinder()
print(d.dive_loc(50, 60, 70, 60, 1).iloc[0][1])