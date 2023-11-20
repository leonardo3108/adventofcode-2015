import json

def sum_numbers(obj, ignore_red):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(sum_numbers(item, ignore_red) for item in obj)
    elif isinstance(obj, dict):
        # Ignora objetos que contêm a propriedade "red"
        if ignore_red and "red" in obj.values():
            return 0
        return sum(sum_numbers(value, ignore_red) for value in obj.values())
    else:
        return 0

def main():
    # Lê o JSON do arquivo input-12.txt
    with open('input-12.txt', 'r') as file:
        json_data = file.read()
    
    data = json.loads(json_data)

    print("\nPart One:")
    result = sum_numbers(data, False)
    print("\tO resultado da soma de todos os números no documento é:", result)

    print("\nPart Two:")
    result = sum_numbers(data, True)
    print('\tIgnorando os objetos com propriedade "red", a soma dos números no documento é:', result)

if __name__ == "__main__":
    main()
