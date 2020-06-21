#!/usr/bin/env python

#--------------Imports-----------------
import numpy as np
#--------------------------------------

#--------------Main Body-----------------

# array of zeros
print(np.zeros(10))

# array of zeros
print(np.ones(10))

# array of twos
print(np.ones(10)*2)

# array of any length
print(np.arange(10))

# create array manually
z=np.array([1,2,3,4,5,6,7,8,9,10])
print(z)

# Reshape array into column vector
z=np.arange(10).reshape(10,1)
print(z)

# Generate Array of random numbers in grid format
z=np.random.randint(0,1000,(10,10))
print(z)

# Create line space
'''It will generate 11 values of equal space
from 0 to 1'''
z=np.linspace(0,1,11)
print(z) # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]

# create mesh grid
z=np.mgrid[0:3,0:3]
print(z)
#--------------------------------------

#--------------Testing-----------------


#--------------------------------------
