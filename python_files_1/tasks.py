#Problems based on conditional statements: 
#Even or odd 
# def Even_or_Odd(n) :
#     if n % 2 == 0 :
#         print(f"The Given number {n} is Even")
#     else:
#         print(f"The Given number {n} is Odd") 
#     if n > 0 :
#         print("Positive Number")
#     elif n < 0 :
#         print("Negative Number")
#     else : 
#         print("Zero ")
# n = int(input("Enter Value : "))
# Even_or_Odd(n) 

# Age group classifier:
#def agegroup(age):
#     if 0 < age <= 12:
#         print("Kid")
#     elif 13 < age <= 19:
#         print("Teenage")
#     elif 20 < age <= 40:
#         print("Young")
#     elif 41 < age <= 59:
#         print("Prime")
#     else : 
#         print("senior")
#age = int(input("Enter Age : "))
#agegroup(age)

# Grade Evaluator: 
# def grade(avg) :
#     if avg >= 90:
#         print("A")
#     elif 80 < avg <= 89:
#         print("B")
#     elif 70 < avg <= 80:
#         print("C")
#     elif 60 < avg <= 70:
#         print("D")
#     else : 
#         print("F")
# s1,s2,s3,s4,s5,s6 = map(int,input("Enter Marks : ").split())
# avg = (s1+s2+s3+s4+s5+s6)/6
# print(avg)
# grade(avg)

# Triangle type checker:
# def triangle(a,b,c):
#     if (a + b > c) and (b + c > a) and (c + a > b):
#         print("The sides can form a triangle")
#         if a == b == c :
#             print("It is an Equilateral triangle")
#         elif a == b or b == c or c == a:
#             print("It is an Isosceles triangle.")
#         else:
#             print("It is a Scalene triangle.")
#     else:
#         print("The given sides can make a triangle.")
# a,b,c = map(int,input("Enter 3 side values").split())
# triangle(a,b,c)

# ATM Withdrawal simulator: 
# def withdraw_from_atm(amount,balance):
#     if balance < amount :
#         print("Insufficient balance")
#     elif amount % 100 != 0 :
#         print("The amonut must be divisible by 100")
#     else :
#         v =  (balance -amount )
#         print(f"Withdrawal successful. Current balance is ₹{v}") 
# amount,balance = map(int,input("Enter amount & balance to withdraw: ").split())
# withdraw_from_atm(amount,balance)

# Problems based on functions:
# def greet():
#     print("Nasmte Boss")
# greet()


# def add(a,b):
#     return a + b 
# def sub(a,b):
#     return a - b
# def mux(a,b):
#     return a * b
# def div(a,b):
#     return a/b

# a,b = map(int,input("Enter Two values : ").split())
# operation = input("select any Operand : + , - , * , / : ")

# if operation == '+':
#     result = add(a, b)
# elif operation == '-':
#     result = sub(a, b)
# elif operation == "*":
#     result = mux(a, b)
# elif operation == '/':
#     result = div(a, b)
# else:
#     result = "Invalid operation"

# print("result",result)/

# def wishing_student(name , program ) :
#     wishing =  len(name) and len(program)
#     if wishing :
#         print(f"Welcome {name}, Hope you do good in your {program}")   
#     else :
#         print(f"Welcome Student, Hope you do good in your Engineering program.")
    
# name = input("Enter Name  : ")
# program = input("Enter program  : ")
# wishing_student(name, program)

# def age_after10years(name , age ) :
#     age+=10
#     print(f"Hi i'm {name} , my age  is {age}")   
# name = input("Enter Name  : ")
# age = int(input("Enter program  : "))
# age_after10years(name, age)

# def age_after10years(name , age ) :
#     age+=10
#     print(f"Hi i'm {name} , my age  is {age}")   
# name = input("Enter Name  : ")
# age = int(input("Enter program  : "))
# age_after10years(name, age)

# def display(*details):
#     print(f"My name is {name} , and i'm {age} old!") 
#     print(f"My phone number is {number} and email id {email}")
#     print(f"my Blood group is {blood}")
# name ,email ,blood = map(str,input("enter (seperate by comma)").split())
# age , number = map(int,input().split())
# display(name,age,number,email ,blood)