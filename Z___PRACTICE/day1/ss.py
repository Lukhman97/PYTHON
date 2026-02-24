# int x=10
# print(type(x))



# a=list(map(int,input("Enter numbers: ").split()))
# print(a)

# a=0
# b=20
# print(not a)


# a class is a blueprint for creating objects.it defines the function and varaiables.
# class Car:
#     def start(self):
#         print("Car has being started")
# obj1=Car()
# obj1.start() 

# class student:
#     def __init__(self,name):
#         self.name=name
# s1=student("Lukhman")
# print(s1.name)

# class student:
#     college="ABC Juniour"
#     def __init__(self,name):
#         self.name=name
# s1=student("Lukhman")
# s2=student("Ali")
# print(s1.name,s1.college)
# print(s2.name,s2.college)


# def prime_numbers(num):
#     # is_prime=True
#     if num==0 or num==1:
#        return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(prime_numbers(7))

# prime_01=[i for i in range(1,100) if prime_numbers(i)]
# print(prime_01)


# class Car:
#     def __init__(self,name):
#         self.name=name
#     def start(self):
#         print(f"Car has be started its name is {self.name}")
# obj1=Car("suzukii")
# obj1.start()

# with open("texr.txt",'r')as f:
#     file=f.read()


# import sys

# a = [1, 2, 3]
# print(sys.getrefcount(a))  # shows reference count


# a=[1,2,3,4,5]
# for i,j in enumerate(a):
#     print(i,j)

nums = [1, 2, 3]

# pr/int(nums.all(2))

# def numbers(nums):
#     for i in nums:
#         yield i
#     # yield 2
#     # yield 3

# print(numbers( [1, 2, 3]))

# print(next(gen))
# print(next(gen))
# print(next(gen))

