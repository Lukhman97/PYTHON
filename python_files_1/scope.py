# # scopeee
# # it defines the life of the varaible there are three types
# # 1.global
# # 2.local
# # 3.enclosed   

# # x=10
# # def fun1():
# #     print(x)   -----> global
# # fun1()

# # def fun():
# #     x=10
# #     print("hello")  -- > local

# # fun()
# # print(x)


# # def fun():
# #     x=7
# #     print(x)
# #     def fun2():
# #         x= 10              ----------->embended
# #     fun2()
# # fun()


# x=10
# def show():
#     x=5
#     print(x)
# show()
# print(x)


# def outer():
#     x=20
#     print(x)
#     def inner():
#         print(x)
#     inner()
# outer()

# x="global"
# def outer():
#     x="outer"
#     def inner():
#         x="inner"
#     inner()
#     print("outer",x)
# outer()
# print("inner",x)


# # count = 0

# # def increment():
# #     # global count
# #     count += 1
# #     print(count)
# # increment()
# # print("Count:", count)

# # def outer():
# #     x = 'outer variable'
    
# #     def inner():
# #         print("Accessing from inner:", x)
    
# #     inner()

# # outer()

# # def outer():
# #     x = 'outer variable'
    
# #     def inner():
# #         global x
# #         x=22
# # #         print("Accessing from inner:", x)
    
# #     inner()

# # outer()
# # print("Accessing from inner:", x)


# # def outer():
# #     message = "Hello"

# #     def inner():
# #         global message
# #         message = "Hi"
# #         print("Inner:", message)

# #     inner()
# #     print("Outer:", message)
# # # print("Outer:", message)
# # outer()
# # print("Outer2:", message)



# # count = 0

# # def greet():
# #     global count
# #     count += 1
# #     print("Hello!", "Called", count, "times")

# # greet()
# # greet()
# # greet()

# # n1=0
# # def factorial(n):
    
# #     n1=0
# #     if n==0:
# #         return 1
# #     n1= n * factorial(n-1)
# # n=int(input("enter the number: "))
# # # print(n)
# # # factorial(n)
# # print(n1)
# # # print(factorial(3))


# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     return n * factorial(n - 1)

# # print("Factorial of 5:", factorial(5))


# # for i in range(1,11):
# #     print(f"2 X {i}=",2*i)

# # def fun(n):
# #     for i in range(1,11):
# #         print(f"{n} X {i}=",n*i)
# # n=int(input("Enter the number: "))
# # fun(n)



# # def fun(n):
# #     for i in range(1,11):
# #         print(f"{n} X {i}={n*i}")
# # n=int(input("Enter the number: "))
# # fun(n)

# # x=int(input())
# # for i in range(1,11):
# #     print(i*i)


# # for i in range(1,11):
# #     if i%2==0:
# #         print(i*i)
# #     else:
# #         print("-------",i*i*i)



# # n=int(input())
# # for i in range(1,21):
# #     if i%2==0 and i%3==0: 
# #         print("Non-fizzbuss----",i)
# #     elif i%3==0:
# #         print("buzz---",i)
# #     elif i%2==0 :
# #         print("fizz----",i)
# #     else:
# #         print("----",i)




# sum=0
# for i in range(1,11):
#     sum+=i
# print("sum of first 10 numbers:",sum)


# sum=0
# for i in range(1,11):
#     a=i**2
#     sum+=a
# print("sum of first 10 squares:",sum)

# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 print(i,j)
# nums=list(map(int,input().split()))
# target=int(input())
# two_sum(nums,target)





# s=0
# print(*range(11,21))

# list=['hi',"hello","python",'is',"our","class","today"]
# for i in range(1,len(list)-1):
#     print(list[i])