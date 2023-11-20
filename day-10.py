def look_and_say(sequence):
    result = ""
    start_digit = 0
    end_sequence = len(sequence)
    while start_digit < end_sequence:
        end_digit = start_digit + 1
        digit = sequence[start_digit]
        while end_digit < end_sequence and digit == sequence[end_digit]:
            end_digit += 1
        result += str(end_digit - start_digit) + digit
        start_digit = end_digit
    return result

def iterate_look_and_say(sequence, iterations):
    for _ in range(iterations):
        sequence = look_and_say(sequence)
    return sequence

puzzle_input = "1321131112"
result_after_40_iterations = iterate_look_and_say(puzzle_input, 40)
result_after_50_iterations = iterate_look_and_say(result_after_40_iterations, 10)

print("Length after 40 iterations:", len(result_after_40_iterations))
print("Length after 50 iterations:", len(result_after_50_iterations))

