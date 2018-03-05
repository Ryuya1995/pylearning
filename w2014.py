from decimal import *
getcontext().prec = 32

def f1(n):  # (1)
    if n <= 2:
        return 1
    return f1(n - 1) + f1(n - 2)


def f2(n):  # (2)
    dp = [0] + [1] + [1] + [0] * (n - 2)
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def add(a, b):  # (3)
    c = str(int(a) + int(b))
    return '0' * (32 - len(c)) + c


def f4(n):  # (4)
    res = str(f2(n))
    return '0' * (32 - len(res)) + res


def mul(a, b):  # (5)
    a, Ea = a.split()
    b, Eb = b.split()

    c = str(int(a) * int(b))
    e = str(int(Ea) + int(Eb))
    if len(c) == len(a) + len(b):
        e = str(int(e) + 1)

    c = c + '0' * (32 - len(c))
    e = '0' * (2 - len(e)) + e
    return c[0:32] + ' ' + e


def phi():  # (6)
    a = str(Decimal(1 + 5 ** 0.5))
    a = a[:1] + a[2:] + ' 00'
    b = '5' + '0' * 31 + ' -1'
    return mul(a, b)


def g(n):  # (7)
    a = p = phi()
    for i in range(n - 1):  # phi^n
        a = mul(a, p)

    b = '4472135954999579'  # 1 / sqrt(5)
    b = b + '0' * (32 - len(b)) + ' -1'

    return mul(a, b)


def f8(n):
    f = f4(n)

    sft = 0
    for i in range(len(f)):
        if f[i] != '0':
            sft = i
            break
    f = f[sft:] + '0' * (sft)
    sft = str(32 - sft - 1)
    sft = '0' * (2 - len(sft)) + sft

    return f + ' ' + sft


def abs_sub(a, b):
    a, Ea = a.split()
    b, Eb = b.split()

    diff = abs(int(Ea) - int(Eb))
    if Ea > Eb:
        b = '0' * diff + b[0:len(b) - diff]
        Eb = str(int(Eb) + diff)
    elif Ea < Eb:
        a = '0' * diff + a[0:len(a) - diff]
        Ea = str(int(Ea) + diff)

    c = str(abs(int(a) - int(b)))
    sft = 32 - len(c)
    c = c + '0' * sft
    e = str(int(Ea) - sft)
    e = '0' * (2 - len(e)) + e
    return c + ' ' + e


def lessThan(a, b):
    a, Ea = a.split()
    b, Eb = b.split()
    if Ea != Eb:
        return Ea < Eb
    else:
        return a < b


def calcMaxv():  # (8):
    maxv = '0' * 32 + ' 00'
    for i in range(1, 140 + 1):
        diff = abs_sub(f8(i), g(i))  # |f(x) - g(x)|
        if lessThan(maxv, diff):
            maxv = diff
    return maxv


def main():
    print('(1) f(10) =', f1(10))

    print('(2) f(50) =', f2(50))

    a = '00123456789012345678901234567890'
    b = '00987654321098765432109876543210'
    print('(3) a + b =', add(a, b))

    print('(4) f(140) =', f4(140))

    a = '12345678901234567890123456789012 04'
    b = '98765432109876543210987654321098 09'
    print('(5) a * b = ', mul(a, b))

    print('(6) phi =', phi())

    print('(7) g(140) =', g(140))

    print('(8) maxv =', calcMaxv())

if __name__ == '__main__':
    main()
