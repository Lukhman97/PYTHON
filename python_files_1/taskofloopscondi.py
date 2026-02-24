# # Conditional statements:
# # 1. Check Even or Odd
# # Input a number and print whether it's even or odd.


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


# # 2. Age Group Classifier
# # Input age and print:
# # "Child" if age < 13
# # "Teen" if 13 ≤ age < 20
# # "Adult" if age ≥ 20

# def fun(age):
#     if age<13:
#         print("child")
#     elif age<20:
#         print("Teen")
#     else:
#         print("Adult")
# age=int(input("Enter the number:"))
# fun(age)

# # 3. Check if a given number is positive, negative, or zero.

# def fun(number):
#     if number==0:
#         print("Zero")
#     elif number>0:
#         print("positive")
#     elif number<0:
#         print("Negitive")
# number=int(input("Enter the number: "))
# fun(number)

# # 4. Divisibility Checker
# # Check if a number is divisible by both 3 and 5.
# def divisible(num):
#     if num%3==0 and num%5==0:
#         print(f"{num} is divisible by 3 and 5")
#     elif num%3==0:
#         print(f"{num} is divisible by 3 only")
#     elif num%5==0:
#         print(f"{num} is divisible by 5 only")
#     else:
#         print("Te number is not divisible by 3 and 5")
# num=int(input("Enter the number: "))
# divisible(num)


# # 5. Find Largest of Two Numbers
# # Input two numbers and print the larger one.
# def largest(a,b):
#     if a==b:
#         print("Both are Equal")
#     elif a>b:
#         print(f"{a} is greater")
#     else:
#         print(f"{b} is greater")
# a,b=map(int,input("Enter the numbers: ").split())
# largest(a,b)

# # 6. Triangle Validity Checker
# # Give three sides(eg:s1=15, s2=10, s3=23), check if they can form a triangle (that is, sum of any two sides > third side).

# def triangle(s1,s2,s3):
#     if s1+s2>s3 and s2+s3>s1 and s3+s2>s1:
#         print("It will form the trianglee")
#     else:
#         print("It will not form a triangle")
# triangle(15,10,23)
    



# # for loop with sequential data:
# # 1. Print each character of a string
# # Input: "hello" → Output: h e l l o

# a=input()
# for i in range(len(a)):
#     print(a[i])


# # 2. Sum of first 10 natural numbers
# # Use a for loop with range().

# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)


# # 3. Print even numbers from 1 to 20

# for i in range(1,21):
#     if i&1==0:
#         print(i)
    

# # 4. Print elements in a list
# # List: ["pen", "pencil", "eraser"]

# list1=[]
# n=int(input("Enter the entity: "))
# for i in range(n):
#     a=int(input("enter value: "))
#     list1.append(a)
# for i in list1:
#     print(i)

# # 5. Print common elements in two lists

# list1=[5,6,2,4,7,8]
# list2=[5,6,2,4,7,8]
# for i in range(len(list1)):
#     if list1[i] in list2:
#         print(list1[i])



# # 6. Print all elements in a set
# #     my_set = {"apple", "banana", "cherry"}


# ans=set()
# n=int(input("enter the entity:"))
# for i in range(n):
#     key=input("Enter the key: ")
#     ans.add(key)
# print(ans)
# for i in ans:
#     print(i)



# # 7. Count how many items are in a set using a loop
# #     colors = {"red", "blue", "green", "yellow"}

# my_set=set()
# c=0
# n=int(input("Enter the entity: "))
# for i in range(n):
#     key=input("enter the key: ")
#     my_set.add(key)
#     c+=1
# print(my_set)
# print(c)





# # 8. Print all keys and values in a dictionary
# #    person = {"name": "Alice", "age": 25, "city": "Delhi"}
# dict={}
# n=int(input("Enter the entity: "))
# for i in range(n):
#     key=input("Enter the key: ")
#     value=int(input("Enter the value: "))
#     dict[key]=value
# print(dict)


# # 9. Count how many values in a dictionary are greater than 50
# #      scores = {"math": 45, "english": 55, "science": 80, "history": 40}

# dict={}
# c=0
# n=int(input("Enter the entity: "))
# for i in range(n):
#     key=input("Enter the key: ")
#     value=int(input("Enter the value: "))
#     # dict[key]=value
#     if value>50:
#         # dict[key]=value
#         c+=1
# print(c)

# # 10. Create a new dictionary with only items where the value is even
# #    data = {"a": 1, "b": 4, "c": 6, "d": 3}


# dict={}
# n=int(input("Enter the entity: "))
# for i in range(n):
#     key=input("Enter the key: ")
#     value=int(input("Enter the value: "))
#     # dict[key]=value
#     if value%2==0:
#         dict[key]=value
# print(dict)



# dict={}
# n=int(input("enetr the entity: "))
# for i in range(n):
#     key=input("Enter the key: ")
#     value=int(input("Enter the value: "))
#     dict[key]=value
#     # if value==True:
#         # print(dict)
#         # dict[key]=value

# print(dict)

# def facti(num):
#     # global ans
#     # ans=0
#     for i in range(num):
#         if i==1:
#             print(i)
#         else:
#             if i>=2:
#                 return num*(num-i)
            
# num=int(input("Enter the number: "))
# # facti(num)
# print(facti(num))

num=int(input("Enter number: "))
ans=num
sum=1
while num>0:
    if num==1 and ans==1:
        a=sum
    elif num>=2:
        sum=num*(num-1)*sum

    num=num-2
a=sum
print(sum)