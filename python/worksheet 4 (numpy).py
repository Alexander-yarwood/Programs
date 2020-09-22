# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

treeheight = np.random.uniform(low=0.5,high=5.0,size=100)  #generate 100 values
print(treeheight.mean)                                     # between 0.5 and 5
                         #print the mean value
forest_means = []        #an empty array

for i in range(0, 1000):
    treeheight = np.random.uniform(low=0.5,high=5.0,size=100)
    forest_means.append(treeheight.mean())    #add the mean height to the array
    

forest_means.sort()                                     #sorts the array

print(forest_means)                                     #prints the array

if 2.5 >= forest_means[50]:
    lowest = "false"
else:
    lowest = "true"
    
print(lowest)              #prints the check for if 2.5 is in the lowest values