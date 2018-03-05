from math import sqrt

def aR0(d):
    return (10 // d + 1) ** 2

def aR1(d):
    x, k = 0, 0
    while x <= 5:
        y = 0
        while y < 5:
            if (x-5)**2 + (y-5)**2 <= 25:
                k += 1
            y += d
        x += d
    return 1 + (4 * k)

def q2(d):
    return (aR1(d)/aR0(d))/4

def areaKochSnow(n):
    area = {}
    def aKoch(n):
        if n not in area:
            if n == 0:
                edge = 10
                a = edge * edge * sqrt(3) / 4
                area[n] = (a, 3, 10/3)
            else:
                pre = aKoch(n-1)
                pa = pre[0]
                edge_n = pre[1]
                edge_len = pre[2]
                na = edge_n * edge_len * edge_len * sqrt(3) / 4
                area[n] = (pa + na, edge_n*4, edge_len/3)
        return area[n]
    return aKoch(n)[0]




def main():
    d = 1
    print("(1) ar0({}) = {}".format(d, aR0(d)))
    print("    ar1({}) = {}".format(d, aR1(d)))
    print("(2) f({}) = {}".format(d, q2(d)))
    print("(3) area of K({}) = {}".format(2, areaKochSnow(2)))
    n = int(input("please input n: "))
    print("(4) area of K({}) = {}".format(n, areaKochSnow(n)))


if __name__ == '__main__':
    main()


