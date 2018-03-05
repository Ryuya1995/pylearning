def cntSemi(): #1
    with open("program.txt","r") as f:
        cont = f.read()
        return cont.count(";")

def prtMain(): #2
    with open("program.txt", "r") as f:
        i = 0
        for row in f:
            if "main" in row:
                print(i, ":", row)
            i += 1

def prtDL(): #3
    with open("program.txt", "r") as f:
        dupl = set()
        pre = ""
        for row in f:
            if row == pre:
                dupl.add(row)
            pre = row
        for line in dupl:
            print(line)

def prtDL2(): #4
    with open("program.txt", "r") as f:
        cnt = set()
        dupl = set()
        for row in f:
            if row in cnt:
                dupl.add(row)
            cnt.add(row)
        for line in dupl:
            print(line)
        print("The number of the lines printed as duplicates:", len(dupl))

def isSimilar(row1, row2):
    if row1 == row2:
        return False
    l1 = len(row1)
    l2 = len(row2)
    if l1 > l2:
        row2 = row2 + " " * (l1 - l2)
    elif l2 > l1:
        row1 = row1 + " " * (l2 - l1)
    diff = 0
    for i in range(max(l1, l2)):
        diff += (row1[i] != row2[i])
    return diff < 5

def prtSL(): #5
    with open("program.txt", "r") as f:
        siml = []
        pre = ""
        for row in f:
            if len(row) > 20 and isSimilar(row[:-1], pre[:-1]):
                siml.append(pre)
                siml.append(row)
            pre = row
        for line in siml:
            print(line)
        print(len(siml))

def editDistance(s1,s2):
    dp ={}
    def edit(i,j):
        if (i,j) not in dp:
            if not (i and j):
                dp[i,j] = i + j
            else:
                dp[i,j] = min(edit(i-1,j) + 1, edit(i, j-1) +1, edit(i-1, j-1) + (s1[i - 1] != s2[j - 1]))
        return dp[i, j]
    return edit(len(s1),len(s2))

def prtSL2(): #6
    with open("program.txt", "r") as f:
        siml = []
        pre = ""
        for row in f:
            if len(row) > 20 and editDistance(row, pre) < 4:
                siml.append(pre)
                siml.append(row)
            pre = row
        for line in siml:
            print(line)
        print(len(siml))

def prtDL3(): #7
    with open("program.txt", "r") as f:
        dupl = set()
        pre = ""
        cnt = 0
        for row in f:
            if row == pre:
                cnt += 1
                if cnt > 2:
                    dupl.add(row)
            else:
                cnt = 0
            pre = row
        for line in dupl:
            print(line)

def main():
    print("q1")
    print("The number of semicolons:",cntSemi())
    print("q2")
    prtMain()
    print("q3")
    prtDL()
    print("q4")
    prtDL2()
    print("q5")
    prtSL()
    print("q6")
    prtSL2()
    print("q7")
    prtDL3()

if __name__ == '__main__':
    main()













