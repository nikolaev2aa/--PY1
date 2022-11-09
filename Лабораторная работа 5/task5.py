def get_random_password(n = 8) -> str: #по умолчанию пароль длиной 8 символов
    from random import sample #импорт функции sample из модуля random
    population = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' #задание используемых символов
    list_letter = sample(population, n) #получение списка заданной длины из представленных выше символов

    return "".join(list_letter) #получение пароля в виде текста

print(get_random_password())
