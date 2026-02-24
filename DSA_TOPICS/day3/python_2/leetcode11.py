# class Person:
#     name="---Lukhman"
#     age=25
#     gender="Male"
# # obj1=Person()
# # obj2=Person()
# # # print(obj1)
# # # print(obj2)
# # print(obj1.name)
# # print(obj2.name)

# # obj1.name="Kiran Kumar"
# # print(obj1.name)
# # print(obj2.name)

# print(Person.name)



# class Person:
#     def __init__(self,name,gender,age):
#         self.name=name 
#         self.gender=gender
#         self.age=age
# obj1=Person("Lukhman","male",23)
# obj2=Person("King","mlae",30)
# print(obj1.name)
# print(obj2.age)

# class SocialMedia:
#     def __init__(self,apps,color,uses):
#         self.apps=apps
#         self.color=color
#         self.uses=uses
#     def purpose(self,app_name,purpose):
#         print(f"{app_name} this is used for {purpose}")
# obj1=SocialMedia("Instagram","red","Watching reels")
# obj2=SocialMedia("FACEbook","blue","Waching videos")
# obj3=SocialMedia("Youtube","Red","Broswing videos")
# obj4=SocialMedia("whatsapp","Green","Messgening")

# obj1.purpose("Instagram","Social media")
# obj2.purpose("youtube","entertainment")
# # obj3.purpose("")

# obj1=SocialMedia("Instagram","red","Watching reels")
# obj2=SocialMedia("FACEbook","blue","Waching videos")
# obj3=SocialMedia("Youtube","Red","Broswing videos")
# obj4=SocialMedia("whatsapp","Green","Messgening")
# print(obj1.apps,obj1.color,obj1.uses)
# print(obj2.apps,obj2.color,obj2.uses)
# print(obj3.apps,obj3.color,obj3.uses)
# print(obj4.apps,obj4.color,obj4.uses)


# def prime_list(n):
#     list1=[]
#     count=0
#     while count<5:
#         # n=int(input())
#         is_prime=True
#         if n<=1:
#             print("Enter number gretaer than 1")
#         for i in range(2,n):
#             if n%i==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             list1.append(n)
#             count+=1
#         n=n+1
#     print(list1)
# prime_list(1)


# def prime_number(num):
#     count=0
#     list1=[]
#     while count<5:
#         is_prime=True
#         if num<=1:
#             print("Numner greater than 1")
#         for i in range(2,num):
#             if num%i==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             list1.append(num)
#             count+=1
#         num+=1
#     print(list1)
# num=int(input("enter the starting number: "))
# prime_number(num)

# booble sort



# nums=[5,3,8,6,7,2]
# # b=sorted(nums)
# # print(b)

# for i in range(len(nums)-1,0,-1):
#     for j in range(i):
#         # print(nums[j],nums[j+1])
#         # print(i,j)
#         if nums[j]>nums[j+1]:
#             # print(nums[j],nums[j+1])

#             nums[j],nums[j+1]=nums[j+1],nums[j]
# print(nums)

# nums=[5,3,8,6,7,2]
# for i in range(len(nums)):
#     minpostion=i 
#     for j in range(i,len(nums)):
#         if nums[j]<nums[minpostion]:
#             minpostion=j
#     nums[i],nums[minpostion]=nums[minpostion],nums[i]
#     print(nums)



# str1="153 21 79 232"
# # print(len(str1))
# a=[]
# b=""
# for i in range(len(str1)):

#     if str1[i]!=" ":
#         b+=str1[i]
    
#     else:
#         b=""
#     # a.append(b)
# a.append(b)
# print(a)


# str1="153 21 79 232"
# a=str1.split(" ")
# list1=[]
# for i in a:
#     l=list(i)
#     x=[int(x) for x in l]
#     x.sort()
#     sum_str=0
#     for j in x:
#         sum_str=sum_str*10+j
#     list1.append(sum_str)
# # for i in list1:
# print(list1)

# str1=153
# for i in range(3):
#     for j in range(3):
#         if int(str1[j])>int(str1[j+1]):

#             str1[j],str1[j+1]=str1[j+1],str1[j]
# print(str1)

    


# a="1983"
# b=list(a)
# b.sort()
# print(b)


# str1="153 21 79 232"
# a=str1.split(" ")
# list1=[]
# for i in a:
#     l=list(i)
#     # x=[int(x) for x in l]
#     l.sort()
#     sum_str=0
#     for j in l:
#         sum_str=sum_str*10+j
#     list1.append(sum_str)
# # for i in list1:
# print(list1)





# str1="beautiful"
# S=""
# for i in str1:
#     # if i not in ["a","e","i","o","u","A","E","I","O","U"]:
#     if i not in "AEIOUaeiou":
#         S=S+i
# print(S)


# s="beatuful"
# volwesl=set("aeiouAEIOU")
# s=''.join(i for i in s if i not in volwesl)
# print(s)



# Perfect, Lukhman! Here are 10 string manipulation problems, starting from basic to intermediate, similar to what you’ve been practicing — like sorting digits, reversing, filtering characters, etc.


# ---

# 🔤 String Manipulation Practice Problems


# ---

# 1. Remove vowels from a string

# 📌 Input: "beautiful"
# 📌 Output: "btfl"

# s="beatuful"
# volwesl=set("aeiouAEIOU")
# s=''.join(i for i in s if i not in volwesl)
# print(s)

# ---

# 2. Reverse each word in a sentence

# 📌 Input: "hello world"
# 📌 Output: "olleh dlrow"

# s="hello world"
# st=s.split(" ")
# print(st)
# a=[]
# for i in st:
#     d=""
#     for j in i:

#         d=j+d  
#     a.append(d)  
# print(a)
# for i in a:
#     print(i,end=" ")
#     print(type(i))


# s="hello world"
# st=s.split()
# se=""
# ab=[]
# for i in st:
#     a=i[::-1]
#     ab.append(a)
#     k=' '.join(ab)
# print(type(k),k)




# s="hello world"
# st=s.split()
# # se=""
# ab=[]
# for i in st:
#     se=""
#     for j in i:
#         se=j+se
#     ab.append()
#     k=' '.join(ab)
# print(type(k),k)

    

# print(' '.join(a))
# print(type(a))


# s="king"
# a=""
# for i in s:
#     a=i+a
# print(a)
# ---

# 3. Sort characters in each word

# 📌 Input: "cat dog"
# 📌 Output: "act dgo"

# s="cat dog"
# cd="az"
# cd1="ba"
# if cd<cd1:
#     print("true")

# s="zxyba"
# li=''.join(sorted(list(s)))
# print(li)

# staa="cat dog"
# s=staa.split()
# abc=[]
# for k in range(len(s)):
#     li=list(s[k])
#     n=len(li)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if li[j]>li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
#     abc.append(''.join(li))
# print(' '.join(abc))



# ---

# 4. Check if a string is a palindrome (ignore spaces)

# 📌 Input: "nurses run"
# 📌 Output: True

# a="nurses run"
# ab=""
# abc=a.split()
# print(''.join(abc))


# a="madama"
# s=""
# for i in a:
#     if i!=" ":
#         s+=i
# is_valid=False
# for i in range(len(s)):
#     l=i
#     r=len(s)-i-1
#     if s[l]==s[r]:
#         is_valid=True
#         # print("it is palindrom")
# if is_valid:
#         print("it is palindrom")
# else:
#     print("it is  not a palindrom")
#         # print("it is not a paloindrom")




# a="madama"
# s=""
# for i in a:
#     if i!=" ":
#         s+=i
# is_valid=True
# for i in range(len(s)):
#     l=i
#     r=len(s)-i-1
#     if s[l]!=s[r]:
#         is_valid=False
#         # print("it is palindrom")
# if is_valid:
#         print("it is palindrom")
# else:
#     print("it is  not a palindrom")
#         # print("it is not a paloindrom")


# ---

# 5. Count frequency of each character (ignore space)

# 📌 Input: "apple pie"
# 📌 Output: {'a':1, 'p':3, 'l':1, 'e':2, 'i':1}

# data1="apple pie"
# data=''.join(data1.split())
# # print(data)
# dicti={}
# for i in data:
#     # print(i)
#     if i not in dicti:
#         dicti[i]=1
#     else:
#         dicti[i]+=1
# print(dicti)



# data1="apple pie"
# data=''.join(data1.split())
# # print(data)
# dicti={}
# for i in data:
#     # print(i)
#     if i in dicti:
#         dicti[i]+=1
#     else:
#         dicti[i]=1
# print(dicti)

# ---

# 6. Remove duplicate characters

# 📌 Input: "banana"
# 📌 Output: "ban"

# s="banana"
# str=""
# for i in s:
#     if i not in str:
#         str+=i
# print(str)

# s="banana"
# b=set(s)
# print(b)
    


# ---

# 7. Find the most frequent character

# 📌 Input: "success"
# 📌 Output: 's'

# string="successccceeee"
# c={}
# for i in string:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1

# max_val=0
# for i in c:
#     if c[i]>=max_val:
#         max_val=c[i]
#         max_ch=i
# print(max_ch,max_val)






# ---

# 8. Sort digits within each number in a space-separated string

# 📌 Input: "321 45 9"
# 📌 Output: "123 45 9"

# str="321 45 9"
# b=str.split()
# ab=[]
# for i in b:
#     li=list(i)
#     li.sort()
#     sum=0
#     for j in li:
#         sum=sum*10+int(j)
#     ab.append(sum)
# print(sorted(ab))

    # a=''.join(li)
    # ab.append(a)
# print(ab)


# ---

# 9. Remove all non-alphabet characters

# 📌 Input: "Hello@123 World!"
# 📌 Output: "HelloWorld"

# s="12abcd"
# for i in range(len(s)):
#     if s[i] not in ord(64)> s[i] <ord(133):
#         print(i)

# ---

# 10. Replace consecutive duplicates with one

# 📌 Input: "aaabbccccd"
# 📌 Output: "abcd"


# s="aaabbccccd"
# a=""
# for i in s:
#     if i not in a:
#         a+=i
# print(a)

# ---

# Would you like solutions for any of these? Or should I give you a custom coding assignment based on these for practice?