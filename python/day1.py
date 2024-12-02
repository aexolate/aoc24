from collections import defaultdict

def part1():
    input_path = "data/day1.in"

    with open(input_path, 'r') as file:
        lines = file.readlines()

    list1 = []
    list2 = []

    for line in lines:
        numbers = list(map(int, line.split()))
        list1.append(numbers[0])
        list2.append(numbers[1])

    assert len(list1) == len(list2), "Lists are not the same length!"

    total_distance = 0

    while list1:
        min1 = min(list1)
        min2 = min(list2)

        total_distance += abs(min1 - min2)  # Add the distances

        list1.remove(min1)
        list2.remove(min2)

    print('part1_total_distance:', total_distance)

def part2():
    input_path = "data/day1.in"

    with open(input_path, 'r') as file:
        lines = file.readlines()

    list1 = []
    list2_dict = defaultdict(int)

    for line in lines:
        numbers = list(map(int, line.split()))
        list1.append(numbers[0])
        list2_dict[numbers[1]] += 1


    similarity_score = 0
    for value in list1:
        similarity_score += value * list2_dict[value]

    print('part2_similarity_score:', similarity_score)

if __name__ == "__main__":
    part1()
    part2()
