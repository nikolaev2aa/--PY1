def get_unique_list_numbers() -> list[int]:
    from random import randint #импорт функции randint из модуля random
    list_numbers = [randint(-10, 10)] #вычисление первого числа
    while len(list_numbers) < 15: #проверка на количество чисел в списке
        K = randint(-10, 10) #вычисление очередного числа и его запись в промежуточную переменную
        if K not in list_numbers: #проверка отсутствия вычисленной величины в списке (проверка уникальности)
            list_numbers.append(K) #запись уникального числа в список

    return list_numbers #вывод списка уникальных чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
