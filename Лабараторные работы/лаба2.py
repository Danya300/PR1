#1
# x = int(input("Enter a number: "))
# if x>4:
#     print('II')
# else:
#     print('I');
#2
# y = int(input("Enter a number: "))
# if y>3:
#     print('I')
# else:
#     print('II');
#3
# x = float(input())
#а print('y', 0 if x <= -1 else 2 if x >= 2 else x - 1)
#б print('y', 0 if x <= -1 else -3 if x >= -3 else x - 1)
#4
# a = int(input("Введите a : ")) # Вводим число a
# b = int(input("Введите b : ")) # Вводим число b
# 
# if a > b:
#     print("a больше, чем b")
# elif a < b:
#     print("b больше, чем a")
# else:
#     print("a равно b")
#5
# import sys
# 
# min = sys.float_info.max
# max = sys.float_info.min
# 
# for i in range(2):
#     a = float(input('enter number '))
# 
#     if a > max:
#         max = a
# 
#     if a < min:
#         min = a
# 
# print('\n', 'min is: ', round(min,2), '\n', 'max is: ', round(max,2))
#6
# import datetime
#  
#  
# def db(d1, d2):
#     date_format = "%m/%Y"
#     delta = datetime.datetime.strptime(d2, date_format) - datetime.datetime.strptime(d1, date_format)
#     return delta.days / 365
#  
#  
# print("%d" % db('01/2003', '09/2022'))
#7
# from math import sin
#  
#  
# x = float(input())
#  
# if x > 0:
#   y = sin(x)**2
# else:
#   y = 1-sin(x)**2
#  
# print(y)
#8
# from math import sin
#  
#  
# x = float(input())
#  
# if x > 0:
#   y = sin(x)**2
# else:
#   y = 1+sin(x**2)
#  
# print(y)
#9
# a = int(input())
# b = int(input())
#  
# print("YES" if not (a and b) or not (a % b and b % a) else "NO")
#10
# n = int(input())
# if n % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')
#  
# if n % 10 == 7:
#     print('Число оканчивается на 7')
# else:
#     print('Число не оканчивается на 7')
#11
# n = int(input())
# max1 = max(n % 10, n // 10)
# check = False
# if max1 == n // 10 != n % 10:
#     check = True
#     print('Первая цифра числа больше')
# elif max1 == n % 10 != n // 10:
#     check = True
#     print('Вторая цифра числа больше')
#  
# if not check:
#     print('Цифры числа одинаковы')
# else:
#     print('Цифры числа различны')
#12
# num = input()
# 
# print('Yes' if num == num[::-1] else 'No')
#13
# def array(x):
#     nums = []
#     while x > 0:
#         b = x % 10
#         nums.append(b)
#         x //= 10
#     return list(reversed(nums))
# 
# 
# x = int(input('Введите число: '))
# a = array(x)
# print('Да' if len(set(a)) != len(a) else 'Нет')
#14
# n = int(input())
# if n % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')
#15
# print('green' if 0 <= float(input()) % 5 <= 3 else 'red')
#16
# M = int(input("Введите массу в килограммах (M): "))
# m = int(M / 1000)
# print("Количество полных тонн: ", m)
#17
# x = 543 * 130
# y = 130**2
# z = 70590/16900
# print(z)
#18
# m = int(input('m='))
# a = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# print(a[m % 12])
#19
# b=int(input())
# print(b%10*100+b%100//10*10+b//100)
#20
# print(input()[::-1])
# #21
# import random
# N = random.randrange(100,1000)
# print("Число: ", N)
# d2 = int(N/100)
# d1 = int((N-d2*100)/10)
# d0 = N%10
# print("Сотни: ", d2)
# print("Десятки: ", d1)
# print("Единицы: ", d0)
# print("Другое число: ", d1*100 + d0*10 + d2)
# 22
# print(*map(lambda x: x[1] + x[0] + x[2:], (input(),)))
# 23
# pn = int(input())
# x = n // 100 * 100 + n % 10 * 10 + n % 100 // 10
# print(x)
#24
# import itertools
# print(list(itertools.permutations([1,2,3], 3)))
#25
# x = int(input())
# print(str(x)[-2] if abs(x) > 9 else 0)
#26
# a = int(237)
# b = int(a//100)
# c = int(a%100)
# x = c*10+b
# print(x)
#27
# n = input('? ')
# a= str(n)[:-1]
# d = str(n[-1])
# print(int(d + a))
#28
# n = int(input())
# print((n % 10)*100+(n // 10))
#29
# n = int(input())
# x = n % 10 + n // 100 * 10 + n % 100 // 10 * 100
#30
# def f(h,m,s):
#     return (h//24)*30+m/60+h/3600
#31
# grad = float(input()) * 2
# h = int(grad // 60)
# m = int(grad % 60)
# print('{}:{:02d}'.format(h, m))
#32
# import datetime
# from math import floor
# now = datetime.datetime.now()
# m = float(now.minute) + float(now.second/60)
# ugol = m/5*30
# print(str(now.hour) + " час " + str(now.minute) + " минут")
# print(str(floor(ugol)) + " Угол")
#33
# a = int(input())
# b = int(input())
# c = int(input())
# #а
# print((a>100) and (b>100))
# #б
# print (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
# #в
# print(a>0) or (b>0)
# #г
# print((a%3==0 and b%3==0 and c%3==0))
# #д
# if a % 2 == 0 and b % 2 == 0 and  c % 2 == 0:
#     print("NO")
#     exit()
# if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
#     print('YES')
# else:
#     print('NO')
# #е
# print((a<0) or (b<0) or (c<0))
#34
# x1, y1, x2, y2 = [input() for _ in range(4)]
# print('YES' if (x1 == x2) is not (y1 == y2) else 'NO')
