#1
# kd=float (input ("Введите курс доллара "))
# k=float (input ("Введите курс евро "))
# print ("1) Перевести из рублей в доллары и евро\n2) Перевести из долларов и евро в рубли\n")
# vibor=int (input ("Выберите ваше действие\n"))
# if vibor==1:
#     ryb=float(input("Введите количество рублей "))
#     s1=ryb/kd
#     s2=ryb/k
#     print ("Сумма вашего перевода из рублей в доллары = ",'{:.2f}'.format(s1))
#     print("Сумма вашего перевода из рублей в евро = ",'{:.2f}'.format(s2))
# elif vibor==2:
#     kold=float (input ("Введите количество долларов "))
#     kol=float (input ("Введите количество евро "))
#     s1=kold*kd
#     s2=kol*k
#     print ("Сумма вашего перевода из доллара в рубли = ",'{:.2f}'.format(s1))
#     print("Сумма вашего перевода из евро в рубли = ",'(:.2f}'.format(s2))
# else:
#     print ("Ошибка! Введите, пожалуйста, только 1 или 2")
#     exit (0)
#2
# print('Таблица умножения')
#  
# for i in range(1, 10):
#     for k in range(2, 10):
#         print(f'{i} * {k} = {i * k}\t', end='')
#     print('')
# else:
#     print('')
#3
# A = int(input())
# B = int(input())
#  
# ans = 0
#  
# for i in range(A, B + 1):
#     ans += i ** 2
#  
# print(ans)
#4
# n = 12345
# print( str(n)[::-1] )
#5
# n = int(input())
# sum_of_factorials = 1
# curr_factorial = 1
# for i in range(2, n + 1):
#     curr_factorial *= i
#     sum_of_factorials += curr_factorial
# print(sum_of_factorials)
#6
# lst = [-1,-2,-3,-5,-6,-7,-7,9,7,4,9]
# count = 0
# index = 0
# while(lst[index]<0):
#    count+=1
#    index+=1
# print(count)
#7
# fib1 = fib2 = 1
#  
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n) - 2
#  
# while n > 0:
#     fib1, fib2 = fib2, fib1 + fib2
#     n -= 1
#  
# print("Значение этого элемента:", fib2)
#8
# n = list(input('Введите n: '))
# print(n.count(max(n)))
#9
# n, f, s = map(float, input('n, f, s = ').split())
# if s != 0:
#     if n == f:
#         print('Нет')
#     else:
#         if s<0:
#             f, n = n, f
#             s = abs(s)
#         while f<n:
#             f += s
#         print('Да' if n == f else 'Нет')
# else:
#     print('Да' if n == f else 'Нет')
#10
# cheslo = int(234567891)
# cheslo = str(cheslo)
# ok = []
# for i in cheslo:
#     ok.append(i)
# print(ok)
# print(ok.index(max(ok)))
# ok.reverse()
# print(ok.index(max(ok)))
#11
# from math import *
# f = int(input("Введите факториал числа n:"))
# for n in range(1,f+1):
#     if(n==f):
#         print("Текст")
#         break
#     if factorial(n) == f:
#         print(n)
#         break
#12
# n = int(input()) 
# money = [] 
# money_range = sorted([1, 2, 4, 8, 16, 32, 64], reverse=True) 
# 
# 
# for i in range(0, len(money_range)): 
# 
#     if n // money_range[i] != 0:
#         num = n // money_range[i] 
# for j in range(0, num): 
#     money.append(money_range[i]) 
#     n -= money_range[i] 
# else:
#     
#     print(*money) 
#13
# for b in range (1, 100//10+1):
#     for k in range(1, 100//5+1):
#         for t in range(1, 101-b-k):
#             if b+k+t == 100 and b*10+k*5+t*0.5 == 100:
#                 print("быки:", b, "коровы:", k, "телята:", t)
#14
# e=int(input())
# i = 0
# for e in range(e):
#     e += 1
# i = i + e ** 2
# print (i)

