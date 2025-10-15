# numerical python 

import numpy as np

print(np.__version__) #dunder(double underscore __)

# normally to store sequence of data in python we use list tuple or set  


# creating numpy array 
array = np.array([1, 2, 3])
print(array)

print(type(array))  #<class 'numpy.ndarray'>


# multiplying all the arr ele by x

array *= 2
print("arr *= 2 : ", array)