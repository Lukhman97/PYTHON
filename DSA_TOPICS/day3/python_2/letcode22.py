# nums=[5,3,7,6,2]
# for i in range(len(nums)):
#     minpos=i
#     for j in range(i+1,len(nums)):
#         if nums[j]<nums[minpos]:
#             minpos=j
#     nums[i],nums[minpos]=nums[minpos],nums[i]
# print(nums)
        
        # if nums[i]>nums[minpos]



# n=6
# li=[]
# for i in range(n):
#     n=int(input("Enter the number in list: "))
#     li.append(n)
# print(li)


# li=list(map(int,input().split()))
# n=len(li)
# for i in range(n):
#     min_pos=i
#     for j in range(i+1,n):
#         if li[j]<li[min_pos]:
#             min_pos=j
#     li[i],li[min_pos]=li[min_pos],li[i]
# print(li)
        


# arr = [2, 4, 6, 8, 10, 12, 14]
# target = 7 #1,
# l=0
# h=len(arr)-1
# is_true=False
# while l<=h:
#     mid=(l+h)//2
#     if arr[mid]==target:
#         print("it is found")
#         print(mid)
#         is_true=True
#         break
#     elif arr[mid]<target:
#         l=mid+1
#     else:
#         h=mid-1
# if not is_true:
#     print("number not found")


# str="153 21 97 542"
# str1=str.split()
# ab=[]
# list1=[]
# for i in str1:
#     li=list(i)
#     ab.append(sorted(li))
# for i in ab:
#     list1.append(''.join(i))
    

# print(list1)


# li1="15329922"
# li=list(li1)
# for i in range(len(li)):
#     for j in range(len(li)-1):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
# print(''.join(li))


# words = ["listen", "silent", "enlist", "rat", "tar", "art", "cat", "tac"]
# anagram_groups = {}

# for word in words:
#     key = ''.join(sorted(word))  # Use sorted characters as key
#     if key in anagram_groups:
#         anagram_groups[key].append(word)
#     else:
#         anagram_groups[key] = [word]

# # Final result
# result = list(anagram_groups.values())
# print(result) 


# class Bank_account:
#     def __init__(account,name,id,ph,balance):
#         account.name=name
#         account.id=id
#         account.ph=ph
#         account.balance=balance
#     def deposit(account,d_amount):
#         account.balance+=d_amount
#     def withdraw(account,w_amount):
#         account.balance-=w_amount
#     def check_balance(account):
#         print(account.balance)
# lukhman_account=Bank_account("Lukhman","lukhman@gmail.com",8247256969,12000)
# lukhman_account.check_balance()
# lukhman_account.withdraw(2990)
# lukhman_account.check_balance()
# lukhman_account.deposit(11111)
# lukhman_account.check_balance()


# class Parent:
#     def Pmethod(self):
#         print(" i am from parent class")
#     def Pmethod2(self):
#         print("I am a second method from class")

# class Child(Parent):
#     def Cmethod(self):
#         print("i am from child class")
#         super().Pmethod2
#         super().Pmethod2
# obj1=Child()
# # obj1=Parent()
# obj1.Pmethod()
# # obj1.Cmethod()
# obj1.Pmethod2()
# obj1.Cmethod()


# class parent:
#         class child:
#                 class hai:
#                         def __init__(self):
#                                 print("what a kai")
# obj1=parent()
# print(obj1)




# class user:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
# class student(user):
#     def __init__(self,name,email,emailed_courses):
#         super().__init__(name,email)
#         self.emailed_courses=emailed_courses
#     def getCourses(self):
#         print(f"{self.name} is learning {self.emailed_courses}")

# class instructor(user):
#     def __init__(self,name,email,courses_trained):
#         super().__init__(name,email)
#         self.courses_trained=courses_trained
#     def getCourses(self):
#         print(f"{self.name} is teachingg {self.courses_trained}")


# student_obj=student("Lukhman","lukhman@gmail.com",["html","css","js"])
# student_obj.getCourses()
# student_obj1=student("LOKESH","lokesh123@gmail.com",["html","css","js"])
# student_obj1.getCourses()
# trainer_obj=instructor("Harish","harish123#gmail.com",["frontend","backend","html","css"])
# trainer_obj.getCourses()





# class user:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
# class student(user):
#     def __init__(self,name,email,emailed_courses):
#         super().__init__(name,email)
#         self.emailed_courses=emailed_courses
#     def getCourses(self):
#         print(f"{self.name} is learning {self.emailed_courses}")
#     def remove_course(self,course):
#         # self.course=course
#         self.emailed_courses.remove(course)
#         self.getCourses()
#     def add_course(self,course):
#         self.emailed_courses.append(course)


# class instructor(user):
#     def __init__(self,name,email,courses_trained):
#         super().__init__(name,email)
#         self.courses_trained=courses_trained
#     def getCourses(self):
#         print(f"{self.name} is teachingg {self.courses_trained}")


# student_obj=student("Lukhman","lukhman@gmail.com",["html","css","js"])
# student_obj.getCourses()
# # student_obj1=student("LOKESH","lokesh123@gmail.com",["html","css","js"])
# # student_obj1.getCourses()
# # trainer_obj=instructor("Harish","harish123#gmail.com",["frontend","backend","html","css"])
# # trainer_obj.getCourses()

# student_obj.remove_course("html")
# student_obj.add_course("javascript")
# student_obj.add_course("power BI")
# student_obj.getCourses()



# class Parent1:
#     def P1method(self):
#         print("I am method from parent1")
# class Parent2:
#     def P2method(self):
#         print("I am method from parent2")
# class child(Parent1,Parent2):
#     def Cmethod(self):
#         super().P1method()
#         super().P2method()
#         print("i am method from child")

# obj1=child()
# # obj1.P1method()
# # obj1.Cmethod()
# obj1.Cmethod()

    
    

        
        




