# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
x = np.random.random(10)      #generates a random number up to 10
y = np.random.random((3,3,3)) #generates three random numbers in 
#print(x)                      #three sets of three arrays
#print(y)

z = np.random.random((10,3))
z.shape
z.dtype
#print(z)


a = np.zeros(5)                #makes an array of 5 zeroes
#print(a)
b = np.ones(5)                  #makes an array of 5 ones
#print(b)
c = 5 * np.ones(5)               #makes an array of 5 fives
#print(c)


d = np.random.random((10,3))
#print(d)
#print(d[5,2])       #element, collumn 5 row 2
#print(d[5])         #row 5
#print(d[:,2])       #collumn 2
#print(d[4:6,1:3])   #2d slice

      
#print(d[0:1,:])     #will give you two brackets for row zero as it expects many


      
      
#read the data from the file as a 1-dimensional array of 16 bit signed ints (big endian)
e = np.fromfile("megt90n000cb.img", dtype='>i2')
#reshape the array to have rows and collumns
f = e.reshape(720, 1440)
print(f)