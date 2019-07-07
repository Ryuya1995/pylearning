def finish_pos(j, paras, dirs):
    [_, _, _, r, c] = paras
    went = set()
    went.add((r, c))
    for dir in dirs:
        if dir == 'S':
            while (r, c) in went:
                r += 1
        elif dir == 'N':
            while (r, c) in went:
                r -= 1
        elif dir == 'W':
            while (r, c) in went:
                c -= 1
        elif dir == 'E':
            while (r, c) in went:
                c += 1
        went.add((r, c))
    return 'Case #{}: {} {}'.format(j + 1, r, c)


def main():
    n = int(input())
    for j in range(n):
        paras = [int(x) for x in input().split(' ')]
        dirs = list(input())
        print(finish_pos(j, paras, dirs))


if __name__ == '__main__':
    main()
