import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
# 矩阵上下合并
print(np.vstack((A, B)))
C = np.vstack((A, B))
print(A.shape,C.shape)

#矩阵左右合并
print(np.hstack((A,B)))

print(A)

A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]

C=np.vstack((A,B))
D=np.hstack((A,B))

print(C)
print(D)

C=np.concatenate((A,B,B,A),axis=1)
print(C)