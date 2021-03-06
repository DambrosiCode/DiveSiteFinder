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

    def dive_loc(self, winter='Winter', spring='Spring', summer='Summer', fall='Fall', n_neighbors=5):
        dive_params = dict() #{ParamName:ParamValue}
        
        #if the parameter value is quantifiable than is will be considered in the NN algo
        for i, param in enumerate([winter, spring, summer, fall]):
            if isinstance(param, int):
                dive_params[self.cats[i]] = param
                
        self.dive_sites_params = self.dive_sites_df[dive_params.keys()] #DF with just targeted parameters

        data = list(dive_params.values()) #actual param number
        params = list(dive_params.keys()) #param name

        #NN model
        self.X = self.dive_sites_params[params].dropna()        
        self.X = np.array(self.X).reshape(-1,len(params))        
        self.neigh = NearestNeighbors()
        self.neigh.fit(self.X)        
        dist, ind = self.neigh.kneighbors([data],n_neighbors=n_neighbors)
        
        #calculate the nearest neighbors
        near_neighs = self.dive_sites_df.dropna(subset=params).iloc[ind[0]]
        params = np.append('Location', params)
        return(near_neighs[params])

#dive = DiveFinder()

#print(dive.dive_loc(winter=60, summer=100, n_neighbors=1))












