from itertools import permutations

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    return total_distance

def find_extreme_distances(distances):
    locations = list(distances.keys())
    all_routes = permutations(locations)
    shortest_distance = float('inf')
    longest_distance = 0

    for route in all_routes:
        distance = calculate_distance(route, distances)
        if distance < shortest_distance:
            shortest_distance = distance
        if distance > longest_distance:
            longest_distance = distance
        #print(route, distance, shortest_distance, longest_distance)

    return shortest_distance, longest_distance

def extract_distances_from_file(filename):
    distances = {}
    for line in open(filename, 'r'):
        parts = line.strip().split()
        city1, city2, distance = parts[0], parts[2], int(parts[4])
        
        if city1 not in distances:
            distances[city1] = {}
        if city2 not in distances:
            distances[city2] = {}
        
        distances[city1][city2] = distance
        distances[city2][city1] = distance

    return distances

def main():
    distances = extract_distances_from_file('input-09.txt')

    shortest_distance, longest_distance = find_extreme_distances(distances)

    print(f"The shortest distance is: {shortest_distance}.")
    print(f"The longest  distance is: {longest_distance}.")

if __name__ == "__main__":
    main()