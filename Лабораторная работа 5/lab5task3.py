from random import randint


def get_unique_list_numbers() -> list[int]:
    new = []
    i = 0
    while i < 15:
        number = randint(-10, 10)
        if number not in new:
            new.append(number)
            i += 1
    return new
    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
