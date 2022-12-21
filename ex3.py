# программа возводит числа в списке в куб
numbers = [1, 2, 3, 4, 5, 6]
mapped_numbers = list(map(lambda x: x**3, numbers))
print(mapped_numbers)