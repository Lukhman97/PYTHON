# list1=[10,'lokesh',9,'kholi',78,'kaleel']
# a=len(list1)
# # for r in range(-1,-1,-1):
# #     print(r,end="")
# print(f"lenghtgh of the fruits is {a}")


#list1=[10,'lokesh',9,'kholi',78,'kaleel']
#for i in range():
#    print(i,end="")
# a = ["hello","vamsi",10,20,True,None]
# c = [ ]
# for i in range(len(a)-1,-1,-1) :
#     c.append(a[i])
# print(c)

# list1=["mango","orange","watermelon","apple"]
# c=[]
# for i in list1:
#     if len(i)>5:
#         c.append(i)
# print(c)


# fruits=["apple","mango","banana"]
# print(fruits[0],fruits[-1])
# print(len(fruits))
# fruits[1]="pineapple"
# print(fruits)


# x=["harish","naresh", "suresh", "Mahesh"]
# print(id(x))
# # for i in x:
# #     print(id(i))
# x[2]="kiran"
# print(x)
# print(id(x))


# data=[1, 2, [4, 5], [6, 7], 8, ["something"]]
# print(data[2][0])
# print(data[3][0])
# print(data[5][0][2])


# mixed=[1,2,'hi',12.5,"True"]


# print(f"Value:{mixed[0]},Type:{type(mixed[0])}")
# print(f"Value:{mixed[2]},Type:{type(mixed[2])}")
# print(f"Value:{mixed[3]},Type:{type(mixed[3])}")


# s="lukhman"
# n=len(s)//2
# m=len(s)*2
# for i in range(n):
#     l=s[i]
#     r=s[-1-i]
#     print(l,r)


# s="hello"
# b=len(s)
# for i in range(b):
#     l=ord(s[i])
#     r=ord(s[i])

# s="hello"
# b=0
# for i in range(len(s)-1):
#     l=ord(s[i])
#     r=ord(s[i+1])
#     a=abs(l-r)
#     b+=a
# print(b)
    
    

# a=["--X","X++","X++"]
# b=0
# for i in range(len(a)):
#     if a[i]=="--X" or a[i]=="X--":
#         b=b-1
#     if a[i]=="X++" or a[i]=="++X":
#         b=b+1
# print(b)


# a="1.1.1.1.1"
# b=""
# for i in a:
#     # b=""
#     if i==".":
#        b+="[.]"
#     else:
#         b+=i 
# print(b)

# jewels="z"
# stones="ZZ"
# ans=0
# for i in range(len(stones)):
#     for j in range(len(jewels)):
#         if jewels[j]==stones[i]:
#             ans+=1
# print(ans)

# li=[6,7,8,10,2]
# ans=0
# for i in range(len(li)):
#     val=li[i]
#     ans=max(ans,val)
# print(ans)
       

# li=[99,88,561,87,666]
# ans=0
# for i in range(len(li)):
#     val=li[i]
#     ans=max(ans,val)
# print(ans)

# sentence=["alice and bob love leetcode","i think so too","these is great thanks very much"]
# ans=[]
# b=0
# a=0
# for i in range(len(sentence)):
#     for j in range(len(sentence[i])):
#         if sentence[j]==" ":
#             a+=1
#             ans.append(a)
# print(ans)
# # for i in range(len(ans)):
# #     b=max(ans[i],b)
# # print(b)


# li=["alice and bob love leetcode","i think so too","these is great thanks very much"]
# for i in range(len(li)):
#     s=li[i]
#     temp=1
#     ans=0
#     for j in range(len(s)):
#         ch=s[j]
#         if ch==" ":
#             temp+=1
# ans=max(temp,ans)
# print(ans)
# tickets=1
# if tickets:
#     print("Tickets are available")
# else:
#     print("Tickets are not available")



# age=int(input("Enter your age:"))
# if age>=18:
#     print("You are elligible to vote ")
# else:
#     print("You are not elligible to vote")


# enter_number=int(input("Enter the number: "))
# if enter_number%2==0:
#     print(f"{enter_number} is EVEN")
# else:
#     print(f"{enter_number} is ODD")

# num=7659
# print(num%10)
# print