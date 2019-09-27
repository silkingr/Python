# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
print ("----------Задача 1-------------")
equation = 'y = -12x + 11111140.2121'
x = 2.5
# # вычислите и выведите y
# # y = -12*x + 11111140.2121
# # print (y)
# # Решение задачи в заданном частном виде. equation = 'y = -12x + 11111140.2121'
str_koeff1 = equation[4:7]
str_koeff2 = equation[11:]
koeff1 = float(str_koeff1)
koeff2 = float(str_koeff2)
y = koeff1*x + koeff2
print (y)
#
# #Решение задачи в общем виде. Считаем, что заданное выражение приведено к виду "y = kx + b", и нет лишних пробелов
a1 = equation.find("=")
a2 = equation.find("x")
str_koeff1 = equation[a1+1:a2]  #Нашли k
str_koeff2 = equation[a2+3:]    #Нашли b
koeff1 = float(str_koeff1)
koeff2 = float(str_koeff2)
y = koeff1*x + koeff2
print (y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
print ("----------Задача 2-------------")
# Пример корректной даты
# date = '01.11.1985'
#
# # Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'
#
date = input("Введите дату в формате dd.mm.yyyy :")
print("Ведена дата ", date)
a1 = date.find(".")
a2 = date.rfind(".")
# print(a1,a2)
#
str_day = date[:a1]      #получаем день
str_month = date[a1+1:a2]   #получаем месяц
str_year = date[a2+1:]     #получаем год
#print("День - ", str_day, ", месяц - ", str_month, ", год - ", str_year)
day = int(str_day)
month = int(str_month)
year = int(str_year)
#print("День - ", day, ", месяц - ", month, ", год - ", year)
yes = True
while True:
    if len(str_day)==2 and len(str_month)==2 and len(str_year)==4:
        yes = True
    else:
        yes = False
        print ("Дата не соответствует формату 2 символа для дня, 2 - для месяца, 4 - для года")
        break
    if not int(year) in range(1,10000):
        yes = False
        print ("Год не в диапазоне от 1 до 9999")
        break
    if not int(month) in range(1,13):
        yes = False
        print("Месяц не в диапазоне от 1 до 12")
        break
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) in range(1, 32):
            yes = True
        else:
            yes = False
            print("Неправильное число дня")
            break
    else:
        if int(day) in range(1, 31):
            yes = True
        else:
            yes = False
            print("Неправильное число дня")
            break
    break
if yes:
    print("Дата введена корректно")
else:
    print("Дата введена некорректно.")


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...           floor = 7, kabinet = 4 n15=f+k+4, n16=f+k+5, n17=f+k+6
#     12  13  14        floor = 6, kabinet = 3 n12=f+k+3, n13=f+k+4, n14=f+k+5
#     9   10  11        floor = 5, kabinet = 3 n9=f+k+1, n10=f+k+2, n11=f+k+3
#     6   7   8         floor = 4, kabinet = 3 n6=f+k-1, n7=f+k,    n8=f+k+1
#       4   5           floor = 3, kabinet = 2 n4=f+k-1, n5=f+k
#       2   3           floor = 2, kabinet = 2 n2=f+k-2, n3=f+k-1
#         1             floor = 1, kabinet = 1 n1=f+k-1
#


# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
print ("----------Задача 3-------------")
number = 0
while (number < 2) and (number <=2000000000):
    number = int(input("Введите номер комнаты (больше 1): "))
m = 1 # номер группы
sum=1
while number > sum:
#    print("m= ",m)
    kube = m*m
    sum += kube
#    print (sum, kube)
    m +=1
# знаем номер группы - m-1
# группа n начинается с числа z
z=1 # число начала группы
for i in range(1,m-1):
    z +=i*i
#print (z) # начало группы
floor = 1
for i in range(1,m-1):
    floor +=i
#print(floor) # этаж начала группы
while (z+m-1)<=number:
    z +=m-1
    floor +=1
#print(z,floor)
l=1
while number>z:
    z +=1
    l +=1
#print (z,floor,l)
print ("Номер комнаты -", number," номер этажа - ",floor," порядковый номер слева на этаже - ",l)
