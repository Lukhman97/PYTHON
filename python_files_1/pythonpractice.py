# 1.Even or odd (and) positive and negative: 
# Ask the user for the input a number and: 
# Check if it is even or odd 
# Also check if it’s positive, negative, or zero 

# n=int(input("Enter the number: "))
# if n>0:
#     if n&1==0:
#         print(f"The number {n} is Even and it is positive")
#     else:
#         print(f"The number {n} is odd and it is positive")
# elif n<0:
#     if n&1==0:
#         print(f"The number {n} is Even and it is Negitive")
#     else:
#         print(f"The number {n} is 0dd and it is Negitive")



# 2. Age group classifier:  
# (ask the user to enter their age and classify them into one of the 
# following categories) 
# Kids (0-12) 
# Teenage (13-19) 
# Young (20-40) 
# Prime (41-59) 
# Senior (above 60)

# n=int(input("Enter the age:"))
# if n<=12:
#     print("You are kid")
# elif n<=19:
#     print("You are a teenager")
# elif n<=40:
#     print("you are young")
# elif n<=59:
#     print("you are prime")
# elif n<=100:
#     print("You are seniour")
# else:
#     print("You are pro seniour")



# 3. Grade Evaluator: 
# Calculate average of 6 subjects each subject for maximum 100   
# marks   and give the grade based on the percentage. 
# User should be able to give input of all 6 subjects (each subject out 
# of 100) 
# 90% and above -> A 
# 80%-89% ->B 
# 70%-79% -> C 
# 60%-69% -> D 
# Below 60% -> F


# def fun(avg):
#     if avg>=90:
#         print("You got A grade")
#     elif avg>=80:
#         print("You got b grade")
#     elif avg>=70:
#         print("you got C garde")
#     elif avg>=60:
#         print("You got D Grade")
#     elif avg<60:
#         print("Fail")
#     else:
#         print("INvalid")
# s1,s2,s3,s4,s5,s6=map(float,input("Enter the 6 subjects mark: ").split())
# avg=(s1+s2+s3+s4+s5+s6)//6
# print(avg)

# fun(avg)

# Triangle type checker: 
# Take 3 side lengths as input and check if the triangle is: 
# Equilateral if all three sides same 
# Isosceles if any two sides are equal 
# Scalene if all sides are different 
# Also check whether the given sides form a triangle or not based on 
# triangle inequality rule: 
# The Triangle Inequality Rule states that for any triangle: 
# The sum of the lengths of any two sides must be greater than or 
# equal to the length of the remaining side.  
# If you have a triangle with sides a, b, and c, then a + b > c, b + c > a, 
# and c + a > b.

# def fun(a,b,c):
#     if (a+b>c) and (b+c>a) and (c+a>b):
#         print("It will form a Triangle")
#         if a==b==c:
#             print("It is an Euilateral traingle")
#         elif a==b or b==c or c==a:
#             print("It is an Isoscles")
#         elif a!=b!=c:
#             print("It is an Scalean traingle")
#     else:
#         print("It is not a triangle")
# a,b,c=map(int,input("Enter the numbers: ").split())
# fun(a,b,c)


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


# . Write functions for four basic arithmetic operations(+,-,*,/) one 
# function for each operation. 
# User must be able to give input of which operation he wants to 
# perform 
# User must be able to give input of numeric values on which he 
# wants to perform the arithmetic operation 



# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b 
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# a,b=map(int,input("Enter the numbers: ").split())
# operation=input("enter the operator: ")
# if operation=="+":
#     print(f"ADD the number {a},{b} is ",add(a,b))
# elif operation=="-":
#     print(f"subb the number {a},{b} is",sub(a,b))
# elif operation=="*":
#     print(f"MUL the number {a},{b} is",mul(a,b))
# elif operation=="/":
#     print(f"division the number {a},{b } is ",div(a,b))
# else:
#     print("Enter valid numbers")
   


#  Write a function to wish a student based on his name and the 
# program he chooses to study 
# User must be able to give student name and the program name 
# (Mechanical, Civil, Computer Science, ECE, etc.) 
# If no arguments given, the function must wish student with 
# words ‘Student’ and ‘Engineering’ in place of his name and 
# program. 
# eg: output: 
# Welcome Rajesh, Hope you do good in your Mechanical 
# program 
# or 
# Welcome Student, Hope you do good in your Engineering 
# program.


# def fun(name="student",branch="Engeernering"):
#     print(f" Welcome {name}, Hope you do good in your {branch}  branch ")
# name=input("Enter the name: ")
# branch=input("Enetr the branch: ")
# fun(name,branch)


#  Write a function to print user’s name and age of the user in 
# 2035(after 10 years from now): 
# User must be able to pass his name in the form of string and 
# age in the form of integer to the function 

# def fun(age,name):
#     age+=10
#     print(f"The Person age is {age} and his name is {name}")

# age=int(input("Enetr the age: "))
# name=(input("Enter the name:"))
# fun(age,name)


#  Write a function to display student name, age, phone number, 
# address, email address, and blood group  
# User must be able to pass the details in any order we want while 
# calling the function.  
# eg. the user can give name, age, number, address, email address, 
# blood group or   age, name, email address, address, blood group or 
# in any other order.
#

# def fun(*student_details):
#     print(f"My name is {name} ,age is {age},phone-number is  {phone_number},coming to my address {address},email is {email_address},and  finally comming to blood_group {blood_group}")
# name=input("Enter your name: ")
# age=int(input('Enter your age: '))
# phone_number=int(input('enter your number: '))
# address=input("Enter the address: ")
# email_address=input("Enetr your email: ")
# blood_group=input("Enter your blood group: ")
# fun(name, age, phone_number, address, email_address,blood_group)


# a=True
# print("i am lukhamn") if a else print("I am not lukhman")

# a=3
# b=4
# op=a if a>b else b
# print(op)

# op=lambda:5
# print(op())

# op=lambda:print("Hello World")
# print(op())


# op=lambda:print("Hello World")
# op()

# op=lambda x:x+2
# print(op(5))  #7

# op=lambda x:x*x
# print(op(5))  

# op=lambda x,y:x+y
# print(op(5,7))  #7

# op=lambda x,y:print("x is greater than y") if x>y else print("x is lessthan y")
# op(3,4)

# op=lambda x:print("EVEN") if x%2==0  else print("ODD")
# op(3)


num=int(input())
# digit=num
sum=0
while num>0:
    digit=num%10
    if digit%2==0:
        sum+=digit
    num=num//10
print(sum)


    


