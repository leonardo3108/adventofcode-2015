from itertools import combinations

def count_combinations(containers, target):
    combinations_container = {}

    for r in range(len(containers)):
        for combo in combinations(containers, r + 1):
            if sum(combo) == target:
                num_containers = len(combo)
                combinations_container[num_containers] = combinations_container.get(num_containers, 0) + 1

    return combinations_container

def main():
    with open("input-17.txt", "r") as file:
        containers = [int(line.strip()) for line in file]

    target_liters = 150
    combinations_dict = count_combinations(containers, target_liters)

    total_combinations = sum(combinations_dict.values())
    min_containers = min(combinations_dict.keys())
    total_min_combinations = combinations_dict[min_containers]

    print("\nMinimum containers needed for a combination:", min_containers)
    print("\nPart One:")
    print("\tTotal combinations:", total_combinations)
    print("Part Two:")
    print("\tWays to fill the minimum containers:", total_min_combinations, '\n')

if __name__ == "__main__":
    main()
