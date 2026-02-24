# n=6
# for i in range(n):
#     row=""
#     for j in range(i):
#         row+="*"
#     print(row)

# n=6
# a=0
# for i in range(n):
#     row=""
#     for j in range(i):
#         row+=str(a)
#     print(row)
#     a+=1
# print()



# s="lukhman"
# for i in range(len(s)+1):
#     raw=""
#     for j in range(i):
#         raw=raw+s[j]
#     print(raw)


# s="lukhman"
# for i in range(len(s)):
#     raw=""
#     for j in range(i+1):
#         raw=raw+s[i]
#     print(raw)


# s="lukhman"
# for i in range(len(s)-1,-1,-1):
#     raw=""
#     for j in range(i+1):
#         raw=raw+s[j]
#     print(raw)


# # ------------------------------------


# s="lukhman"
# for i in range(len(s)): #0
#     st=""  # 
#     for j in range(i+1):#0
#         st+=s[j]   #l,
#     print(st)


# a=1
# for i in range(3):
#     st=""
#     for j in range(3):
#         st+=str(a)
#         a+=1
#         # print(a,end="")
#     print(st)
    
#     # print()

# n=4
# a=4
# for i in range(n):
#     row=""
#     colo=""
#     for j in range(n):
#         if i+j>=3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# n=4
# a=4
# for i in range(n):
#     row=""
#     for j in range(n):
#         if i+j>=3:
#             row+="*"
#         else:
#             row+=" "
#     print(row)


# n=10
# a=4
# for i in range(n):
#     row=" "
#     for j in range(n-i-1):
#         row+=" "
#             # print("",end="")
#     for k in range(i+1):
#         row+="* "
#         #   print("* ",end="")
#     print(row)



# n=4
# for i in range(n):
#     row=""
#     for j in range(i):
#         row+="*"
#     for k in range(i+1):
#         row+=" "
#     print(row)

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n=10
# a=1
# for i in range(1,n):
#     row=" "
#     for j in range(1,i+1):
#         row+=f"{j} "
#         # print(j,end=" ")
#     print(row)


# n=4
# a=1
# for i in range(n):
#     for j in range(i+1):
#         print(a,end=" ")
#         a+=1
#     print()

# n=4
# a=1
# for i in range(n):
#     row=" "
#     for j in range(i+1):
#         row+=f"{str(a) } "
#         a+=1
#     print(row+"")


# n=4
# a=1
# for i in range(n):
#     for j in range(i+1):
#         print(a,end=" ")
#         a+=1
#     print()

# n=6
# for i in range(n):
#     raw=""
#     for j in range(n-i):
#             raw+=" "
#     a=1
#     for j in range(i+1):
#         raw+=f"{str(a)} "
#         a=a*(i-j)//(j+1)
#     print(raw)


# n=5
# for i in range(n):
#     row=""
#     for j in range(n-i):
#         row+=" "
#     for k in range(i+1):
#         row+="* "
#     print(row)
# a=n
# for i in range(a):
#     row=""
#     for j in range(i+1):
#         row+=" "
#     for k in range(n-i):
#         row+="* "
#     print(row)


# n=10
# for i in range(1,n):
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()




# n=6
# for i in range(n):
#     for j in range(n):
#         if (i==0 or j==0 ) or (i==n-1 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ") 
#     print()



# n=4
# for i in range(n):
#     for j in range(n):
#         if ((i==0 and j==n-1) or (i==n-1 and j==0) or (i+j==n-1)):
#             print("*",end=" ")
#         else:
#             print("",end=" ")
#     print()
# for i in range(1,n):
#     for j in range(n):
#         if (i==j and j==i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=5
# for i in range(n):
#     raw=""
#     for j in range(n-i):
#         raw+=" "
#     a=1
#     for k in range(i+1):
#         raw+=f"{a} "
#         a=a*(i-k)//(k+1)
#     print(raw)


# n=5
# for i in range(n):
#     row=""
#     for j in range(n-i):
#         row+=" "
#     for k in range(1,i+1):
#         row+=f"{str(i)} "
#     print(row)

# n=6
# for i in range(n):
#     for j in range(i+1):
#         if (i==j and j==i) or(i==n-1 )or (j==0) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=11
# for i in range(n):
#     for m in range(i+1):
#          print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
        

# a=[]
# def add(*x):
    
#     a.append(x)
# n=int(input())
# x=(input().split())
# add(*x)
# print(a)


# def add():
#     # n=int(input())
#     list1=list(map(int,input().split()))
#     print(list1)
# add()

# def addd(n):
#     n=int(input())
#     for i in range(n):
#         return 
# addd()
# print([x for x in range(1,6)] if addd(x))

# nums = [int(i) for i in input("Enter numbers: ").split()]
# print(nums)


# nums = [int(i) for i in input().split()]
# print(nums)
# a=[]
# n=int(input())
# for i in range(n):
#     i=int(input())
#     a.append(i)
# print(a)

# list1=[3, 4, 5, 6, 99, 8, 9, 8, 76, 44, 55, 888]
# print(list1[2:6])

# li=[3, 4, 5, 6, 7, 8, 9, 8, 76, 44, 55, 888]
# li[3]=3333
# print(li)
# li=[3, 4, 5, 6, 7, 8, 9, 8, 76, 44, 55, 888]
# li.append(333333)
# print(li)

# li=[3, 4, 5, 6, 7, 8, 9, 8, 76, 44, 55, 888]
# li.insert(1,44444)
# print(li)

# li=[3, 4, 5, 6, 7, 8, 9, 8, 76, 44, 55, 888]
# li.remove(3)
# li.pop(5)
# a=len(li)
# print(a)
# print(li)
# if 7 in li:
#     print("it is there")
# print()

# li=[3, 4, 5, 6, 7, 8555, 9555, 85555, 75556, 44, 55, 888]
# for i in range(len(li)):
#     for j in range(len(li)):
#         # print(i,j)
#         # print(li[i],li[j])
#         if  li[i]<li[j]:
#             li[i],li[j]=li[j],li[i]
# print(li)

# li=[3, 4, 5, 6, 7, 8555, 9555, 85555, 75556, 44, 55, 888]
# li.reverse()
# b=li[::-1]
# print(b)
# print((li))

# print(li)


# li=[3, 4, 5, 6, 7, 8555, 9555, 85555, 75556, 44, 55, 888]
# copied_list=li[:]
# print(copied_list)

# li=[3, 4, 5, 6, 7, 8555, 9555, 85555, 75556, 44, 55, 888]
# b=li.copy()
# print(b)

# li=[3, 4, 5, 6, 7, 8555, 9555, 85555, 75556, 44, 55, 888]
# li.clear()
# print(li)


# li=[22,222,2222,33,444,5555,666]
# li1=[55,77,888,999,55,4444]
# li.extend(li1)
# print(li)

# li=[[2,4,5,6,7,8],[8,9,6,54,4,3,33],[9,55,666,444,3332]]
# for i in range(len(li)):
#     print(li[i][1])


# li=[2,3,4,5555,666,7777,888]
# op=", ".join(map(str,li))
# print(op)

# li=[2,3,4,5555,666,7777,888]
# maxval=li[0]
# for i in li:
#     if maxval<i:
#         maxval=i
# print(maxval)


# li=[2,3,4,5555,666,7777,888 ,222,222222,2,3,4,222222,222222]
# li2=[]
# duplictes=[]
# for i in li:
#     if i in li and i not in li2:
#         li2.append(i)
#     else:
#         duplictes.append(i)
# print(li2)
# print(duplictes)


# s="lukhmamshik"
# print(list(s))


# li=[[2,3,3,4,55,66],[3,4,5,6],[5,6,7,8,45,6,66,9]]
# op=[i*i for x in li for i in x]
# print(op)
# from itertools import chain
# li=[[2,3,3,4,55,66],[3,4,5,6],[5,6,7,8,45,6,66,9]]
# a=list(chain.from_iterable(li))
# print(a)

# li=["lukhman","virat","dhoni","kinguu","khan"]
# for i in range(len(li)):
#     for j in range(len(li)):
#         if len(li[i])>len(li[j]):
#             li[i],li[j]=li[j],li[i]
# print(li)

# li=[2,3,4,5,6]
# li1=[2,7,8,4,5,9]
# li2=[]
# for i in li:
#     if i in li1:
#         li2.append(i)
# print(li2)

# li=[2,3,4,5,6,4]
# li1=[2,7,8,4,5,9]
# list1=[]
# for i in li:
#     if i not in li1:
#         list1.append(i)
# print(list1)

# li=[2,3,4,5,6,4]
# li1=[2,7,8,4,5,9]
# list1=li+li1
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# list1=[2, 3, 4, 5, 6, 7, 8, 9]
# n=2
# for i in list1:
#     for j in range(2):
#         list1.append(i)
# print(list1)

# list1=[2, 3, 4, 5, 6, 7, 8, 9]
# nested=[]
# for i in range(0,8,2):
#     nested.append([list1[i] ,list1[i+1]])
# print(nested)



# list1=[222222,2333334,444444,55555,66666,777777,88,8,8888888,88888,444]
# b=len(list1)
# list=[]
# for i in range(0,b,2):
#     list.append(list1[i:i+2])
# print(list)


# list1=[222222,2333334,444444,55555,66666,777777,88,8,8888888,88888,444]

# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1[1])


# a=[1,2,3,5]
# b=[1,2,3]
# print(a == b)

# lst=[1,2,3,4,5,6,7]
# k=-3
# # print(lst[-2:]+lst[:-2])

# roated=lst[-k:]+lst[:-k]
# print(roated)

# li=[1,2,3,4,5]
# k=2
# for i in range(k):
#     last=li.pop()
#     li.insert(0,last)
# print(li)

# li=[22,3,4,5,22,44,55,666,22,33,22]
# n=22
# index=[]
# for i in range(len(li)):
#     if li[i]==n:
#         index.append(i)
# print(index)



# a=[4,2,2,1]
# op=[a[i] for i in range(len(a)-1,-1,-1)]
# if a==op:
#     print("the string is palindrom")
# else:
#     print("it is not a palindrom"

# n=int(input())
# a=[]
# for i in range(1,n):
#     a.append(i*i)
# print(a)


# n=int(input())
# is_prime=True
# if n<=1:
#     print("Enter a number greter than 1")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             is_prime=False
#             break
# if is_prime:
#     print("it is prime")
# else:
#     print("it is not prime")


# li=[1,2,3,4,5,6,7,8,8,8888,888,9,8,1,8,8]
# a=[]
# for i in li:
#     a.append(str(i))
# print(a)

# li=['1', '2', '3', '4', '5', '6', '7', '8', '8', '8888', '888', '9', '8', '1', '8', '8']
# a=[]
# for i in li:
#     a.append(int(i))
# print(a)


# Remove all None values from a list.

# li=["liiii",99,"king","khan",66,77,88,99,88,66,88]
# list1=[]
# for i in li:
#     # if i not in range(0,10000):
#     if type(i)!=int :
#         list1.append(i)
# print(list1)
        

# li=["lukhman","kinggg","jassuu","kijjjbjah"]
# liii=list(enumerate(li))
# print(liii)

# pairs = [(1, 2), (3, 4), (5, 6)]
# # sums=[a+b for a ,b in pairs]


# # print(sums)
# sum=[]
# for i in pairs:
#     a=i[0]
#     b=i[1]
#     sum.append(a+b)
# print(sum)
# li=[1, 4, 9, 16, 25, 36, 49, 64, 81]
# mid=len(li)//2
# print(li[mid:],li[:mid])



# s="python"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

# for i in range(5):
#     for k in range(5-i):
#         print(" ",end=" ")
#     for j in range(5):
#         print("*",end="")
#     print()


# n=10
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     y=1
#     for k in range(i+1):
#         print(y,end=" ")
#         y=y*(i-k)//(k+1)
#     print()

# import copy

# original = [[1, 2], [3, 4]]

# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# # Modify nested list
# original[0][0] = 100

# print("Original:", original)  # [[100, 2], [3, 4]]
# print("Shallow :", shallow)   # [[100, 2], [3, 4]]  ← affected!
# print("Deep    :", deep)      # [[1, 2], [3, 4]]    ← not affected!


# s="lukhman"
# a=""
# for i in s:
#     a=i+a
# print(a)

# li=[2,4,6,8,10]
# for i in li:
#     li.append(i+2)
#     if len(li)>8:
#         break
# print(li)

# user=input("enter the numbers: ")
# elemnets=user.split()
# t=tuple(elemnets)
# print(t)




