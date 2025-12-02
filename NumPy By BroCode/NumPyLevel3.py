import numpy as np

rng = np.random.default_rng(seed = 42)
A = np.array(rng.integers(1,51,(5,5)))

A[2] = 999
A[:,-1] = A[:,-1].mean().astype(int)

print(A)

X = np.array([10, 21, 32, 43, 54, 65, 76, 87])
result = X[(np.arange(len(X))% 2 == 0)&(X % 5 == 0)]
print(result)

A = np.array([[1,2,3],[4,5,6]])
B = np.array([10,20,30])

print(A + B)
print(A * B)
print(A**2 + B)


B = np.array(rng.integers(0,101,(4,4)))
print(np.where(B < 20 ,-1 , np.where(B>50,1,0)))

C = np.array(rng.integers(-30,31,(6,6)))
print(C)

absZ = np.abs(C)
index  = np.unravel_index(np.argmax(absZ),absZ.shape)

print(f"The furthest value from 0 is : {C[index]} & the index is : {index}")


