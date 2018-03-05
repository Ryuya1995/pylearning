dicf = {}
dicg = {}


def f(n):
    if n not in dicf:
        if n < 1:
            dicf[n] = 1
        else:
            dicf[n] = (161 * f(n - 1) + 2457) % (2 ** 24)
    return dicf[n]


def q1():
    return f(100)


def q2():
    j = 0
    for i in range(100):
        if f(i) % 2 == 0:
            j += 1
    return j


def q3():
    j = 0
    for i in range(1, 100, 2):
        if f(i) % 2 == 0:
            j += 1
    return j


def f_iter(n):  # n is positive integer
    f = 1
    for _ in range(n):
        f = (161 * f + 2457) % (2 ** 24)
    return f


def q4():
    return f_iter(1000000)


def g_iter(n):  # n is positive integer
    g = 1
    for _ in range(n):
        g = (1103515245 * g + 12345) % (2 ** 26)
    return g


def g(n):
    if n not in dicg:
        if n < 1:
            dicg[n] = 1
        else:
            dicg[n] = (1103515245 * g(n - 1) + 12345) % (2 ** 26)
    return dicg[n]


def q5():
    return "g2 = {}, g3 = {}".format(g(2), g(3))


def q6():
    g = 1
    k = 0
    while True:
        g = (1103515245 * g + 12345) % 67108864
        k += 1
        if g == 1:
            break
    return k


def q7():
    h = 1
    k = 0
    while True:
        h = ((1103515245 * h + 12345) % 67108864) % 1024
        k += 1
        if h == 1:
            break
    return k


def main():
    print("(1) {}".format(q1()))
    print("(2) {}".format(q2()))
    print("(3) {}".format(q3()))
    print("(4) {}".format(q4()))
    print("(5) {}".format(q5()))
    print("(6) {}".format(q6()))
    print("(7) {}".format(q7()))


if __name__ == '__main__':
    main()
