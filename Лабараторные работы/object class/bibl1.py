from dataclasses import dataclass
from collections import namedtuple
import pickle
import requests

class college():  
    def __init__(self, students, nomer):
        self.students = students
        self.nomer = nomer

# Конструктор
    def allstud(self):  
        x = b1.students + b2.students + b3.students + b4.students
        return (f"ул. Воронина,{self.nomer} в колледже 4 в группах находятся {x} студентов")

    def student_test(self):  # unittest
        x = b1.students + b2.students + b3.students + b4.students
        return x

# Сериализация
    def serialize(self):  # Сериализация номера библиотеки
        with open('C:\\Users\\danii\\Desktop\\object class\\test_pickuli.pkl', 'wb') as f:
            pickle.dump(self.nomer, f)
        f.closed

# Десериализация
    def deserialize(self):  # Десериализация номера библиотеки
        with open('C:\\Users\\danii\\Desktop\\object class\\test_pickuli.pkl', 'rb') as f:
            college = pickle.load(f)
        f.closed
        return college

# Деструктор
    # def __del__(self): # Уничтожение экземпляра
        #print(f"привет {self.nomer} пропал")

        # Наследование


class College(college):
    def __init__(self, students, nomer, name, kolvo_paidstud):
        super().__init__(students, nomer)
        self.name = name
        self.kolvo_kolvo_paidstud = kolvo_paidstud

    def Nazvanie(self):
        print(f"Название {self.name}")

    def Otdelbi(self):
        x = (self.students/round (2, 1))
        print(f"Количество бюджетников {x}")

    # Полиморфизм
    def allstud(self):
        print(f"Всего учатся в 4 группе {self.students} студентов.")


b1 = college(33, 34)
b2 = college(30, 2)
b3 = college(25, 3)
b4 = college(32, 4)
print(b1.allstud())
b2 = College(b2.students, b2.nomer, "Технологический колледж Императора Петра I САФУ", 1)
b2.Nazvanie()
b2.Otdelbi()
b2.allstud()


b1.serialize()
print(b1.deserialize())
b4.serialize()
print(b4.deserialize())
#del b1

#Inkapsulyatsia проерка сайта колледжа
class site(college):
    url='https://narfu.ru/ltk/'
    print('сайт колледжа', url)
    try:
        r = requests.get(url,timeout=3)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
#перезагрузка
class Student: 
    def __init__(self,name,marks): 
        self.name=name 
        self.marks=marks 
    def display(self): 
        print(self.name,self.marks) 
    def __add__(self,S): 
        temp=Student(S.name,[]) 
        for i in range(len(self.marks)): 
            temp.marks.append(self.marks[i]+S.marks[i]) 
        return temp 
S1=Student("Оценка за пары",[8,7,10]) 
S2=Student("Итого",[8,7,9]) 
S1.display() 

S3=Student("",[]) 
S3=S1+S2 
S3.display()
#Метапрограммирование
class MyDecorator:
    def __init__(self, function):
        self.function = function
        self.counter = 30
    
    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
        self.counter+=30
        print(f"Большая перемена длиться {self.counter} минут")


@MyDecorator
def some_function():
    return 42


some_function()
#Агрегация
class Storage(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except (KeyError, k):
            raise (AttributeError, k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except (KeyError, k):
            raise (AttributeError, k)

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'
cont = dict(Сетевое_и_системное_администрирование ='09.02.06 ',Организация_перевозок_и_управления_на_транспорте='23.02.01', Лесное_и_лесопарковое_хозяйство='35.02.01')
for k in cont:
    print( k, cont[k])
#Перезагрузка операторов

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
     # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
 
Ob1 = complex('И', 1)
Ob2 = complex('С', 2)
Ob3 = Ob1 + Ob2
print(Ob3)
#интерфейсы
from abc import ABC
from abc import abstractmethod
class Transport(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def get_info(self):
        pass
class group(Transport):
    def start(self):
        print('В группе')
    def stop(self):
        print('ИC3')
    def get_info(self):
        print('24 человека')
IS3 = group()
IS3.start()
IS3.stop()
IS3.get_info()
##dataclass
@dataclass
class Employee:
    name: str
    IS3: str = 'Python'


@dataclass
class Developer(Employee):
    stepenia: int = 0


Alex = Developer('Александр', 'Програмист', 2600)
print(Alex)
##Коллекции в Python
Features = namedtuple('Features', ['age', 'gender', 'name'])
row = Features(age=22, gender='male', name='Alex')
print(row.gender)
##Обобщенные классы в Python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
import re
  
def main():
    passwd = 'Student123@'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
    # compiling regex
    pat = re.compile(reg)
      
    # searching regex                 
    mat = re.search(pat, passwd)
      
    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")
  
# Driver Code     
if __name__ == '__main__':
    main()
username="studentikt"
password="student123@"
from getpass import getpass
uname=input('Имя пользователья - ')
uname=uname.strip()
if uname!=username:
    print("неправильно")
else:
    pword=getpass("Пароль - ")
    if pword==password:
        print("Добро пожаловать")
    else:
        print("Неправильный пароль")


