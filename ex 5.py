proceeds = int(input('Введите значение выручки:'))
costs = int(input('Введите значения издержек:'))
profit = proceeds - costs
if profit > 0:
    profitability = profit / proceeds
    print('Прибыль:' , profit , 'Рентабельность:' , profitability)
    count_workers = int(input('Введите численность сотрудников:'))
    profit_worker = profit / count_workers
    print('Прибыль на одного сотрудника составляет:' , profit_worker)
else:
    print('Убыток:' , profit)