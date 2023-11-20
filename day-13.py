from itertools import permutations

def parse_example():
    input_text = """Alice would gain 54 happiness units by sitting next to Bob.
    Alice would lose 79 happiness units by sitting next to Carol.
    Alice would lose 2 happiness units by sitting next to David.
    Bob would gain 83 happiness units by sitting next to Alice.
    Bob would lose 7 happiness units by sitting next to Carol.
    Bob would lose 63 happiness units by sitting next to David.
    Carol would lose 62 happiness units by sitting next to Alice.
    Carol would gain 60 happiness units by sitting next to Bob.
    Carol would gain 55 happiness units by sitting next to David.
    David would gain 46 happiness units by sitting next to Alice.
    David would lose 7 happiness units by sitting next to Bob.
    David would gain 41 happiness units by sitting next to Carol."""

    happiness_dict = {}
    for line in input_text.split('\n'):
        parse_line(line, happiness_dict)
    return happiness_dict

def parse_input():
    happiness_dict = {}
    for line in open('input-13.txt'):
        parse_line(line, happiness_dict)
    return happiness_dict

def parse_line(line, happiness_dict):
    person, _, sign, happiness, _, _, _, _, _, _, neighbor = line.rstrip().rstrip('.').split()  # remove the trailing dot

    if person not in happiness_dict:
        happiness_dict[person] = {}
    happiness_dict[person][neighbor] = (1 if sign == 'gain' else -1) * int(happiness)

def add_yourself_to_happiness(happiness_dict, yourself):
    happiness_dict[yourself] = {}
    for person in happiness_dict:
        if person != yourself:
            happiness_dict[person][yourself] = 0
            happiness_dict[yourself][person] = 0

def calculate_total_happiness(arrangement, happiness_dict):
    total_happiness = 0
    n = len(arrangement)

    for i in range(n):
        person = arrangement[i]
        left_neighbor = arrangement[(i - 1) % n]
        right_neighbor = arrangement[(i + 1) % n]

        total_happiness += happiness_dict[person][left_neighbor]
        total_happiness += happiness_dict[person][right_neighbor]

    return total_happiness

def find_optimal_seating(happiness_dict):
    attendees = list(happiness_dict.keys())
    max_happiness = 0

    for arrangement in permutations(attendees):
        total_happiness = calculate_total_happiness(arrangement, happiness_dict)
        if total_happiness > max_happiness:
            max_happiness = total_happiness

    return max_happiness

if __name__ == "__main__":
    print('\nExample:')
    happiness_dict = parse_example()
    optimal_seating_happiness = find_optimal_seating(happiness_dict)
    print("\tTotal change in happiness for the optimal seating arrangement:", optimal_seating_happiness)

    print('\nPart One:')
    happiness_dict = parse_input()
    optimal_seating_happiness = find_optimal_seating(happiness_dict)
    print("\tTotal change in happiness for the optimal seating arrangement:", optimal_seating_happiness)

    print('\nPart Two:')
    add_yourself_to_happiness(happiness_dict, "You")
    optimal_seating_happiness = find_optimal_seating(happiness_dict)
    print("\tTotal change in happiness for the optimal seating arrangement:", optimal_seating_happiness)
