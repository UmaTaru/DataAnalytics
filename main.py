import numpy as np
#arr = numpy.array([34, 65, 30, 65, 30, 11, 2],dtype=float)
arr = np.array([[1,2,3],[3,4,5]])
#print(arr.shape)
b = arr.reshape(3,2)
print(b)
#c = arr.reshape(4,1)
print(arr.size) #gives no of elements
print(arr.ndim) #gives dimension

a = np.arange()