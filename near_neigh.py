# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:28:09 2020

@author: Matthew D'Ambrosio
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

class DiveFinder():
    def __init__(self):
        #dataset location
        self.dive_sites_df = pd.read_csv('./dive_sites_2020.csv')
        #categories using
        self.cats = ['Winter','Spring','Summer','Fall']
        
        self.X = self.dive_sites_df[self.cats].dropna()
        self.X = np.array(self.X).reshape(-1,len(self.cats))
        self.neigh = NearestNeighbors()
        self.neigh.fit(self.X)
        
    def dive_loc(self, winter, spring, summer, fall, n_neighbors=5): #all you have to do is call
        #calculate the nearest neighbors
        dist, ind = self.neigh.kneighbors([[winter, spring, summer, fall]], n_neighbors=n_neighbors)
        
        near_neighs = self.dive_sites_df.dropna(subset=self.cats).iloc[ind[0]]
        self.cats.insert(0,'Location')
        self.cats.insert(1,'Contact')
        return(near_neighs[self.cats])
        
d = DiveFinder()
print(d.dive_loc(50, 60, 70, 60, 1))