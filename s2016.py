# file os
import os

s1 = ["*|*|*"]
s2 = ["* *|*", "* * *", "* * *", "*|* *"]
s7 = ["*    ", "*    ", "*    ", "*|*|*"]
dic = {"1": s1, "2": s2, "7": s7}
# reverse dic dict(zip(dic.values(),dic.keys()))
kvalue = []
for value in dic.values():
    kvalue.append("".join(value))
dic2 = dict(zip(kvalue, dic.keys()))
file_t = "tmp.txt"
file_a = "out1.txt"


def reverse(s):
    return list(map(list, zip(*s)))


def reverseFile(file_n):
    with open(file_n, 'r') as f:
        text = []
        for row in f:
            text.append(row[:-1])
        newtext = reverse(text)
    with open(file_n, 'w') as f:
        for row in newtext:
            for char in row:
                f.write(char)
            f.write('\n')


def printchar(s, blankline=1, blankn=5):
    with open(file_a, 'a') as f:
        for row in s:
            f.write(row + '\n')
        for i in range(blankline):
            f.write(' ' * 5 + '\n')


def printnum(n):
    sn = str(n)
    while len(sn) > 1:
        x = sn[0]
        sn = sn[1:]
        printchar(dic[x])
    if len(sn) == 1:
        printchar(dic[sn])


def recognize(file_n):
    with open(file_n, 'r') as f:
        text = []
        for row in f:
            text.append(row[:-1])
        newtext = reverse(text)
    num = ['']
    i = 0
    for row in newtext:
        curr = ''.join(row)
        if curr.strip():
            num[i] += (curr)
        else:
            i += 1
            num.append('')
    for match in num:
        if match in dic2:
            print(dic2[match], end='')


def main():
    os.remove(file_a)
    printnum(127)
    reverseFile(file_a)
    recognize(file_a)


if __name__ == '__main__':
    main()
