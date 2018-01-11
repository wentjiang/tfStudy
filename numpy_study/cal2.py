import numpy as np
A = np.arange(2,14).reshape((3,4))
print(A)

#最小值
print(np.argmin(A))
#最大值
print(np.argmax(A))

#平均值
print(np.mean(A))
print(np.average(A))

#中位数
print(np.median(A))

#累加
print(np.cumsum(A))

#累差
print(np.diff(A))

print(np.nonzero(A))

A=np.arange(14,2,-1).reshape((3,4))
print(A)
print(np.sort(A))

print(A.T)
print(np.transpose(A))

#判断是否有最小或最大值之外的值,并转换成最大最小值
print(np.clip(A,6,9))