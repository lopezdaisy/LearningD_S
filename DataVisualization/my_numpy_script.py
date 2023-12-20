import numpy as np

# Create a one-dimensional array
a = np.array([1, 2, 3, 4])
print(a)
print(a.ndim)
print(a.min)
print(a.max)
print(a.sum)
# Create a two-dimentional array
b = np.array([[4,5,6,7],[9,8,7,6],[2,1,3,4]], dtype=np.float64)
print(b)
#properties of an array
print(b.ndim)
print(b.itemsize)
print(b.dtype)
print(b.size)
print(b.shape)
#print(b.ravel)
print(b.min)
print(b.max)
print(b.sum)


#initializing array of zeros
print(np.zeros(   (3,3) ))

#applying range in array
print(np.arange(1,11))

#linspace function
print(np.linspace(1,5,10))

