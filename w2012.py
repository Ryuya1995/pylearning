import pylab as pl

data = []


def q1():
    with open("data1.txt") as f:
        maxp = (0, 0)
        for x in f:
            matchobj = x[1:-2].split(',')
            x = int(matchobj[0])
            y = int(matchobj[1])
            if y > maxp[1]:
                maxp = (x, y)
            data.append((x, y))
    return maxp


def q2():
    pl.figure(1)
    for (x, y) in data:
        pl.plot(x, y, 'o')
    pl.title('figure 1')
    pl.xlabel('xaxis')  # make axis labels
    pl.ylabel('yaxis')
    pl.xlim(0, 30)  # set axis limits
    pl.ylim(0, 30)
    pl.show()
    return


def q3(a=0.5, b=10, title='figure 2'):
    pl.figure(2)
    pl.title(title)
    x = range(31)
    y = [a * num + b for num in x]
    func = 'xy = {} * x + {}'.format(round(a,4), round(b,4))
    pl.plot(x, y, label =func)
    pl.legend()
    pl.show()

    return


def q4():
    sumx = sum(num[0] for num in data)
    sumy = sum(num[1] for num in data)
    sumx2 = sum(num[0] * num[0] for num in data)
    sumxy = sum(num[0] * num[1] for num in data)
    n = len(data)
    a = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx * sumx)
    b = (sumx2 * sumy - sumxy * sumx) / (n * sumx2 - sumx * sumx)
    q3(a, b, 'figure 3')
    return


def q5():
    return


def main():
    print("(1) {}".format(q1()))
    print("(2) {}".format(q2()))
    print("(3) {}".format(q3()))
    print("(4) {}".format(q4()))
    print("(5) {}".format(q5()))


if __name__ == '__main__':
    main()
