salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
spendi = 0
# TODO Оформить решение
for i in range(months, 0, -1):
    spendi = spend * (1 + increase) ** (i - 1)
    need_money = need_money + spendi - salary
print(round(need_money))
