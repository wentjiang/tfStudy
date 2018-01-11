import numpy as np

A=np.arange(3,15).reshape((3,4))
print(A)
print(A[2])
print(A[1][1])

for row in A:
    print(row)
for column in np.transpose(A):
    print(column)

#展开多维数组函数
print(A.flatten())

#迭代器
for item in A.flat:
    print(item)