# # Initialize empty list
# my_list = []

# # Take number of commands
# N = int(input())

# # Process each command
# for _ in range(N):
#     cmd = input().split()
#     operation = cmd[0]

#     if operation == "insert":
#         my_list.insert(int(cmd[1]), int(cmd[2]))
#     elif operation == "print":
#         print(my_list)
#     elif operation == "remove":
#         my_list.remove(int(cmd[1]))
#     elif operation == "append":
#         my_list.append(int(cmd[1]))
#     elif operation == "sort":
#         my_list.sort()
#     elif operation == "pop":
#         my_list.pop()
#     elif operation == "reverse":
#         my_list.reverse()
# # print(my_list)
# mylist=[]
# n=int(input())
# for i in range(n):
#     command=input().split()
#     operation=command[0]
#     # mylist.append(command)
#     print(mylist)

# Perform operations on a list of student scores:
# Commands:
# add e: Add score e to the list.
# avg: Print the average of the scores.
# max: Print the highest score.
# min: Print the lowest score.
# remove e: Remove score e.
# print: Print the current list.
# import math
# my_list=[]
# n=int(input())
# for i in range(n):
#     comm=input().split()
#     operation=comm[0]
#     if operation=='add':
#         my_list.append(comm[1])
        
#     elif operation=="avg":
#         b=math.avg(comm[1])
#         print(b)
#     elif operation=="min":
#         print(min(my_list))
#     elif operation=="max":
#         print(max(my_list))
# print(my_list)
    


# scores=[]
# n=int(input())
# for i in range(n):
#     cmd=input().split()
#     if cmd[0]=="add":
#         scores.append(int(cmd[1]))
#     elif cmd[0]=='avg':
#         if scores:
#             avg=(sum(scores)/len(scores))
#         else:
#             print("No scores")
    
# scores = []
# n = int(input())
# for _ in range(n):
#     cmd = input().split()
#     if cmd[0] == "add":
#         scores.append(int(cmd[1]))
#     elif cmd[0] == "avg":
#         if scores:
#             avg = sum(scores) / len(scores)
#             print(f"Average: {avg:.2f}")
#         else:
#             print("No scores")
#     elif cmd[0] == "max":
#         if scores:
#             print(f"Max: {max(scores)}")
#     elif cmd[0] == "min":
#         if scores:
#             print(f"Min: {min(scores)}")
#     elif cmd[0] == "remove":
#         val = int(cmd[1])
#         if val in scores:
#             scores.remove(val)
#     elif cmd[0] == "print":
#         print(scores)

# print(hash("apple"))   # Returns a unique integer for the string "apple"
# print(hash(123))       # Works with numbers too


# n=int(input())
# list=map(list(int,input().split()))
# b=tuple(list)
# print(hash(b))

# n=int(input())
# list1=map(int,input().split())
# b=tuple(list1)
# print(hash(b))


# s = input()
# result = s.swapcase()
# print(result)

# line=input()
# a=""
# for i in range(len(line)):
#         if line[i]==" ":
#             a+="-"
#         else:
#              a+=line[i]
# print(a)
# print(line[i])


# li=[9,7,6,5,19,5,4,1,2,-3,4]
# minval=li[0]
# for i in ra2,6nge(len(li)):
#     if minval>li[i]:
#         minval=li[i]
# print(minval)


# li=[9,7,6,5,19,5,4,1,2,-3,4]
# maxval=li[0]
# for i in range(len(li)):
#     if maxval<li[i]:
#         maxval=li[i]
# print(maxval)


# li=[4,,1,6]
# minval=li[0]
# ans=0
# for i in range(1,len(li)):
#     ans=max(ans,(li[i]-minval))
#     minval=min(minval,li[i])
# print(ans)


# li=[4,2,6,1,6]
# minval=li[0]
# ans=0
# for i in range(1,len(li)):
#     ans=max(minval,li[i])
#     minval=min(minval,li[i])
# print(ans-minval)

# li=[7,1,5,4]
# ans=[]
# for i in range(len(li)):
#     for j in range(1,len(li)):
#         if li[i]<li[j]:
#             a=abs(li[i]-li[j])
#             ans.append(a)
# print(max(ans))


# a=1
# for i in range(1,6):
#     for j in range(1,4):
#         # for j in range(1,4):
#         print(a,end=" ")
#         a+=1
#     print()


# 
# list1=[[5,1,7],[2,8,5],[6,4,1]]
# sum=0
# a=[]
# # a=list1[0][0]
# # print(a)
# for i in list1:
#     for k in i:
#         a=list1[i][0]
#         if a<list1[k]:
            
#     for j in i:
#         ab=sum+j
#         a.append(ab)
#     print(i)
#     print(sum)

# a=[]
# sum=0
# ad=[]
# n=int(input())
# for i in range(len):
#     cmd=input().split()
#     b=sorted(cmd)
#     a.append(b)
#     for j in i:
#         sum+=j
#         ad.append(sum)
#     print(ad)
# print(a)



# list1=[[5,1,7],[2,8,5],[6,4,1]]
# sum=0
# a=[]
# # a=list1[0][0]
# # print(a)
# for i in list1:
#     for k in i:
#         a=list1[i][0]
#         if a<list1[k]:
            
#     for j in i:
#         ab=sum+j
#         a.append(ab)
#     print(i)
#     print(sum)




# list1=['kiran','lukhman','king']
# op=[x.upper() for x in list1]
# print(op)


# op=[x**2 for x in range(10,31)if x%2==0]
# print(op)

# list1=["king","welocme","queen","hai","bhai"]
# op=[x.upper() for x in list1 if len(x)%2==0]
# print(op)
# def vowels(ip):
#     count=0
#     for x in ip:
#         if x in ['a','e','i','o','u']:
#             count+=1
#     if count%2==0:
#         return True
#     else:
#         return False
# list1=["king","welocme","queen","hai","bhai"]
# op1=[x.upper() for x in list1 if vowels(x) ]
# print(op1)

# list1=["king","welocme","queen","hai","bhai"]
# str1="AEIOUaeiou"
# op=[x.upper() for x in list1 if x in str1]
# print(op)

# def perfect(num):
#     num1=num
#     sum=0
#     count=len(str(num))
#     while num>0:
#         digit=num%10
#         sum+=digit**count
#         num=num//10
#         # print(count)

#     if sum==num1:
#         return True
#     else:
#         return False
# op1=[x for x in range(100,1001) if perfect(x)]
# print(op1)



# list1=["lukhmana","virat","hai","josheph","dhonia"]
# for i in range(len(list1)):
#     for j in range(0,len(list1)-i-1):
#         print(list1[j],list1[j+1])
#         if len(list1[j])>len(list1[j+1]):
#             list1[j],list1[j+1]=list1[j+1],list1[j]
            
# print(list1)
    
# for i in range(len(list1)):
#     for j in range(0,len(list1)-i-1):
#         if len(list1[i])>len(list1[j]):
#             list1[j],list1[j+1]=list1[j+1],list1[j]


# def am_strong(num):
#     num2=num
#     num1=num
#     count=0
#     sum1=0
#     while num>0:
#         digit=num%10
#         count+=1
#         num=num//10
    
#     while num1>0:
#         digit=num1%10
#         sum1=digit**count+sum1
#         num1=num1//10
#     if num2==sum1:
#         return True
#     else:
#         return False
# op=[x for x in range(100,1000) if am_strong(x)]
# print(op)