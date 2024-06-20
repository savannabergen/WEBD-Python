# Intro Slicing
import numpy as np

list1 = [1,2,3,4,5]
#print(list1)

list2 = ["John Elder", 41, list1, True]
#print(list2)

# Numpy - Numeric Python
# ndarray = n-dimensional array
np1 = np.array([1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

# Range
np2 = np.arange(10)
print(np2)

# Step
np3 = np.arange(0, 10, 2)
print(np3)

# Zeros 
np4 = np.zeros(10)
print(np4)

# Multidimensional Zeros
np5 = np.zeros((2, 10))
print(np5)

# Full
np6 = np.full((10), 6)
print(np6)

# Multidimensional Full
np7 = np.full((2, 10), 6)
print(np7)

# Convert Python Lists to Numpy
my_list = [1, 2, 3, 4, 5]
np8 = np.array(my_list)
print(np8[2])

# Slicing Numpy Arrays
print(np1[0:9])

# Return from something til the end of the array?
print(np1[3:])

# Return Negative Slices
print(np1[-3:-1])

# Steps
print(np1[1:5:])
print(np1[1:5:2])

# Steps on the entire array
print(np1[::2])

# Slice a 2-d array
d2 = np.array([[1,2,3,4,5], [6, 7, 8, 9, 10]])
# Pull out a single item
print(d2[1,2])

# Slice a 2-d array
print(d2[0:1, 1:3])

# Slice both rows 2-d array
print(d2[0:2, 1:3])