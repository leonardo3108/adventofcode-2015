def parse_instruction(instruction):
    parts = instruction.split()
    assert(len(parts) in [3, 4, 5])
    if len(parts) == 3:
        return ("ASSIGN", parts[0], parts[-1])
    elif len(parts) == 4:
        return (parts[0], parts[1], parts[-1])
    else:
        return (parts[1], parts[0], parts[2], parts[-1])

def prepare_instructions(parsed_instructions):
    instructions = {}
    for parsed_instruction in parsed_instructions:
        output = parsed_instruction[-1]
        assert(output not in instructions)
        instructions[output] = {'operation': parsed_instruction[0], 'input': list(parsed_instruction[1:-1])}
    return instructions

def get_value(input, instructions):
    if input not in instructions:
        return int(input)
    if 'value' not in instructions[input]:
        instructions[input]['value'] = execute_instruction(input, instructions)
    return instructions[input]['value']

def execute_instruction(wire, instructions):
    operation = instructions[wire]['operation']
    value1 = get_value(instructions[wire]['input'][0], instructions)
    if operation == 'ASSIGN':
        return value1
    elif operation == 'NOT':
        return 65535 - value1
    else:
        value2 = get_value(instructions[wire]['input'][1], instructions)
        if operation == "AND":
            return value1 & value2
        elif operation == "OR":
            return value1 | value2
        elif operation == "LSHIFT":
            return value1 << value2
        elif operation == "RSHIFT":
            return value1 >> value2
        else:
            assert(False)

def main():
    with open("input-07.txt", "r") as file:
        parsed_instructions = [parse_instruction(line.strip()) for line in file.readlines()]

    print("\nPart  One")
    instructions = prepare_instructions(parsed_instructions)
    print("\tSignal provided to wire a:", execute_instruction('a', instructions))

    print("\nPart  Two")
    instructions = prepare_instructions(parsed_instructions)
    instructions['b']['value'] = 16076
    print("\tSignal provided to wire a:", execute_instruction('a', instructions))

if __name__ == "__main__":
    main()
