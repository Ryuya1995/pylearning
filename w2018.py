import random
import re


def q1(com='SSSSSb0012fssttj0006'):
    s, t = q2(com)
    return 's = {}, t = {}'.format(s, t)


def q2(com=''):
    s = t = 0
    i = 0
    while i < len(com) and i >= 0:
        char = com[i]
        if char == 'j':
            i = int(com[i + 1:i + 5]) - 2
        elif char == 'b':
            if s > 0:
                i = int(com[i + 1:i + 5]) - 2
            else:
                i = i + 4
        elif char == 'S':
            s += 1
        elif char == 's':
            s -= 1
        elif char == 'T':
            t += 1
        elif char == 't':
            t -= 1
        elif char == 'f':
            break
        i += 1
    return s, t


def q3(com):  # from q2 add 'c' and 'r'
    # with open('prog3.txt') as f:
    #     com = f.read()
    s = t = 0
    i = 0
    stackr = []
    while i < len(com) and i >= 0:
        char = com[i]
        if char == 'j':
            i = int(com[i + 1:i + 5]) - 2
        elif char == 'b':
            if s > 0:
                i = int(com[i + 1:i + 5]) - 2
            else:
                i = i + 4
        elif char == 'S':
            s += 1
        elif char == 's':
            s -= 1
        elif char == 'T':
            t += 1
        elif char == 't':
            t -= 1
        elif char == 'c':
            stackr.append(i + 5)
            i = int(com[i + 1:i + 5]) - 2
        elif char == 'r':
            i = stackr.pop() - 1
        elif char == 'f' and stackr == []:
            break
        i += 1
    return 's = {}, t = {}'.format(s, t)


def allcommand(com):  # get all instructions
    i = 0
    allcom = []
    while i < len(com) and i >= 0:
        char = com[i]
        if re.match(r'[tTsSfr]', char):
            allcom.append(i)
            i += 1
        elif re.match(r'[bjc]', char):
            allcom.append(i)
            i += 5
    return allcom


def countunused(com, unusedcom):  # change the defination for 'b' and delete used instruction from all instructions
    s = t = 0
    i = 0
    stackr = []
    while i < len(com) and i >= 0:
        char = com[i]
        if i in unusedcom:
            unusedcom.remove(i)
        if char == 'j':
            i = int(com[i + 1:i + 5]) - 2
        elif char == 'S':
            s += 1
        elif char == 's':
            s -= 1
        elif char == 'T':
            t += 1
        elif char == 't':
            t -= 1
        elif char == 'c':
            stackr.append(i + 5)
            i = int(com[i + 1:i + 5]) - 2
        elif char == 'r':
            i = stackr.pop() - 1
        elif char == 'b':
            value = [int(com[i + 1:i + 5]) - 2, i + 4]
            i = random.choice(value)
        elif char == 'f' and stackr == []:
            break
        i += 1
    return unusedcom


def q5():
    with open('prog5.txt') as f:
        com = f.read()
    unusedcom = allcommand(com)
    for _ in range(10000):
        unusedcom = countunused(com, unusedcom)
    return len(unusedcom)


def countstep(com, minstep):
    i = 0
    step = 0
    stackr = []
    while i < len(com) and i >= 0:
        if step >= minstep:
            break
        char = com[i]
        if re.match(r'[tTsS]', char):
            i += 1
        elif char == 'j':
            i = int(com[i + 1:i + 5]) - 1
        elif char == 'c':
            stackr.append(i + 5)
            i = int(com[i + 1:i + 5]) - 1
        elif char == 'r':
            i = stackr.pop()
        elif char == 'b':
            value = [int(com[i + 1:i + 5]) - 1, i + 5]
            i = random.choice(value)
        elif char == 'f' and stackr == []:
            step += 1
            break
        step += 1
    return step


def q6():
    with open('prog6.txt') as f:
        com = f.read()
    minstep = float('inf')
    for _ in range(10000):
        minstep = countstep(com, minstep)
    return minstep


def q7():
    with open('prog7.txt') as f:
        com = f.read()
    # minstep = float('inf')
    minstep = 999  # in case unlimited loop
    for _ in range(10000):
        minstep = countstep(com, minstep)
    return minstep


def main():
    # print("(1) {}".format(q1()))
    # print("(3) {}".format(q3()))
    print("(5) The number of the instructions that are never executed for prog5: {}".format(q5()))
    print("(6) The minimum number of the instructions for prog6: {}".format(q6()))
    print("(7) The minimum number of the instructions for prog7: {}".format(q7()))
    print(q2('TSSSSb0012fssTTj0006'))
    print(q2('j0018j0013Tfj0006'))
    print(q3('c0007fSSttr'))
    print(q3('Tc0008fTc0015rsr'))

if __name__ == '__main__':
    main()
