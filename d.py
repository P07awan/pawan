#How can you reshape a 1D array of shape (12,) into a 3D array of shape (2, 2, 3)?
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
b=a.reshape(2,2,3)
print(b)