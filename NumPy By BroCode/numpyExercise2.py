import numpy as np

rng = np.random.default_rng(seed=10)

A = np.array(rng.integers(1,10,(3,3)))
B = np.array(rng.integers(10,19,(3,3)))

print(A+B)
print(A*B)
print(np.matmul(A,B))

print(A)
print(A[0])
print(A[::,-1])
print(A[0:2,1:3])

C = np.array([5,12,7,30,18,2])

print(C[C>10])
C[C<10] = 0

D = np.array(rng.integers(1,10,(2,3)))

print(np.sum(D))
print(np.mean(D))
print(np.min(D))
print(np.max(D))
print(np.argmax(D))

E  = np.array(rng.integers(1,101,10))

print(np.sort(E))
list = [number for number in E if number%2 == 0]
print(*list,sep = " ")

F = np.array(rng.integers(1,101,(4,4)))
print(F)
F[F%3==0] = -1
print(F)