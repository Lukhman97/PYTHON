# class A:
#     def __init__(self,balance):
#         self.__balance=balance
    
#     def deposit1(self,amount):
#         self.__balance+=amount
    
#     def get_balance(self):
#         print(self.__balance)

# obj1=A(20000)
# obj1.deposit1(30000)
# obj1.get_balance()



# from abc import ABC,abstractmethod

# class vechile(ABC):
#     @abstractmethod
#     def start(self):
#         pass
   
# class car(vechile):
#     def start(self):
#         print("car engien start")

# my_car=car()
# my_car.start()


# from abc import ABC ,abstractmethod

# class animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class dog(animal):
#     def make_sound(self):
#         print("BOW BOW BOW")

# class cat(animal):
#     def make_sound(self):
#         print("MEOW MEOW MEOW")

# class cow(animal):
#     def make_sound(self):
#         print("'Coew Coew")

# li=[cat(),dog(),cow()]

# for i in li:
#     i.make_sound()




# from abc import ABC ,abstractmethod

# class Anial(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# # @abstractmethod
# def start(self):
#     print("It is an animal")


# a=Anial()
# a.start()



# # single inhertiance

# class vechile:
#     def move(self):
#         print("The vechile is moving................")
    
# class car(vechile):
#     def play_radio(self):
#         print("the pm channel was spotted")


# c=vechile()
# # b=vechile()
# c.move()
# c.play_radio()


# class a:
#     def move(self):
#         print("added it with ....")

# class b(a):
#     def start(self):
#         print("It is stratefd")


# add=b()
# add.move()
# add.start()


# multiple_inhertance=it is nothing aquaring properties and methoads  from two patrents claasses to childclass



# class a:
#     def move(self):
#         print("It is added royy")

# class b:
#     def strat(self):
#         print("it is known as it")

# class child(a,b):
#     def wild(self):
#         print("itbis animated")

# dash=child()
# dash.move()
# dash.strat()
# dash.wild()


# mutlilevel means a chain where cild inherits from parents and another child inhertots from that child


# class vechile:
#     def move(self):
#         print("It is value")

# class car(vechile):
#     def strat(self):
#         print("The value is loaded")

# class auto(car):
#     def road(self):
#         print("The value is noted")

# anni=auto()
# anni.move()
# anni.strat()
# anni.road()


# class a:
#     def ant(self):
#         print("mame of the cild")

# class b(a):
#     def ant1(self):
#         print("it is noted as it ")

# class c(a):
#     def ant2(self):
#         print("it is noted as it 1111111")
# class d(a):
#     def ant4(self):
#         print("it is noted as it22222222222222 e")


# nano=d()
# nano1=c()
# nano2=b()


# nano.ant()
# nano1.ant()

# class Vechile:
#     def __init__(self,brand):
#         self.brand=brand

#     def move(self):
#         print("it is moving")
# class car(Vechile):
#     def __init__(self, brand,color):
#         super().__init__(brand)
#         self.color=color

        


# class Point:
#     def __init__(self, x):
#         self.x = x

#     def __add__(self, other):
#         return self.x + other.x

# p1 = Point(10)
# p2 = Point(20)
# print(p1 + p2) 

# import threading
# import time

# def task(name):
#     for i in range(3):
#         print(f"{name} is running")
#         time.sleep(1)

# t1 = threading.Thread(target=task, args=("Thread 1",))
# t2 = threading.Thread(target=task, args=("Thread 2",))

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# # print("Both threads finished execution")

# import threading
# import time

# def spam(name ):
#     for i in range(1,3):
#         print(f" running...............{name}")
#         # time.sleep(1)
# t1=threading.Thread(target=spam,args=("Thread 1",))
# t2=threading.Thread(target=spam,args=("Thread 2",))

# t1.start()
# t2.start()
# t1.join()
# t2.join()



# class student:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age

#     def __str__(self):
#         return f"student name:{self.name},age:{self.age}"
    
# s=student("lukhman",22)
# print(s)


# class student:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age

#     def __repr__(self):
#         return f"student name:{self.name},age:{self.age}"
    
# s=student("lukhman",22)
# print(repr(s))


# class student:
#     def __init__(self,name):
#         self.name=name 


#     def __len__(self):
#         return len(self.name)
    
# c=student("lukhmanshaik")
# # for i in c:
# print(len(c))



# class a:
#         print("Subjects: ",a)                                        
    
# b=a()
# b.add(age1=1,age2=2,age3=3,age4=4,age5=5,age6=6,age7=7)

# class a:
#         def start(self):
#                 print("I m lukhmsn")

# class b(a):
#         def king(self):
#                 print("I am shaik")

# obj1=b()
# obj1.start()



# Create a class Student with attributes name, age, and marks. Write a method display to print all the student details. Create 2 objects of Student and call the display method for each.

# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def get_details(self):
#         print(f"student name is {self.name} age is {self.age} and marks are {self.marks}.")
# obj1=student("lukhman",22,99)
# obj2=student("king",55,254)
# obj1.get_details()
# obj2.get_details()

# import numpy as np

# array1=[12,3,4,54,5,56,6,6,7,7,78]

# print(np.sum(array1))
# print(np.mean(array1))
# print(np.max(array1))



