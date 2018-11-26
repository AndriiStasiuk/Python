import numpy as np

M = 208
N = 12
array = np.zeros((M, N))


a = np.array([1, 3, 2])

key = int(input('Enter key:'))
print(key)


def find_nearest(z, A):
    id = (np.abs(A - z)).argmin()
    return A[id]


print(find_nearest(key, a))




