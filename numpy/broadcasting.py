import numpy as np

# to perform operations on arrays of different shapes by expanding dimensions virtually 

# conditions 

# The dimensions have the same size 
# or 
# one of the dimensions has a size of 1 

a1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
a2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(a1.shape)
print(a2.shape)

print(a1 * a2)