def is_valid(password):
    # Check for the first requirement: increasing straight of at least three letters
    straight_found = False
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
            straight_found = True
            break
    if not straight_found:
        return False

    # Check for the second requirement: no 'i', 'o', or 'l'
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    # Check for the third requirement: at least two different, non-overlapping pairs of letters
    pair_count = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pair_count += 1
            if pair_count == 2:
                return True
            i += 2  # Skip the pair
        else:
            i += 1
    return False

def increment_password(password):
    # Helper function to increment a password
    password = list(password)
    i = len(password) - 1
    while i >= 0:
        if password[i] == 'z':
            password[i] = 'a'
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return ''.join(password)

def find_next_password(current_password):
    # Find the next valid password
    while True:
        current_password = increment_password(current_password)
        if is_valid(current_password):
            return current_password

# Puzzle input
current_password = "cqjxjnds"

# Find and print the next valid password
next_password = find_next_password(current_password)
print("Santa's next password should be:", next_password)

# Again, find and print the next valid password
print("Santa's next password should be:", find_next_password(next_password))

