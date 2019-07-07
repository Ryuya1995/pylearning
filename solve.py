import numpy as np
y = '?'
# A = np.mat('560,167,206;490,155,189;600,180,192')
A = np.mat('9,18,12;10,14,11;7,17,13')
b = np.array([417.6,368.4,405.6]).T
x = [6,12,8,y]
r = np.linalg.solve(A, b)
print('solve:{}'.format(r))

if x[-1] == y:
    result = 0
    for i, xx in enumerate(x):
        if xx != y:
            result += xx * r[i]
    print('result:{}'.format(result))
else:
    b = x[-1]
    for i,xx in enumerate(x[:-1]):
        if xx != y:
            b -= xx*r[i]
        else:
            bb = r[i]
    print('result:{}'.format(b/bb))




"""
A = np.array([])         # 构造系数矩阵 A
b = np.array([]).T 
rr = np.linalg.solve(A,b)
"""