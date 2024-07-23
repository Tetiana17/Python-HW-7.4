def common_elements():
    # генеруємо список чисел кратних 3
    multiples_of_3 = [x for x in range(0, 101) if x % 3 == 0]
    # генеруємо список чисел кратних 5
    multiples_of_5 = [x for x in range(0, 101) if x % 5 == 0]
    # створюємо множини з цих списків
    set_3 = set(multiples_of_3)
    set_5 = set(multiples_of_5)
    # знаходимо перетин множин
    common_elements_set = set_3.intersection(set_5)

    return common_elements_set


# перевірка роботи функції
result = common_elements()
print(result)
