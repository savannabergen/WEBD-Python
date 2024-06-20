import numpy as np
# Numpy Universal Function
np1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(np1)

# Square root of each element
print(np.sqrt(np1))

# Absolute Value
print(np.absolute(np1))

# Exponents
print(np.exp(np1))

# Min/Mx
print(np.max(np1))
print(np.min(np1))

# Copy vs View
np2 = np1.view()
print(f'Original Np1{np1}')
print(f'Original Np2{np2}')

np1[0] = 41
print(f'Original Np1{np1}')
print(f'Original Np2{np2}')

np2 = np1.copy() # Not connected

# Shape and Reshape