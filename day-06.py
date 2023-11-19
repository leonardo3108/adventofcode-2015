def parse_instruction(instruction):
    parts = instruction.split()

    action = None
    if parts[0] == 'toggle':
        action = toggle_brightness
    if parts[1] == 'on':
        action = increase_brightness
    elif parts[1] == 'off':
        action = decrease_brightness

    start_coords = list(map(int, parts[-3].split(',')))
    end_coords = list(map(int, parts[-1].split(',')))

    return action, start_coords, end_coords

def process_instruction(instruction, brightness, part=1):
    action, start_coords, end_coords = instruction
    for x in range(start_coords[0], end_coords[0] + 1):
        for y in range(start_coords[1], end_coords[1] + 1):
            brightness[x][y] = action(brightness[x][y])[part - 1]

def toggle_brightness(brightness):
    return 1 - brightness, brightness + 2

def increase_brightness(brightness):
    return 1, brightness + 1

def decrease_brightness(brightness):
    return 0, max(0, brightness - 1)

def count_total_brightness(brightness):
    return sum(sum(row) for row in brightness)

def reset_grid():
    return [[0] * 1000 for _ in range(1000)]

def main():
    instructions = []
    with open('input-06.txt') as file:
        for line in file:
            instructions.append(parse_instruction(line.strip()))

    for part in [1, 2]:
        print(f"\nPart {part}:")
        brightness = reset_grid()

        for instruction in instructions:
            process_instruction(instruction, brightness, part)

        result = count_total_brightness(brightness)
        print(f"\tO total de brilho em todas as luzes é: {result}")

if __name__ == "__main__":
    main()
