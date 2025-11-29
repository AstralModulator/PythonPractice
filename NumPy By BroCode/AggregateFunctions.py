import numpy as np

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.sum(array1))
print(np.mean(array1))
print(np.var(array1))
print(np.max(array1))
print(np.min(array1))
print(np.argmax(array1))
print(np.argmin(array1))

print(np.sum(array1,axis = 0))
print(np.sum(array1,axis = 1))