# a=int(input())
# b=int(input())
# add=lambda a,b:a+b
# print(add(int(input()),int(input())))


# add=lambda a:"even nUmber" if a%2==0 else "Odd Number"
# print(add(int(input("Enter tthe number :"))))

# n=int(input())
# print("Even" if n%2==0 else "Odd")

# n=int(input())
# if n&1==0:
#     print("Even")
# else:
#     print("ODD")



# a=int(input())
# b=int(input())
# c=int(input())
# if a==b==c:
#     print(a)
# elif a>b and a>c:
#     print(a)
# elif b>c and b>a:
#     print(b)
# else:
#     print(c)


# n=int(input())
# temp=1
# while n>0:
#     temp=n*temp
#     n=n-1
# print(temp)
    


# def fun(n):
#     if n==0:
#         return 1
#     return n* fun(n-1)
# print(fun(5))

# s="python"
# # a=""
# # for i in s:
# #     a=i+a
# # print(a)
# # a=len(s)-1
# # rev=""
# # while a>=0:
# #     rev+=s[a]
# #     a-=1
# # print(rev)
# b=len(s)-1
# a=""
# while b>=0:
#     a+=s[b]
#     b-=1
# print(a)


# input="education"
# c=0
# for i in input:
#     if i in "aeiou":
#         c+=1
# print(c)


# input="education"
# l=len([i for i in input if i in "aeiouAEIOU"])
# print(l)



# list1=[1, 2, 2, 3, 4, 4, 5]
# list2=[]
# # for i in list1:
# #     if i not in list2:
# #         list2.append(i)
# # print(list2)

# for i in list1:
#     found=False
#     for y in list2:
#         if i==y:
#             found=True
#             break
#     if not found:
#             list2.append(i)
# print(list2)



# num=int(input())
# is_prime=True
# for i in range(2,num):
#     if num%i==0:
#         is_prime=False
#         break
# if is_prime:
#     print("It is a prime")
# else:
#     print("It is not a prime")


# n=int(input())
# a=0
# b=1
# for i in range(n+1):
#     print(a,end=" ")
#     a,b=b,a+b

# n=int(input())
# li=[i*i for i in range(1,n+1) if i%2==0]
# print(li)

# n=[1, 2, 3, 4, 5, 6]
# # li=(filter(lambda x: x%2==0,n))
# # li1=map(lambda i:i*i,li)
# # print(list(li1))

# print(list(map(lambda x:x*x,filter(lambda x:x%2==0,n))))


# def fact(num):
#     if num<=1:
#         return 1
#     return num*fact(num-1)
# print(fact(5))

# with open("Practice_all\data.txt",'r+') as f:
#     a=f.write("I ma lukhman11")
#     # b=a.split(" ")
#     # print(len(b))
#     print(a)

# import time

# start=time.time()
# end=time.time()
# print(f"Executed time: {end-start}seconds")
import time
def my_decorder(func):
    def wrapper():
        strat=time.time()
        print("Before the function is executed..")
        func()
        end=time.time()
        print("After the function is executed....")
        print(f"execupted time is :econds...",(end-strat).total_seconds())
    return wrapper
@my_decorder
def write():
    print("Hello EveryOne")
    # return write

write()