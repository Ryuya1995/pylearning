import re
from itertools import product

def splt(s):
    return s.split('+')

def getlist(s):
    return set(re.sub(r'[+&!()]','',s))


def getequation(s):
    def assign(pattern):
        return 'dic[\'{}\']'.format(pattern.group('alpha'))
    s = re.sub(r'(?P<alpha>[a-z])', assign, s)
    s = re.sub(r'[+]', ' or ', s)
    s = re.sub(r'[&]', ' and ', s)
    s = re.sub(r'[!]', ' not ', s)
    return s

def cal(s,dic):
    return eval(s)

def preprocessing(s):
    x = getlist(s)
    return getequation(s), x, list(product([True, False], repeat=len(x)))

def solution(s):
    s, x ,brutelist = preprocessing(s)
    sol = []
    for atry in brutelist:
        dic = dict(zip(x,atry))
        if cal(s,dic):
            sol.append(dic)
    return sol

def dnform(s):
    s, x, brutelist = preprocessing(s)
    dnf = ''
    for atry in brutelist:
        dic = dict(zip(x,atry))
        if cal(s,dic):
            if dnf:
                dnf += '+'
            for i,char in enumerate(x):
                dnf += '!' * int(not dic[char]) + char
                if i<len(x)-1:
                    dnf += '&'
    return dnf

def cnform(s):
    s, x, brutelist = preprocessing(s)
    cnf = ''
    for atry in brutelist:
        dic = dict(zip(x,atry))
        if not cal(s,dic):
            if cnf:
                cnf += '&'
            cnf += '('
            for i,char in enumerate(x):
                cnf += '!' * int(dic[char]) + char
                if i<len(x)-1:
                    cnf += '+'
            cnf += ')'
    return cnf



def test():
    s = "b&a+b&c+a&b&c"
    # s = "!a&b&!c+a&!d"
    print(splt(s))
    print(getlist(s))
    print(solution(s))
    print(dnform(s))
    print(cnform(s))


if __name__ == '__main__':
    test()