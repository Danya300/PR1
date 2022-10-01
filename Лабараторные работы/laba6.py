#1
#print(len(set(input().split())))
#2
#print(len(set(input().split()) & set(input().split())))
#3
# print(len(set(in_file.read().split())))
#4
# s = int(input())
# mass=[]
# for i in range(s):
#     mass.append(set())
#     for j in range(int(input())):
#         mass[i].add(input())
# evr = set.intersection(*mass)
# all = set.union(*mass)
# print(len(evr), *sorted(evr), sep='\n')
# print(len(all), *sorted(all), sep='\n')
#5
# x = {1, 2, 3}  
# y = {4, 3, 6}  
#  
# print(x | y)
#6
# slov = {}                   ### словарь для строк
# for i in range(int(input())):
#     str = input().split()   ### ввод строк
#     for j in str:           ### словам из строки задаём счётчик 
#         slov[j] = slov.get(j, 0) + 1 ### по поиску этого же слова в словаре
# for j in sorted(slov.items(), key = lambda x: (-x[1],x[0])): ### выводим слова
#     print(j[0]) ### используя словарь, и функцию для сортировки по убыванию
#
#7
# a = ['mamao', 'abacate', 'pera', 'goiaba', 'uva', 'abacaxis', 'laranja', 'maca']
# 
# 
# def find_longest_word(a):
# 
#     d = []
#     for c in a:
#         d.append(len(c))
#         e = max(d)  #Try "min" :D
#     for b in a:
#         if len(b) == e:
#             print ("самое длинное слово %i букв в слове %s" %(len(b), b))
# print(find_longest_word(a))


#8
# text = 'a a a a the the the the'
#  
# l_text = txt.split()
# s_text = set(text.split())
#  
# MyData = sorted(zip([l_text.count(w) for w in s_text], s_text), reverse=True)
# for txt1 in MyData:  
#     if(txt1[0] >= MyData[0][0]):
#         ResData = txt1   
# print(ResData)
#9
# sales_dict = {}
# def inputs():
#     while True:
#         try:
#             yield input().split()
#         except (ValueError, EOFError):
#             return    
# 
# for customer, purchase, count in inputs():
#     if customer not in sales_dict:
#         sales_dict[customer] = {purchase : int(count)}
#     else:
#         sales_dict[customer][purchase] = sales_dict[customer].get(purchase, 0) + int(count)
# 
# for customer, purchases in sorted(sales_dict.items()):
#     print(customer +':')
#     for purchase, count in sorted(sales_dict[customer].items()):
#         print(purchase, count)
#10
# n = int(input())
# cities = {}
# for _ in range(n):
#     line = input().split()
#     for city in line[1:]:
#         cities[city] = line[0]
# 
# for _ in range(int(input())):
#     print(cities[input()])
