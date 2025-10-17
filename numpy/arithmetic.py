import numpy as np


# scalar arithmetic(single value)

array = np.array([1, 2, 3])

print(array + 1) #2, 3 , 4
print(array - 2) #-1, 0, 1
print(array * 3) #3,6,9
print(array ** 5) #1,32, 243

# vectorized maths functions 

array = np.array([1.01, 2.5, 3.99])
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.pi)

# exercise 
radii = np.array([1, 2, 3])

print(np.pi * radii ** 2)

# element wise arithmetic 
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2) #5,7,9
print(array2 - array1) # can be / , -, **



# comparison operators 
scores = np.array([91, 55, 100, 73, 82, 64])
print(scores == 100)