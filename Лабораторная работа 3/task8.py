money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
ost = money_capital
month = 0  # количество месяцев, которое можно прожить
while ost > (spend * ((1 + increase) ** month)):
    ost = (ost) + salary - spend * ((1 + increase) ** month)
    month += 1
# TODO Оформить решение

print(month)
