import numpy as np
#Comparison Operators
scores = np.array([91,42,34,55,66,89,20,10,11])
print(scores >= 34)
scores[scores >= 34] = 100
scores[scores < 34] = 0
print(scores)