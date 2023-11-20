import re

def parse_example():
    example_input = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
                      Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
    reindeers = []
    for line in example_input.strip().split('\n'):
        reindeers.append(parse_line(line))
    return reindeers

def parse_input():
    reindeers = []
    for line in open('input-14.txt'):
        reindeers.append(parse_line(line))
    return reindeers

def parse_line(line):
    match = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line.strip())
    name, speed, fly_time, rest_time = match.groups()
    return {'name': name,
            'speed': int(speed),
            'fly_time': int(fly_time),
            'rest_time': int(rest_time),
            }

def calculate_distance_and_score(reindeers, total_time):
    scores = {reindeer['name']: 0 for reindeer in reindeers}
    distances = {reindeer['name']: 0 for reindeer in reindeers}

    for partial_time in range(1, total_time + 1):
        # Calculating the distance each reindeer traveled at time partial_time
        for reindeer in reindeers:
            cycle_time = reindeer['fly_time'] + reindeer['rest_time']
            full_cycles = partial_time // cycle_time
            remaining_time = partial_time % cycle_time
            distance = full_cycles * reindeer['speed'] * reindeer['fly_time']
            distance += min(remaining_time, reindeer['fly_time']) * reindeer['speed']
            distances[reindeer['name']] = distance

        # Awards one point to all the reindeer currently in the lead
        leaders = [name for name, dist in distances.items() if dist == max(distances.values())]
        for leader in leaders:
            scores[leader] += 1

    # At total_time, we know for each reindeer the distance traveled and the points awarded. 
    # Return the max distance traveled and the max score earned
    return max(distances.values()), max(scores.values())

def main():
    print('Example:')    
    reindeers = parse_example()
    time = 1000
    distance, score = calculate_distance_and_score(reindeers, time)
    print(f"\tAfter {time} seconds, the max traveled distance is {distance} km. The winner reindeer has {score} points.")


    print('Input file:')    
    reindeers = parse_input()
    time = 2503
    distance, score = calculate_distance_and_score(reindeers, time)
    print(f"\tAfter {time} seconds, the max traveled distance is {distance} km. The winner reindeer has {score} points.")

if __name__ == "__main__":
    main()
