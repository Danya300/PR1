#1
# from random import randrange
# n = 12
# a = [randrange(163, 191) for i in range(n)]
# print(a)
#2
# def ar_progression(a_n, d, k):
#     #An+1 = Q
#     i = 0
#     for i in range(k):
#         Q = a_n + d
#         print(Q)
#         a_n = Q
# Y= int(input( 'Введите первый эл-нт прогрессии (An)'))
# r = int(input( 'Введите разность прогрессии (d): '))
# kol = int(input('Введите кол-во зл-ов прогрессии: '))
# ar_progression(Y, r, kol)
# 3
# elements = [1, 2, 3, 4, 5, 6]
# elements.reverse()
# print(elements)
#4
# a = [int(x) for x in input().split()]
# print(sum(a[::2]) - sum(a[1::2]))
#5
# k=[10,10,20,40,35,30,10,10,20,40,35,30,10,10,20,40,35,30,10,10,20,40,35,30,10,10,20,40,35,30,10,20,40,35,30,10,10,20,40,35,30,10]
# t=str(sum(k))
# print("Общее число учеников ",t)
# if len(t)==4 :
#     print(" есть четырехзначное число")
# else :
#     print(" не является четырехзначным числом")
#6(а)
# s=input()
# a=[int(s) for s in s.split()]
# for i in a:
#     if int(i)%2 == 0:
#        print(i, end=' ')
#6(б)  
# def main(l):
#     print(*(i for i in l if i[-1] == '0'))
#  
# input()
# lst = input().split()
#  
# main(lst)
#7
# math = ['60', '50', '40']
# inf = ['60', '50', '40']
# rus = ['60', '50', '40']
# stud = ['Иванов', 'Петров', 'Сидоров']
# d = zip(math, inf, rus,stud)
# print(tuple(d))
# max_number = max(math), max(inf), max(rus)
# min_number = min(math), min(inf), min(rus)
# if min_number:
#     print('Не зачислен')
# else:
#     print('Зачислен')
# print("Наибольший балл:", max_number)
# print("Наименьший балл:", min_number)
#8
# lst=[int(i) for i in input().split()]
# print(len(set(lst)))
#9
# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([str(i) for i in a]))
#10
# import random
# l = []
# r = int(input())
#     
# for i in range(r):  #создаем список
#     l.append(random.randint(-5,5))
# half = r//2  # для четного количества элементов списка
# shalf = r//2+r%2  # для нечетного кол-ва    _._._._._._._._._._
# print (l)
# if r%2 == 0: # проверка для четного кол-ва
#     print(l[half:] + l[0:half])  # меняем местами элементы
# else:
#     nl = l[half+1:]+ l[shalf-1:shalf] + l[0:half]  # если проверка не пройдена, то меняем местами, при этом оставляем средний 
#     print(nl)                                      # элемент списка посередине
#11
# a = [int(s) for s in input().split()]
# guests = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             guests += 1
# print(guests)
#12
# mylist = ['45', '45', '46', '58', '45', '57', '56']
# myset = set(mylist)
# print(myset)
#13
# from functools import reduce
#  
# a = [17,18,19]
# b = [['Dwain Payne', 'Samuel Caldwell', 'Homer Conley'], ['Rose Fitzgerald', 'Betty Watkins'], ['Cecily Bradford', 'Nicholas Taylor', 'Alexina Daniel', 'Josephine Sparks']]
# c = list( reduce(lambda x,y: x+y, b) )
#  
# print(len(c), min(b, key=len), max(b, key=len), sorted(c))
#14
# grades = [5, 4, 5, 3, 2, 5, 4, 3, 5, 5, 4, 2, 2, 3]
# print(f'Средний балл: {sum(grades) / len(grades)}')
# print(*grades, sep=';')
#15
# print([i for i in range(1, 10001) if (not i%3 and not i%7) or not i%9])
#16
# def EXwhile6 ():
#     
#     #Init
#     a = input ("Напишите, сколько строк вы хотите напечатать: ")
#     a = int(a)
#     K = 1
#     #Condition
#     while K <= a: 
#         #Action
#         line = str(K)
#         #Update
#         line2 = line + str(K)
#         print (line2)
#         K += 1
# EXwhile6 ()
#17
# a = [[i,10*i] for i in range(1,5)]
# print(a)
# b = sum(a,[])
# print(b)
#18
# print([i**2 if i%2 == 0 else i+2 for i in range(1,21)])

