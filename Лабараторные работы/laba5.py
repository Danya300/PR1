#2 вар1
# def f(x: float) -> float:
#     return x ** 6 - ((2*x-7))
#  
#  
# print(f"y = {f(float(input('x = ')))}")
# #2 вар8
# import math
#  
#  
# def f(x: float) -> float:
#     return 3 ** (-x) - (x**2)+1
#  
#  
# print(f"y = {f(float(input('x = ')))}")
#3
# from math import sin, cos
#  
#  
# def f(x):
#     print(sin(x+1)-y-1.2)
#     print(2*x+cos(y)+2*x-2)
#     return ''
# x = float(input('x = '))
# y = float(input('y = '))
# 
# 
# print(f(x))
#4 вар1
# def even_or_odd(a):
#     if a % 2 == 0:
#         print('Четное число')
#     else:
#         print('Нечентное число')
#4 вар8
# n = int(input("Введите число:"))
# def f(n):
#     count = 0
#     while n > 0:
#         count = count + 1
#         n = n // 10
#     return "Количество цифр равно:", count
# print(f(n))
#5 вар 1
# num = [int(x) for x in input().split()]
# 
# def f(num):
#     print('минимальное = ', min(num))
#     print('максимальное = ', max(num))
#     return ''
# 
# 
# # some_function(num)
# print(f(num))  # "num" изменился
#6
# def f(n, b):
#     if n < b:
#         print(n, end='')
#     else:
#         f(n//b, b)
#         print(n % b, end='')
#  
# f(123, 3)
#7
# l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
# 
# divisible_by_7 = []
# 
# for i in l:
#     if (i%7==0):
#         divisible_by_7.append(i)
# print(divisible_by_7)
#8
# s = 'катя,маша,таня,саша'
# print(s.title())
# 9
# Имяs = ['Маша', 'Петя', 'Вася']
# secret_Имяs = list(map(lambda x: hash(x), Имяs))
# print(secret_Имяs)
#10
# Имяs = ['Маша', 'Петя', 'Вася']
# secret_Имяs = list(map(lambda x: hash(x), Имяs))
# print(secret_Имяs)
#11
# from functools import reduce
#  
# s = ['научиться плести рыболовные сети', 'обучать нейронные сети', 'паук ловит в сети мух']
# print(reduce(lambda x, y: x + y, map(lambda x: 'сети' in x.lower(), s), 0))
#12
# my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
# new_list = list(filter(lambda x: (x%7 ==0), my_list))
# print(new_list)
#13
Группа = [
    {
        "Имя": "StudentOne",
        "Группа": "111",
        "Возраст": 21,
        "Оценки": [4, 3, 5, 5, 4]
    },
    {
        "Имя": "StudenTwo",
        "Группа": "111",
        "Возраст": 22,
        "Оценки": [3, 2, 3, 4, 3]
    },
    {
        "Имя": "StudentThree",
        "Группа": "111",
        "Возраст": 23,
        "Оценки": [3, 5, 4, 3, 5]
    },
    {
        "Имя": "StudentFour",
        "Группа": "111",
        "Возраст": 24,
        "Оценки": [5, 5, 5, 4, 5]
    }
]
def print_studs(students):
    
    t = '{:<16}{:<8}{:<8}{}'
    print(t.format('Имя', 'Группа', 'Возраст', 'Оценки'))
    print('\n'.join([t.format(s['Имя'], s['Группа'], s['Возраст'], s['Оценки']) for s in students]))
 
 
def all_students(students):
    
    
    return students
    
 
def students_avg(students, n):
    
    
    return [s for s in students if sum(s['Оценки'])/len(s['Оценки']) > n]
 
print_studs(all_students(Группа))
print()
print_studs(students_avg(Группа, 4))




