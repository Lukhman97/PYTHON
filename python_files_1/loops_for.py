
# # 1. Check Even or Odd
# # Question: Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number 

# def even_or_odd(n):
#     if n>0:
#         if n&1==0:
#             print(f"The number {n} is even and positive")
#         else:
#             print(f"The number {n} is odd and positive")
#     elif n<0:
#         if n&1==0:
#             print(f"The number {n} is even and negitive")
#         else:
#             print(f"The number {n} is odd and negitive")
#     else:
#         print("Ente the valid number!!!!!!")
# n=int(input("Enter the number: "))
# even_or_odd(n)


# # 2. Divisible by 5 but Not by 10
# # Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy

# def divisible_by(n):
#     if n%5==0 and n%10!=0:
#         print(f"The number {n} is divisible by 5 and not divisible by 10")
#     elif n%5==0 and n%10==0:
#         print(f"The number {n} is divisible by 5  and 10")
#     elif n%5==0:
#         print(f"The number {n} is divisible by only 5 ")
#     elif n%10==0:
#         print(f"The number {n} is divisible by only 10 ")
#     else:
#         print(f"The number {n} is not disible by 5 and 10")
# n=int(input("Enter the number: "))
# divisible_by(n)


# # 3. Biggest Among Two Numbers
# # Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7

# def biggest_num(a,b):
#     if a==b:
#         print(f"All the numbers  {a},{b}are equal")
#     elif a>b :
#         print(f" {a} is greater")
#     elif b>a :
#         print(f"{b} is greater")
#     else:
#         print("enter a valid number!!!")

# a=int(input("Enter the  first number: "))
# b=int(input("Enter the second number: "))
# biggest_num(a,b)





# # 4. Smallest Among Two Numbers
# # Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4


# def biggest_num(a,b):
#     if a==b:
#         print(f"All the numbers  {a},{b}are equal")
#     elif a<b :
#         print(f" {a} is small")
#     elif b<a :
#         print(f"{b} is small")
#     else:
#         print("enter a valid number!!!")
# a=int(input("Enter the  first number: "))
# b=int(input("Enter the second number: "))
# biggest_num(a,b)




# # 5. Divisible by 2, 3, and 6
# # Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy


# def divisible(n):
#     if n%2==0 and n%3==0:
#         print("The number is divisible by 2,3 and 6")
#     elif n%2==0:
#         print(" The number is divisible by 2")
#     elif n%3==0:
#         print("The number is divisible by 3")
#     else: 
#         print("The number is not divisible by anything")

# n=int(input("Enter the number: "))
# divisible(n)


# # 6. Voting Eligibility
# # Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote


# def voting(age):
#     if age>=18:
#         print("You are elligible to vote")
#     else:
#         print("You are not elligible to vote")
# age=int(input("Enter the number: "))
# voting(age)


# # 7. Student Pass/Fail Based on All Subjects >= 35
# # Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail

# def pass_or_fail(math,phy,chem):
#     if math>=35 and phy>=35 and chem>=35:
#         print("You are PASS")
#     else:
#         print("You are Fail")
# math,phy,chem=map(int,input("Enter the marks of three subjects: ").split())
# pass_or_fail(math,phy,chem)



# # 8. Student Pass if Passed Any One Subject (>= 35)
# # Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass


# def pass_or_fail(math,phy,chem):
#     if math>=35 or phy>=35 or chem>=35:
#         print("You are PASS")
#     else:
#         print("You are Fail")
# math,phy,chem=map(int,input("Enter the marks of three subjects: ").split())
# pass_or_fail(math,phy,chem)



# # 9. Student Pass if Passed Any Two Subjects
# # Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass

# def pass_or_fail(math,phy,chem):
#     if (math>=35 and phy>=35) or (phy>=35 and chem>=35) or (chem>=35 and math>=35):
#         print("You are PASS")
#     else:
#         print("You are Fail")
# math,phy,chem=map(int,input("Enter the marks of three subjects: ").split())
# pass_or_fail(math,phy,chem)



# # 10. Biggest Among Three Numbers
# # Question: Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9

# def biggest(a,b,c):
#     if a==b==c: 
#         print("All are equal")
#     elif a>b and a>c:
#         print(f"{a} is biggest")
#     elif b>c:
#         print(f"{b} is biggest")
#     else:
#         print(f"{c} is bigest number")
# a,b,c=map(int,input("Enter the three numbers: ").split())
# biggest(a,b,c)


# # 11. Smallest Among Three Numbers
# # Question: Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4
# def biggest(a,b,c):
#     if a==b==c: 
#         print("All are equal")
#     elif a<b and a<c:
#         print(f"{a} is smallest")
#     elif b<c:
#         print(f"{b} is smallest")
#     else:
#         print(f"{c} is smallest number")
# a,b,c=map(int,input("Enter the three numbers: ").split())
# biggest(a,b,c)


# # 12. Perfect Square or Not
# # Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number. - Input: Number = 49 - Output: Perfect square

# def square(num):
#     for i in range(num):
#         b=i**2
#         if num==b:
#             print(f"{num} is perfect square")
#             return 
#     print(f"{num} is  not a square perfect square")  #dount with ifelse 
# num=int(input("Enter the number: "))
# square(num)

# # ________________________________________
# # 13. Cars Required for Members (Max 5 per car)
# # Question: Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4


# import math
# def car_r(num):
#     # print((num+(num%6))//5)
#     print(math.ceil(num/5))
#     print((num+4)//5)
#     # print((num+(num%5)//5)+1)
# num=int(input("Enter the number: "))
# car_r(num)




# # 14. Second Biggest Among Three Numbers
# # Question: Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18


# def numbers(a,b,c):
#     list=[a,b,c]
    
#     b=sorted(list)
#     print(b[-2])
# a,b,c=map(int,input("ENter the numbers: ").split())
# numbers(a,b,c)


    



# # 15. Leap Year or Not
# # Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year


# def numer(num):
#     if (num%4==0) and (num%100!=0) or (num%400==0):
#         print("Leap Year")
#     else:
#         print("non leap year")
# num=int(input("Enter the number: "))
# numer(num)



