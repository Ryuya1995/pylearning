def solution():
    total_case = input()
    total_case = int(total_case)
    res = {}
    for case_ind in range(total_case):
        [N, R, C, SR, SC] = [int(x) for x in input().split()]
        instructions = input()
        final_location = get_location(N, R, C, SR, SC, instructions)
        res[case_ind] = final_location
    return res, total_case


def get_location(N, R, C, SR, SC, instructions):
    location = [SR, SC]
    places_went = set()
    places_went.add((SR,SC))
    for i in range(N):
        step = instructions[i]
        if step == "N":
            while tuple(location) in places_went:
                location[0] -= 1
        elif step == "S":
            while tuple(location) in places_went:
                location[0] += 1
        elif step == "W":
            while tuple(location) in places_went:
                location[1] -= 1
        elif step == "E":
            while tuple(location) in places_went:
                location[1] += 1
        places_went.add(tuple(location))
    return location


def output(res, total_case):
    for case in range(total_case):
        print(("Case #{}: {} {}").format(case + 1, res[case][0], res[case][1]))


def main():
    res, total_case = solution()
    output(res, total_case)


if __name__ == "__main__":
    main()