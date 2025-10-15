import numpy as np

a1 = np.array("A") #zero dim arr
print(a1.ndim)

a2 = np.array(["a", "b", "c"])
print(a2.ndim)


a4 = np.array([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(a4)

a3 = np.array([[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
               [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
               [["s", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]])

# a3 = np.array([[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
#                [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
#                [["a", "b", "c"], ["d", "e", "f"], ["g", "h", ]]])

# err 

print(a3.ndim)
print(a3)



print(a3.shape) #(depth, rows, cols)
 

#  chain indexing 
print(a3[0][0][0]) # traditional array 


# multidimensional indexing
print(a3[0, 0, 1]) #numpy way and also faster

word = a3[0, 0, 0] + a3[2, 0, 0] + a3[2, 0, 0]
print(word)

