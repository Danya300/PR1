#1
# from math import sin
# import random
# x = int(input('x='))
# if x > 0:
#     y = sin(x)**2
# else:
#     y = 1 - (2 * sin(x * x))
# print(y)
#2
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# n=input("Введите целое трехзначное число: ")
# if n==n[2]+n[1]+n[0]:
#     print("Палиндром")
# else:
#     print("Не палиндром")
#3
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# num = int(input('Введите число: '))
# number_1 = num // 100
# number_2 = num // 10 % 10
# number_3 = num % 10
# # a)
# if number_1 == number_2 == number_3:
#     print('a) Да')
# else:
#     print('a) Нет')
# # б)
# if number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
#     print('б) Да')
# else:
#     print('б) Нет')
#4
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# N = random.randrange(100,1000)
# print("Число: ", N)
# d2 = int(N/100)
# d1 = int((N-d2*100)/10)
# d0 = N%10
# print("Сотни: ", d2)
# print("Десятки: ", d1)
# print("Единицы: ", d0)
# print("Другое число: ", d1*100 + d0*10 + d2)
#5
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# x = int(input("Введите число "))
# print((x%100%10)*100+x//10)
#6
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# a = int(input())
# s=str(a)
# print(f'{s[1]}{s[0]}{s[2]}')
#7
# import math
# for i in range(100, 999, 1):
#     if ((str((i % 10)) + str((math.floor(((i - (i % 10))) / 10)))) == "237"): 
#         print(i)
#8
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
#9

# n = int(input())
# sum_of_factorials = 1
# curr_factorial = 1
# for i in range(2, n + 1):
#     curr_factorial *= i
#     sum_of_factorials += curr_factorial
# print(sum_of_factorials)
#10
# n = int(input()) # Получаю сумму для обработки
# money = [] # Делаю список для хранения количества купюр чтобы набрать необходимую сумму
# money_range = sorted([1, 2, 4, 8, 16, 32, 64], reverse=True) # Делаю номиналы имеющихся купюр, для нашей задачи их
# # необходимо расставить по убыванию
# 
# for i in range(0, len(money_range)): # Прохожу по money_range и пытаюсь выяснить сколько в сумме каких купюр
# # Если взять сумму 221 то в нее входит 3 купюре номиналом 64, то есть при делении на цело мы получим число 3
#     if n // money_range[i] != 0:
#         num = n // money_range[i] # В переменную сохраняю количество вхождения купюры определенным номиналом
# for j in range(0, num): # Прохожу указанное количество раз размером который сохранен в переменной num
#     money.append(money_range[i]) # За один проход вписываю номинал купюры в наш список money
#     n -= money_range[i] # Вычитаю из общей суммы номинал купюре
# else:
# 
#     print(*money) # Вывожу данные в консоли
#11
# for n in range(10):
#     for k in range(20):
#         for m in range(200):
#             if 10000*n + 5000*k + 500*m == 100000 and n+k+m == 100:
#                 print(f'{ n } быков\n{ k } коров\n{ m } телят')
#12
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print( sum(v for i,v in enumerate(a) if not i%2) - sum(v for i,v in enumerate(a) if i%2))
#13
# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([str(i) for i in a]))
# 14
# from past.builtins import xrange
# def palin_generator():
#     """Generates palindromic numbers."""
# 
#     palindromes=[]
# 
#     for count in xrange(1000):
#         n = str(count)
#         if n == n[::-1]:
#             palindromes.append(n)
# 
#     print (palindromes)  
# 15
# def main(l):
#     print(*(i for i in l if i[-1] == '0'))
#  
# input()
# lst = input().split()
#  
# main(lst)
# 16
# a=list(input())
#  
# c = 0;
# for i in a:
#     for j in a:
#         if i == j:
#            c+=1
#     c-=1
# print (c / 2)
# 17
# grades = [5, 4, 5, 3, 2, 5, 4, 3, 5, 5, 4, 2, 2, 3]
# print(f'Средний балл: {sum(grades) / len(grades)}')
# print(*grades, sep=';')
# 18
# print([i**2 if i%2 == 0 else i+2 for i in range(1,21)])
#19
# def conv(n,r):
#     if n<r:
#         return "0123456789ABCDEF"[n]
#     else:
#         k=n%r
#         return conv(n//r,r)+"0123456789ABCDEF"[k]
#         
# print(conv(12,2))
#20
# l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
# 
# divisible_by_7 = []
# 
# for i in l:
#     if (i%7==0):
#         divisible_by_7.append(i)
# print(divisible_by_7)
#21
# s = 'катя,маша,таня,саша'
# print(s.title())
# 22
# names = ['Маша', 'Петя', 'Вася']
# secret_names = list(map(lambda x: hash(x), names))
# print(secret_names)
# 23
# a = set('1234')
# b = set('3456')
# print(a | b)
# print(a & b)
# print(a - b)
#24
# import re
# a = '''She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.'''
#  
# print(len({x for x in re.findall(r'\w+', a)}))
#25
# d = dict()
# with open("C:/Users/danii/Desktop/Текстовый документ.txt", 'r') as file:
#     for line in file:
#         for word in line.strip().split():
#             d[word] = d.get(word, -1) + 1
#             print(d[word], end=' ')
#26
# from collections import Counter
# 
# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
# nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
# esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
# in culpa qui officia deserunt mollit anim id est laborum."""
# 
# myLine = text.split()  
# d = Counter(myLine)  
# max_encounters = max(d.values())  
# most_common_word = min(word for word, count in d.items() if count == max_encounters)  
# print(most_common_word) 
# 27
# def main():
#     with open('input.txt') as f:
#         nums = f.read().split()
# 
#     a, b = map(int, nums)
#     result = a + b
# 
#     with open('output.txt', 'w') as f:
#         f.write(str(result))
# 
# 
# if __name__ == '__main__':
#     main()
#28
# with open(input())as f:print('Yes'if input()in f.read()else'No')
# 
# a,b=float(input()),float(input())
# with open(input(),'w')as f:f.write(('%s\n'*4)%(a+b,a-b,a*b,a/b))
# # 29
# with open('input.txt') as t:
#     print(*(sum(map(int, line.split())) for line in t.readlines()), sep='\n')
#30
# s='''Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated'''
# from io import StringIO
# 
# print('буква '+ str(sum(map(str.isalpha,s))))
# print('слов '+str(len(s.split())))
# 
# print('срок '+str(len(s.split('\n'))))

