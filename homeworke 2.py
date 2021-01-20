# Task 1
'''Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''''

list = [2, True, 'name', [1, 2, 3], (4, 5, 6), 12.3, {'name': 'Вася', 'age': 10}]
for i in list:
    print(type(i))

# Task 2
'''Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().'''
list = []
i = 0
while i < 5:
    i += 1
    list.append(input('Введите значение'))
for i in range(1, len(list), 2):
    list[i - 1], list[i] = list[i], list[i - 1]
print(list)

# Task 3
'''Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict. '''

list_month = [0, 'Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
month = list_month[int(input('Введите время года в численном формате:'))]
if month <= 0 or month >= 13:
    print('Некоректный ввод')
else:
    print(month)

# Task 4
'''Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
Если слово длинное, выводить только первые 10 букв в слове. '''

string = input("Введите предложение: ")
a = string.split(' ')
for i, b in enumerate(a, 1):
    if len(b) > 10:
        b = b[0:10]
    print(f"{i}. - {b}")

# Task 5
'''Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
 натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. 
 Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент 
 с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. 
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, 
например, my_list = [7, 5, 3, 3, 2].
'''

my_list = [7, 5, 3, 3, 2]
request = input('Введите число: ')
for index, number in enumerate(my_list):
    if int(request) < int(number):
        continue
    my_list.insert(index, request)
    break
else:
    my_list.append(request)
print(my_list)

# Task6
'''*Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры: 
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, 
в котором каждый ключ — характеристика товара, например название, 
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”, “шт.”, “шт.”]
}
'''
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        user_data = input(f'{f}: ')
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(features[f])
    goods.append((num, features.copy()))
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)


