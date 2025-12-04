import numpy as np

def prime_check(M):
    if M<=1:
        return False
    if M==2:
        return True
    if M%2==0:
        return False
    for i in range(3,int(np.sqrt(M)+1),2):
        if M % i == 0:
            return False
    return True

rng = np.random.default_rng(seed=42)

A = np.array([12, 47, 5, 98, 34, 7, 50, 120, 3])

result = np.where(A<10,A*0,np.where(A>50,A*2,A*1))
print(result)

X = np.arange(1, 11).reshape(5, 2)
Y = np.array([3, 6])

Z = (X*Y) + (X ** Y)
Z.ravel()
print(Z)

M = np.array(rng.integers(0,21,(7,7)))
print(M)
boolean_vec = np.vectorize(prime_check)
boolean_mask = boolean_vec(M)
M[boolean_mask] = -99
print(M)

N = np.array(rng.integers(-500,501,(10,10)))
index = np.unravel_index(np.abs(N).argmin(), N.shape)
value = N[index]
print(value,index)