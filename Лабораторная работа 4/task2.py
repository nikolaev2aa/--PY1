def get_count_char(str_):
    letter_dict = {}
    str_without = list(str_.lower().split())
    #str_without.sort()
    str_without = str("".join(str_without))
    for letter in str_without:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1 #букву уже встретили, поэтому увеличиваем количество
            else:
                letter_dict[letter] = 1 #букву встретили первый раз
    return letter_dict
    # TODO посчитать количество каждой буквы в строке в аргументе str_

def get_count_char_procent(letter_dict):
    #sum(letter_dict.values()) #суммарное количество букв в строке
    letter_dict_procent = {}
    for letter in letter_dict.keys():
                letter_dict_procent[letter] = letter_dict[letter] / sum(letter_dict.values()) * 100 #перевод количества повторений в относительную форму (в %)
    return letter_dict_procent

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(get_count_char_procent(get_count_char(main_str))) #вывод словаря с указанием процентного содержания каждой буквы в строке