import numpy as np

A = np.array([ [1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
            )
print(A.shape)
print(A[1,1])
print(A[0])
print(A[2])

B = np.array([10,20,30,40,50,60,70,80,90])
B = np.reshape(B,(3,3))
print(B)

C = np.array([5,12,7,30,18,2])
print(C[C>10])

D = np.array([1,2,3,4])
E = np.array([10,20,30,40])

print(D+E)
print(D*E)
print(D**2)

print(np.mean(B))
print(np.max(B))
print(np.min(B))

X = np.array([[1,2],
              [3,4]])
Y = np.array([[5,6],
              [7,8]])

print(np.matmul(X,Y))

rng = np.random.default_rng(seed=10)
array = np.array(rng.integers(0,101,10))

array1 = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
array2 = np.array([[1,1],[1,1],[1,1]])
array3 = np.array([[1,0],[0,1]])

array4 = np.array([[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]])