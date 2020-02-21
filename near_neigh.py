# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:28:09 2020

@author: mattd
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

#dataset location
dive_sites_df = pd.read_csv('./dive_sites_2020.csv')

#categories using
cats = ['divSummer','divWinter','divSpring','divFall']


X = dive_sites_df[cats].dropna()
X = np.array(X).reshape(-1,len(cats))
neigh = NearestNeighbors()
neigh.fit(X)

#calculate the nearest neighbors
dist, ind = neigh.kneighbors([[80,70,60,40]], n_neighbors=5)

near_neighs = dive_sites_df.dropna(subset=cats).iloc[ind[0]]
near_neighs[cats]