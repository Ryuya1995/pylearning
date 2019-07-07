y = '?'
A = [5,10,30,60,120]
Price = [12500,22500,60000,105000, y]
base = Price[0]/A[0]
ratio = [1]
for i, x in enumerate(A[1:], 1):
    if Price[i] != y:
        ratio.append(Price[i]/x/base)
        print('the {}-th time ratio:{}'.format(i, ratio))
        diff = ratio[i] - ratio[i-1]
    else:
        n_ratio = ratio[-1] + diff
        result = base * x * n_ratio
        print('the {}-th time using ratio:{}, result = {}'.format(i, n_ratio, result))

