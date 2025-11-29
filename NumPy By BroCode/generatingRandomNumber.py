import numpy as np

# rng = rnd.default_rng()
#
# #For integer
# print(rng.integers(0,101,(2,3)))

#For floating point
# print(rnd.uniform(-1,1,4))

#Shuffling an Array:
rng = np.random.default_rng()
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
rng.shuffle(array)
print(array)

