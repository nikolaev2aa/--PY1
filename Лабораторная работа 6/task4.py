import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, "r") as f:  # открытие файла для чтения
        data = f.readlines() #чтение всех строк файла и их запись в data
        head = data[0].rstrip().split(',') #получение списка заголовков, где разделителем является запятая, с удалением крайних символов
        #print(head)
        rows = [] #создание пуского списка для записи списка, состоящего из списков данных
        list_dict = [] #создание пуского списка для записи словарей
        for row in data[1:]:
            rows.append(row.rstrip().split(',')) #запись списка, состоящего из списков данных, где разделителем является запятая, с удалением крайних символов
            #print(rows)
        for component in rows:
            matrix = {i : j for i, j in zip(head, component)} #создание списка словарей
            list_dict.append(matrix) #добавление полученного словаря в список словарей
        f.close()  # закрытие файла
    return list_dict



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4)) #вывод списка словарей