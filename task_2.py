from random import randint


def get_unique_list_numbers() -> list[int]:
    unique = []
    unique_numbers = ([randint(-10, 10) for _ in range(15)])
    for number in unique_numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


list_unique_numbers = get_unique_list_numbers()

print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# Последняя строка