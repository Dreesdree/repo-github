time = int(input('Введите время в секундах:'))
hours = time // 3600
hours_1 = time % 3600

minutes = hours_1 // 60

second = hours_1 % 60
print(hours, ':',  minutes, ':', second)