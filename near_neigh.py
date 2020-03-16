# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:28:09 2020

@author: Matthew D'Ambrosio
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from operator import itemgetter

class DiveFinder():
    def __init__(self):
        #dataset location
        self.dive_sites_df = pd.read_csv('./dive_sites_2020.csv')
        
        self.cats = np.array(['Winter','Spring','Summer','Fall'], dtype=str)

    def dive_loc(self, dive_params=[], n_neighbors=5):
        
        #if temp is int IE there's an input it will calculate the NN for that season(s)
        inpts = [i for i, temp in enumerate(dive_params) if type(temp)==int] #index of param
        data = [temp for i, temp in enumerate(dive_params) if type(temp)==int] #actual param number
        params = (self.cats[inpts]) #param name
        print(data)                
        #NN model
        self.X = self.dive_sites_df[params].dropna()
        self.X = np.array(self.X).reshape(-1,len(params))
        self.neigh = NearestNeighbors()
        self.neigh.fit(self.X)
        
        #calculate the nearest neighbors
        dist, ind = self.neigh.kneighbors([data], n_neighbors=n_neighbors)
        
        near_neighs = self.dive_sites_df.dropna(subset=params).iloc[ind[0]]
        params = np.append(['Location'], params)
        return(near_neighs[params])

dive = DiveFinder()
print(dive.dive_loc(['Winter', 60,'Summer', 70]))












