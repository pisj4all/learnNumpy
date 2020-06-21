#!/usr/bin/env python

#--------------Imports-----------------
import numpy as np
#--------------------------------------

#--------------Main Body-----------------

# array of zeros
print("# Array of zeros")
print(np.zeros(10))

# array of ones
print("# Array of ones")
print(np.ones(10))

# array of twos
print("# Array of two's")
print(np.ones(10)*2)

# array of any length
print("# Array of any length")
print(np.arange(10))

# create array manually
print("# Array create manually")
z=np.array([1,2,3,4,5,6,7,8,9,10])
print(z)

# Reshape in Details-------------
print("# Reshaping\n")
# Reshape array into column vector

b_array=np.arange(9)
print("Basic Array: ",b_array)
z=b_array.reshape(9,1)
print("Reshaped: ")
print(z)
print("Reshaped 3x3:\n",b_array.reshape(3,3))
print("\n\n\t#End of Reshaping\n\n")
#--------------------------------
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

# Indexing:
print("\n\nIndexing")
Z = np.arange(9).reshape(3,3)
print(Z)
print("First Value:",Z[0,0])
print("Last Value: ",Z[0,0])
print("2nd Row ",Z[1])
print("2nd Col ",Z[:,1])
print("2x2 from 3x3\n",Z[1:,1:])
print("from two locations ",Z[[0,1],[0,2]])
#--------------------------------------
#--------------------------------------

#--------------Testing-----------------


#--------------------------------------
