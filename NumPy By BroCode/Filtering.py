import numpy as np

array1 = np.array([[24,56,78,99,12,14],[45,58,64,24,67,32]])

print(np.where(array1<50,array1,np.nan))

