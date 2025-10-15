import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])


# array[slice_exp]  = arr[start:end-1:step]

# print 1st row 

print(array[0])

# last row 
print(array[-1])


print(array[0:3])
print(array[0:]) #all 

print(array[0:4:2])

# reversed 
print(array[::-1])



# column selection 
print(array[:, 1]) #[row, col]
# [, 1] error

print(array[:, 0:3])

print(array[0:2, 0:2])