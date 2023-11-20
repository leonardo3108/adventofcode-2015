import numpy as np
from itertools import product

def calculate_score(ingredients, amounts):
    properties = np.zeros(len(ingredients[0]))  # Initialize properties list

    # Calculate the total properties for the given amounts of ingredients
    for i, ingredient in enumerate(ingredients):
        properties += amounts[i] * np.array(ingredient)

    # Replace negative totals with 0
    properties = np.maximum(0, properties)

    # Calculate the total score (ignoring calories)
    return int(np.prod(properties[:-1])), properties[-1]  # For total score, ignore the last property (calories)

def find_highest_score(ingredients, target_calories):
    highest_score_general = highest_score_meal = 0
    # Try all possible combinations of ingredient amounts
    for amounts in product(range(101), repeat=len(ingredients)):
        if sum(amounts) == 100:  # Ensure the total amount is 100
            score, calories = calculate_score(ingredients, amounts)
            if score > highest_score_general:
                highest_score_general = score
            if score > highest_score_meal and target_calories == calories:
                highest_score_meal = score
    return highest_score_general, highest_score_meal

def parse_input():
    ingredients = []

    for line in  open('input-15.txt', 'r'):
            # Extraindo as propriedades do ingrediente
            properties_str = line.strip().split(': ')[-1]
            properties = [int(prop.split()[1]) for prop in properties_str.split(', ')]

            # Adicionando o ingrediente à lista
            ingredients.append(properties)

    return ingredients

def main():
    print('Example:')    
    ingredients = [
        [-1, -2, 6, 3, 8],  # Butterscotch
        [2, 3, -2, -1, 3]   # Cinnamon
    ]
    part_one, part_two = find_highest_score(ingredients, 500)
    print("\tThe total score of the highest-scoring cookie is:", part_one)
    print("\tThe total score of the highest-scoring cookie you can make with a calorie total of 500 is:", part_two)

    print('Input:')    
    ingredients = parse_input()
    part_one, part_two = find_highest_score(ingredients, 500)
    print("\tThe highest score is:", part_one)
    print("\tThe highest score is:", part_two)


if __name__ == "__main__":
    main()