#How can you create a new array that contains only the even numbers from the array arr = np.array([1, 2, 3, 4, 5, 6])?
import numpy as np
a=np.array([1,2,3,4,5,6])
b=a%2==0
c=a[b]
print(c)