print('''

███╗░░██╗░█████╗░██████╗░███████╗██╗░░░██╗
████╗░██║██╔══██╗██╔══██╗██╔════╝██║░░░██║
██╔██╗██║███████║██████╔╝█████╗░░██║░░░██║
██║╚████║██╔══██║██╔══██╗██╔══╝░░██║░░░██║
██║░╚███║██║░░██║██║░░██║██║░░░░░╚██████╔╝
╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░
''')
class faculties:
 
    # A simple class
    # attribute
    attr1 = "название факультета"
    attr2 = "ФИО декана"
    attr3 = "номер комнаты"
    attr4 = "номер корпуса"
    attr5 = "телефон"
    # A sample method
    def fun(self):
        print(self.attr1,"номер 1")
        print(self.attr2,"Соколова Полина Кирилловна")
        print(self.attr3,"356")
        print(self.attr4,"2 корпус")
        print(self.attr5,"7(175)850-81-23")
        
 
# Driver code
# Object instantiation
факультеты = faculties()
 
# Accessing class attributes
# and method through objects
факультеты.fun()
print('''

██╗░░██╗░█████╗░███████╗███████╗██████╗░██████╗░░█████╗░
██║░██╔╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗
█████═╝░███████║█████╗░░█████╗░░██║░░██║██████╔╝███████║
██╔═██╗░██╔══██║██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██╔══██║
██║░╚██╗██║░░██║██║░░░░░███████╗██████╔╝██║░░██║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝''')
class kafedra:
 
    # A simple class
    # attribute
    attr1 = "Название кафедры"
    attr2 = "Факультет"
    attr3 = "ФИО заведующего"
    attr4 = "Номер комнаты"
    attr5 = "Номер корпуса"
    attr6 = "Телефон"
    attr7 = "Кол-во преподавателей."
    # A sample method
    def fun(self):
        print(self.attr1,'Экономический')
        print(self.attr2,"Общепрофессиональная")
        print(self.attr3,"Медведев Тимур Львович")
        print(self.attr4,"339")
        print(self.attr5,'3')
        print(self.attr6,"7(963)401-63-15")
        print(self.attr7,'4 преподавателя')
        
 
# Driver code
# Object instantiation
кафедра = kafedra()
 
# Accessing class attributes
# and method through objects
кафедра.fun()
print('''

██╗░░░░░███████╗░█████╗░██████╗░███╗░░██╗░██████╗░██████╗░░█████╗░██╗░░░██╗██████╗░
██║░░░░░██╔════╝██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗██║░░░██║██╔══██╗
██║░░░░░█████╗░░███████║██████╔╝██╔██╗██║██║░░██╗░██████╔╝██║░░██║██║░░░██║██████╔╝
██║░░░░░██╔══╝░░██╔══██║██╔══██╗██║╚████║██║░░╚██╗██╔══██╗██║░░██║██║░░░██║██╔═══╝░
███████╗███████╗██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░░██║╚█████╔╝╚██████╔╝██║░░░░░
╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░░░░''')
class learngroup:
 
    # A simple class
    # attribute
    attr1 = "название группы"
    attr2 = "год поступления"
    attr3 = "курс обучения"
    attr4 = "кол-во студентов в группе"
    
    # A sample method
    def fun(self):
        print(self.attr1,'крутыши')
        print(self.attr2,"2019")
        print(self.attr3,"3 курс")
        print(self.attr4,"30 студентов")
       
        
 
# Driver code
# Object instantiation
Учебнаягруппа = learngroup()
 
# Accessing class attributes
# and method through objects
Учебнаягруппа.fun()
print('''

░██████╗████████╗██╗░░░██╗██████╗░███████╗███╗░░██╗████████╗░██████╗
██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔════╝
╚█████╗░░░░██║░░░██║░░░██║██║░░██║█████╗░░██╔██╗██║░░░██║░░░╚█████╗░
░╚═══██╗░░░██║░░░██║░░░██║██║░░██║██╔══╝░░██║╚████║░░░██║░░░░╚═══██╗
██████╔╝░░░██║░░░╚██████╔╝██████╔╝███████╗██║░╚███║░░░██║░░░██████╔╝
╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░''')
class students:
 
    # A simple class
    # attribute
    attr1 = "Фамилия"
    attr2 = "Имя"
    attr3 = "Отчество"
    attr4 = "Группа"
    attr5 = "Год рождения"
    attr6 = "Пол"
    attr7 = "Адрес"
    attr8 = "Город"
    attr9 = "Телефон"
    # A sample method
    def fun(self):
        print(self.attr1,'Алёшин')
        print(self.attr2,"Даниил")
        print(self.attr3,"Александрович")
        print(self.attr4,"ИС-3")
        print(self.attr5,'2003')
        print(self.attr6,"Мужской")
        print(self.attr7,'Химиков 23')
        print(self.attr8,"Архангельск")
        print(self.attr9,'7(963)401-63-15')
        
 
# Driver code
# Object instantiation
студенты = students()
 
# Accessing class attributes
# and method through objects
студенты.fun()
print('''
██╗░░░██╗███████╗██████╗░░█████╗░███╗░░░███╗░█████╗░░██████╗████████╗██╗
██║░░░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝╚══██╔══╝██║
╚██╗░██╔╝█████╗░░██║░░██║██║░░██║██╔████╔██║██║░░██║╚█████╗░░░░██║░░░██║
░╚████╔╝░██╔══╝░░██║░░██║██║░░██║██║╚██╔╝██║██║░░██║░╚═══██╗░░░██║░░░██║
░░╚██╔╝░░███████╗██████╔╝╚█████╔╝██║░╚═╝░██║╚█████╔╝██████╔╝░░░██║░░░██║
░░░╚═╝░░░╚══════╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝''')
class vedomosti:
 
    # A simple class
    # attribute
    attr1 = "Группа"
    attr2 = "Студент"
    attr3 = "Предмет"
    attr4 = "Оценка"
    # A sample method
    def fun(self):
        print(self.attr1,'Ис-3')
        print(self.attr2,"Алёшин Даниил Александрович")
        print(self.attr3,"Англиский")
        print(self.attr4,"5")
        
 
# Driver code
# Object instantiation
ведомости = vedomosti()
 
# Accessing class attributes
# and method through objects
ведомости.fun()
