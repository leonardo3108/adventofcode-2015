def match_sue(sue, target, retroencabulator):
    for key in set(sue.keys()).intersection(set(target.keys())):
        target_value = target[key]
        sue_value = sue[key]
        if retroencabulator and key in {'cats', 'trees'} and sue_value <= target_value:
            return False
        elif retroencabulator and key in {'pomeranians', 'goldfish'} and sue_value >= target_value:
            return False
        elif retroencabulator and key not in {'cats', 'trees', 'pomeranians', 'goldfish'} and sue_value != target_value:
            return False
        elif not retroencabulator and sue_value != target_value:
            return False
    return True

def find_matching_sue(data, target, retroencabulator):
    for sue_num, sue in data.items():
        if match_sue(sue, target, retroencabulator):
            return sue_num

def parse_input():
    aunts = {}
    for linha in open('input-16.txt'):
        sue, things = linha.strip().split(': ', 1)
        sue_num = int(sue.split()[-1])
        aunts[sue_num] = {}
        for thing in things.split(', '):
            compound, quantity = thing.split(': ')
            aunts[sue_num][compound] = int(quantity)
    return aunts

def main():
    aunts = parse_input()

    # MFCSAM results from the gift
    target = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

    print('\nPart One:')
    matching_sue = find_matching_sue(aunts, target, False)
    print("\tThe number of the Sue that got you the gift is:", matching_sue)
    print('\nPart Two:')
    matching_sue = find_matching_sue(aunts, target, True)
    print("\tThe number of the Sue that got you the gift is:", matching_sue)

if __name__ == "__main__":
    main()
