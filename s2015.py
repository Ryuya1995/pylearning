def quaternary2decimal(x):
    k = ans = 0
    while x:
        x, p = divmod(x, 10)
        ans += p * (4 ** k)
        k += 1
    return ans


def symbol2decimal(x):
    sym = ["a", "b", "c", "d", "e", "f", "g", "h"]
    num = list(map(lambda x: ord(x) - 97, sym))
    dic = dict(zip(sym, num))
    k = ans = 0
    while x:
        x, p = x[:-1], x[-1]
        ans += dic[p] * (8 ** k)
        k += 1
    return ans


def decimal2roman(x):
    strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ans = ""
    for i, num in enumerate(nums):
        while x >= num:
            ans += strs[i]
            x -= num
        if x == 0:
            return ans


def roman2decimal(x):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    k = ans = 0
    while x:
        x, p = x[1:], x[0]
        sign = 1
        if x:
            nex = x[0]
            # if p == "I" and (next == "V" or next == "X") \
            #         or p == "X" and (next == "L" or next == "C") \
            #         or p == "C" and (next == "D" or next == "M"):
            if dic[p] < dic[nex]:
                sign = -1
        ans += sign * dic[p]
        k += 1
    return ans


def sdecimal2roman(x):
    strs = ['M', 'D', 'C', 'L', 'X', 'V', 'I', '']
    nums = [1000, 500, 100, 50, 10, 5, 1, 0]
    plus = ""
    plusn = 0
    for i, num in enumerate(nums):
        if x > num * 2:
            return plus, plusn
        while x >= num:
            plus += strs[i]
            x -= num
            plusn += num
        if x == 0:
            return plus, plusn


def edecimal2roman(x):
    strs = ['M', 'D', 'C', 'L', 'X', 'V', 'I', '']
    nums = [1000, 500, 100, 50, 10, 5, 1, 0]
    ans = ""
    for i, num in enumerate(nums):
        while x >= num:
            ans += strs[i]
            x -= num
        if x > (num + nums[i + 1]) / 2:
            plus, plusn = sdecimal2roman(num - x)
            ans += plus
            ans += strs[i]
            x = x - num + plusn
        if x == 0:
            return ans


def text2int(textnum, numwords={}):
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)
        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    return result + current


def main():
    print(quaternary2decimal(123))
    print(symbol2decimal("bcd"))
    print(decimal2roman(2015))
    print(roman2decimal("MCMIV"))
    print(decimal2roman(2018))
    print(edecimal2roman(2018))
    print(text2int("fifty thousand three hundred twenty five"))


if __name__ == '__main__':
    main()
