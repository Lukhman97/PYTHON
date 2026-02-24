# n=4
# for i in range(1,n):
#     for j in range(1,n):
#         print(i,end=" ")
#     print()




# n=int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int,input().split())))
# print(a)


# entities=int(input("No.of entities: "))
# nested_list=[]
# for i in range(entities):
#     in_list=[]
#     size_of_nexted_list=int(input("Ebnter iner list size:  "))
#     for j in range(size_of_nexted_list):
#         value=int(input())
#         in_list.append(value)
#     nested_list.append(in_list)
# print(nested_list)



# li=[[2, 3, 4], [3, 9, 2], [3, 4, 2]]
# sum=0
# for i in range(len(li)):
#     # print(i)
#     for j in range(len(li[i])):
#         # print(li[i],li[i][j])
#         if i==1 and j==1:
#             sum+=0
#         else:
#             sum+=li[i][j]
# print(sum)




# li=[[2, 3, 4], [3, 9, 2], [3, 4, 1]]
# sum=0
# for i in range(len(li)):
#     # print(i)
#     for j in range(len(li[i])):
#         # print(li[i],li[i][j])
#         if i==j :
#             sum+=li[i][j]
#         else:
#             sum+=0
# print(sum)




# li=[[2, 3, 4], [3, 9, 2], [3, 4, 1]]
# sum=0
# for i in range(len(li)):
#     # print(i)
#     for j in range(len(li[i])):
#         # print(li[i],li[i][j])
#         if i==j or (i==0 and j==2) or (i==2 and j==0):
#             sum+=li[i][j]
#         else:
#             sum+=0
# print(sum)


# li=[[2, 3, 4], [3, 9, 2], [3, 4, 1]]
# sum=0
# for i in range(len(li)):
#     # print(i)
#     for j in range(len(li[i])):
#         # print(li[i],li[i][j])
#         if i==1 and j==1 :#or (i==0 and j==2) or (i==2 and j==0):
#             print(" ",end=" ")
#         else:
#             print(li[i][j],end=" ")
#     print()


# li=[[2, 3, 4], [3, 9, 2], [3, 4, 1]]
# sum=0
# for i in range(len(li)):
#     # print(i)
#     for j in range(len(li[i])):
#         # print(li[i],li[i][j])
#         if (i==0 and j==1) or (i==1 and j==0)  or (i==1 and j==2) or (i==2 and j==1):#or (i==0 and j==2) or (i==2 and j==0):
#             print(" ",end=" ")
#         else:
#             print(li[i][j],end=" ")
#     print()



# str="a+((b-c)+d)"
# s=""
# for i in str:
#     if i=="(" or i==")":
#         s+=""
#     else:
#         s+=i
# print(s)


# str="a+((b-c)+d)"

# a=str.replace("(","").replace(")","")
# print(a)



# n=int(input())
# k=[]
# a=0
# b=1
# while a<n:
#     # print(a,end=" ")
#     k.append(a)
#     a,b=b,a+b
# for i in range(1,n+1):
#     if i not in k:
#         print(i,end=" ")
            
# n=int(input())
# fib=[0,1]
# while fib[-1]<=n:
#     fib.append(fib[-1]+fib[-2])
# for i in range(1,n+1):
#     if i not in fib:
#         print(i,end=" ")


# n=50
# fib=[0,1]

# while fib[-1]<=n:
#         fib.append(fib[-1]+fib[-2])
# if fib[-1]>n:
#     fib.pop()
#     # else:
# print(fib)


# n=int(input())
# list1=[]
# for i in range(2):
#     value=int(input())
#     list1.append(value)
# while list1[-1]<=n:
#     list1.append(list1[-1]+list1[-2])
# print(list1)


# list1=["lukh","kinhhhh","heroooo00000","kalyannnn","atitudekkk","kkkaabababbab"]
# dicti={}
# for i in list1:
#     if i not in dicti:
#         dicti[i]=len(i)
# print(dicti)



# li1=["hai","iam","kingg","ogthe","heroo"]
# dic={}
# li2=[3,4,5,6,7]
# for i in range(len(li1)):
#         dic[li1[i]]=li2[i]
# print(dic)



# li1=["a","b","c",'d',"e"]
# li2=[3,4,5,6,7]
# dic={}
# i=0
# while i<len(li1):
#         dic[li1[i]]=li2[i]
#         i+=1
# print(dic)

# li1=["hai","iam","kingg","ogthe","heroo"]
# # dic={}
# li2=[3,4,5,6,7]

# d=dict(zip(li1,li2))
# print(d)


# l={'hai': 3, 'iam': 4, 'kingg': 5, 'ogthe': 6, 'heroo': 7}
# d={}
# for keys,values in l.items():
#     d[values]=keys
# print(d)
# a=[]
# for i in d.keys():
#     a.append(i)
# print(a)


# dic={3: 'hai', 4: 'iam', 5: 'kingg', 6: 'ogthe', 7: 'heroo'}
# # print(dic["hai"])
# a=[]
# for i in dic.keys():
#     a.append(i)
# maxval=a[0]
# for i in range(len(a)):
#     if a[i]>maxval:
#         maxval=a[i]
# print(dic[maxval])


    
# a= {'C':{'x':7,'y':3},'A': {'x': 3, 'y': 1}, 'B': {'x': 2, 'y': 4}}
# b=[]
# c={}
# for i in a.keys():
#     b.append(i)
# for i in range(len(b)):
#     for j in range(len(b)-1):
#         if b[j]>b[j+1]:
#             b[j],b[j+1]=b[j+1],b[j]
# for i in b:
#    c[i]=dict(sorted(a[i]))
# print(c)
# for values in c.values():
#     print(values)





# git init
# git add ./filename/foldername
# git status
# git commit -m "message"
# git remote add origin "git url"
# git branch -m main
# git push origin main


# git remote add oriign "git limk"
# git banch -m main
# git push origin main
# git 
