from collections import defaultdict

def part1():
    input_path = "data/day2.in"

    with open(input_path, 'r') as file:
        reports = file.readlines()

    safe_reports = 0

    for _, report in enumerate(reports):
        levels = list(map(int, report.split()))

        if len(levels) <= 1:
            safe_reports += 1
            continue

        is_safe = True
        is_increasing = levels[1] > levels[0]
        for i in range(1, len(levels)):
            diff = abs(levels[i] - levels[i-1])

            if (diff < 1 or diff > 3) \
            or ((levels[i] > levels[i-1]) != is_increasing):
                is_safe = False
                break

        if is_safe:
            safe_reports += 1

    print('part1_safe_reports:', safe_reports)


def part2():
    input_path = "data/day2.in"

    with open(input_path, 'r') as file:
        reports = file.readlines()

    safe_reports = 0

    for _, report in enumerate(reports):
        levels = list(map(int, report.split()))

        if len(levels) <= 1:
            safe_reports += 1
            continue

        if is_safe_report(levels, True) or is_safe_report(levels, False) or \
        is_safe_report(levels[1:], True, 0) or is_safe_report(levels[1:], False, 0):
            safe_reports += 1

    print('part2_safe_reports:', safe_reports)

def is_safe_report(levels, is_asc_order, strikes_left=1):
    is_increasing = is_asc_order
    is_safe = True
    prev = levels[0]
    for i in range(1, len(levels)):
        diff = abs(levels[i] - prev)

        if (diff < 1 or diff > 3) \
        or ((levels[i] > prev) != is_increasing):
            strikes_left -= 1

            if strikes_left < 0:
                is_safe = False
                break

            continue

        prev = levels[i]

    return is_safe

if __name__ == "__main__":
    part1()
    part2()
