import numpy as np

A = np.arange(12).reshape((3,4))
print(A)

#纵向切分
print(np.split(A,2,axis=1))
#横向切分
print(np.split(A,3,axis=0))

print(np.vsplit(A, 3)) #等于 print(np.split(A, 3, axis=0))

# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]


print(np.hsplit(A, 2)) #等于 print(np.split(A, 2, axis=1))