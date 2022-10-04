#1
# with open('1.txt') as datfile:
#     text = datfile.read()
# print(sum(map(int, text.split(None, 2)[:2])))
#2
# import mmap
# 
# with open('2.txt', 'rb', 0) as file, \
#     mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
#     if s.find(b's') != -1:
#         print('True')
#     else:
#         print('False')

# with open('3.txt') as t:
#     print(*(sum(map(int, line.split())) for line in t.readlines()), sep='\n')
#4
 # Переменные для подсчета строк, слов и букв.
# lines = 0
# words = 0
# letters = 0
#  
# 
# for line in open('4.txt', 'r'):
#     
#     lines += 1 
#     
#     letters += len(line)      
#     pos = 'out'
#  
#     
#     for letter in line:
#         
#         if letter != ' ' and pos == 'out':
#             
#             words += 1
#             
#             pos = 'in'
#         
#         elif letter == ' ':
#             
#             pos = 'out'
# print("Lines:", lines)
# print("Words:", words)
# print("Letters:", letters)
#5
# file = '5.txt'
#  
# action = input("Введите от 'а' до 'д': ").lower() #а б в г д
#  
# with open(file) as f:
#     data = f.readlines()
#  
# if action == 'а':
#     print(*data[0])
# elif action == 'б':
#     print(*data[4])
# elif action == 'в':
#     print(*data[0:4])
# elif action == 'г':
#     s1, s2 = map(int, input('Введите s1 и s2 через пробел: ').split())
#     print(*data[s1-1 : s2-1])
# elif action == 'д':
#     print(*data)
#6
# large_line = ''
# large_line_len = 0
# filename = r'5.txt'
# 
# with open(filename, 'r') as f:
#     for line in f:
#         if len(line) > large_line_len:
#             large_line_len = len(line)
#             large_line = line
# 
# print (large_line)
#7
# file = open('7.txt', 'r')
# s = file.readlines()
# s.reverse()
# print(''.join(s))
# #8
# count = 0
# eq = True
# with open("81.txt", "r", encoding = "utf-8") as f1, open("82.txt", "r", encoding = "utf-8") as f2:
#     for a1, a2 in zip(f1, f2):
#         count += 1
#         if a1 != a2:
#             eq = False
#             break
# print(f"Нет отличий") if eq else print(f"Отличается строка {count}")
#10
# inFile = open('10.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')
# k = inFile.readline()
# k = int(k)
# rez = []
# l = inFile.readlines()
# for i in l:
#     if len(i.split()) == 6:
#         n1, n2, n3, s1, s2, s3 = i.split()
#     if len(i.split()) == 5:
#         n1, n2, s1, s2, s3 = i.split()
#  
#     if int(s1) >= 40 and int(s2) >= 40 and int(s3) >= 40:
#         sum = int(s1) + int(s2) + int(s3)
#     else:
#         sum = 0
#     rez.append(sum)
# rez.sort(reverse=True)
# if rez[k] == 0:
#     print(0)
# elif rez[0] == rez[k]:
#     print(1)
# elif rez[k] == rez[k - 1]:
#     print(rez[k - 2])
#  
# else:
#     print(rez[k - 1])
# inFile.close()
# outFile.close()