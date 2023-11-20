def encode_string(s):
    encoded_chars = 2  # Account for the two surrounding double quotes
    for i, char in enumerate(s):
        if char == '\\' or char == '"':   # Each backslash or double quote is encoded as "\\" or '\"'
            encoded_chars += 2
        else:                             # Other characters remain the same in the encoded representation
            encoded_chars += 1
    return encoded_chars

def main():
    total_code_length = part1_memory_length = part2_memory_length = 0

    for line in open('input-08.txt', 'r'):
        text = line.strip()
        total_code_length += len(text)
        part1_memory_length += len(eval(text))
        part2_memory_length += encode_string(text)

    print('Part One:', total_code_length - part1_memory_length)
    print('Part Two:', part2_memory_length - total_code_length)

if __name__ == "__main__":
    main()