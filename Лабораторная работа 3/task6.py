list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
maximum = max(list_numbers)
last = list_numbers[-1]
list_numbers[-1] = maximum
a = 0
count = 0
for pos, value in enumerate(list_numbers):
    if (value == maximum) and (count != 1):
        a = pos
        count += 1
list_numbers[a] = last
print(list_numbers)
