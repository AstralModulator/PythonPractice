import numpy as np
rng = np.random.default_rng(seed=42)

array = np.array(rng.integers(1,51,(5,5)))
print(array)
array[2] = 999
print(array)
array[::,-1] = array[:,-1].mean().astype(int)
print(array)


X = np.array([10, 21, 32, 43, 54, 65, 76, 87])
result = X[(np.arange(len(X))%2==0)&(X%5==0)]
print(result)

A = np.array([[1,2,3],
              [4,5,6]])
B = np.array([10,20,30])

print(A+B)
print(A*B)
print(A**2+B)

rng = np.random.default_rng(seed=10)
Z = rng.integers(-30, 31, (6,6))
print(Z)

absZ = np.abs(Z)
print(absZ)
idx = np.unravel_index(absZ.argmax(), absZ.shape

value = Z[idx]

print(value, idx)

