# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint #импорт модуля pprint

list_dict = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)] #составление списка словарей
pprint(list_dict) #вывод результата