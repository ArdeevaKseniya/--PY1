salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев
month = 0

while True:
    month = month + 1
    if month > months:
        break

    delta = spend - salary
    spend *= 1 + increase
    money_capital = money_capital + delta


print(round(money_capital))
