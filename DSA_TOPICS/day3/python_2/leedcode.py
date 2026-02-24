# li=[1,1,1,3,3,4,3,2,4,2]
# is_notdupli=False
# for i in li:
#     if li.count(i)>=2:
#         is_notdupli=True
# if is_notdupli:
#     print("True")
# else:
#     print("False")
    

# a=count()


# li=[1,1,1,3,3,4,3,2,4,2]
# a=set(li)
# if len(a)<len(li):
#     print("true")
# elif len(a)==len(li):
#     print("false")

# s = "anagram"
# t = "nagaram"
# c=0
# for i in s:
#     if i in t:
#         c+=1
# if c==len(t):
#     print("true")
# else:
#     print("false")


# b=set(s)
# c=set(t)
# if c==b:
#     return True
# else:
#     return False
# print(b)
# print(c)

# def is_anagram(s, t):
#     if len(s) != len(t):
#         return False

#     count_s = {}
#     count_t = {}

#     for ch in s:
#         if ch in count_s:
#             count_s[ch] += 1
#         else:
#             count_s[ch] = 1

#     for ch in t:
#         if ch in count_t:
#             count_t[ch] += 1
#         else:
#             count_t[ch] = 1

#     return count_s == count_t

# s = "anagram"
# t = "nagaram"
# is_anagram=True
# if len(s)!=len(t):
#     # return False
#     is_anagram=False
# c={}
# b={}
# for i in s:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# for j in t:
#     if j in b:
#         b[j]+=1
#     else:
#         b[j]=1

# if c==b:
#     return True
# else:
#     return False

# a="abcaaaaaaaaa"
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# li=["abc","ab","a","abcd","abbbb",1,2,3,4,5,6,5,3]
# b=[]
# for i in range(0,len(li)-1,2):
#     # for j in range(len(li)):
#         b.append([li[i],li[i+1]])
# if len(li)%2!=0:
#         b.append([li[-1]])
# print(b)

# entities=int(input())
# li=[]
# for i in range(entities):
#         n=input()
#         li.append(n)
        
# # li=["abc","ab","a","abcd","abbbb",1,2,3,4,5,6,5,3]
# # li=list(map(int,input().split()))
# li=list(input().split())
# print(li)
# b=[]
# for i in range(0,len(li)-1,2):
#     # for j in range(len(li)):
#         b.append([li[i],li[i+1]])
# if len(li)%2!=0:
#         b.append([li[-1]])
# print(b)


# strs = ["eat","tea","tan","ate","nat","bat"]
# a=[]

# for i in range(strs):


# nums = [2,7,11,15]
# target = 9



# nu  ms=[2,7,11,15]
# target=9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] ==target:
#             # print(i,j)
#             print([i,j])
    


# li=[[1,5,4],[5,7,8],[9,7,8]]
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(i,2)
#         # print(li[i][j])



# li=[1,5,8,0,1,8,1,5,1]
# d={}
# for i in li:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)




# str1="   lukhman      shaik   "
# # print(str1.strip())
# # print(str1.lstrip())
# print(str1.rstrip())

# str1="*****lukhman      shaik********"
# # print(str1.strip('*'))
# # print(str1.lstrip('*'))
# print(str1.rstrip('*'))


# str1="i like java,i am too good at java,java developer"
# print(str1.replace('java','python'))


# str1=["i","am","lukhman","shaik","i","am","going","to","institute","with","bike"]
# print(''.join(str1))


# dicti={"lukhman":4,"kaleel":6,"king":9,"shaw":9,"luuuu":90}
# dicti2={"lukhma3333n":433,"33333kaleel":33336,"ki33333ng":33333339}
# dicti.update(dicti2)
# print(dicti)
# print(dicti.clear())
# print(list(dicti.keys()))
# print(list(dicti.values()))
# print(a)


# set={1,2,3,4,5,6,78,88,99}
# # set.add(999999)
# set.update([2,44444],[7,6666666],[8,45454545])
# print(set)

# Number of terms
# n = int(input("Enter the number of terms: "))

# # First two terms
# a = 0
# b = 1

# print("Fibonacci Series:")
# for i in range(n):
#     print(a, end=" ")
#     # Swap and update
#     a, b = b, a + b


# arr=[10,20,30,40]
# postion=2
# value=25
# arr.append(0)
# for i in range(len(arr)-1,postion,-1):
#     arr[i]=arr[i-1]
# # arr[postion]=value
# # arr.append(0)
# # arr[5]=66
# print(arr)



# r=2
# c=3
# m=[]
# for i in range(3):
#     x=[]
#     for j in range(3):
#         value=int(input())
#         x.append(value)
#     m.append(x)
# print(m)

# arr=[2,6,7,9,14,15,-9,8]
# n=len(arr)
# p=[0]*n
# p[0]=arr[0]
# for i in range(1,n):
#     p[i]=p[i-1]+arr[i]
# print(p)

# li=[1,8,9,2,3,4,5,6,7,8,9,99]
# n=len(li)
# list1=[]  
# for i in range(n):           #0                ,1      ,2,
#     for j in range(i,n):       #0,1,2            ,1,2    ,2
#         # print(li[i],li[j])
#         temp=[]    #
#         for k in range(i,j+1):  #0,1,2           ,1,2     ,2
#             temp.append(li[k])
#         list1.append(temp)  #1,1 8,1 8 9,   ,8,8 9,  ,9
# print(list1)



# l="lukhman"
# n=len(l)
# a=[]
# for i in range(n):
#     for j in range(i,n):
#         ki=""
#         for k in range(i,j+1):
#             ki+=l[k]
#         a.append(ki)
# print(a) 

# l=[5,9,1,8,7]
# n=len(l)
# a=[]
# for i in range(n):
#     for j in range(i,n):
#         sum1=0
#         c=0
#         for k in range(i,j+1):
#         #     print(l[k],end=" ")
#         # print(type(l[k]))
#             c+=1
#             if c==3:

#                 sum1+=l[k]
#         a.append(sum1)
#         print(a)




# l=[5,9,1,8,7]
# a=len(l)
# c=[]
# for i in range(a):
#     for j in range(i,a):
#         b=[]
#         for k in range(i,j+1):
#             b.append(l[k])
#         c.append(b)
# sum1=[]
# for m in range(len(c)):
#     if len(c[m])==3:
#         # print(c[m])
#         sum2=0
#         for z in c[m]:
#             sum2+=z
#         sum1.append(sum2)
# print(max(sum1))


# l=[5,9,1,8,7,9,8,7,9,9,9]
# a=len(l)
# c=[]
# ans=0
# for i in range(a):
#     for j in range(i,a):
#         b=[]
#         tsum=0
#         for k in range(i,j+1):
#             b.append(l[k])
#             tsum+=l[k]
#         if len(b)==3:
#             ans=max(ans,tsum)
# print(ans)

# li=[5,9,1,8,7]
# n=len(li)
# l=0
# temp=0
# ans=0
# for r in range(n):
#     temp+=li[r]
#     if r-l==3:
#         temp-=li[l]
#         l+=1
#     if r-l+1==3:
#         ans=max(ans,temp)
# print(ans)

# li=[5,9,1,8,7]
# n=len(li)
# l=0
# temp=0
# ans=0
# for i in range(n):
#     temp+=li[i]
#     if i-l==3:
#         temp-=li[l]
#         l+=1
#     if i-l+1==3:
#         ans=max(ans,temp)
# print(ans)




# li=[5,9,1,8,7]
# ans=0
# n=len(li)
# l=0
# temp=0
# for i in range(n):
#     temp+=li[i]
#     if i-l==3:
#         temp-=li[l]
#         l+=1
#     if i-l+1==3:
#         ans=max(temp,ans)
# print(ans)

# s ="aababcabc"
# n=len(s)
# l=0
# a=[]
# for i in range(n):
#     for j in range(i,n):
#         ans=""
#         for k in range(i,j+1):
#             ans+=s[k]

#         if len(ans)==3 and len(set(ans))==3:
#             l+=1
#             # a.append(ans)
# print(l)
# # c=0
# # for i in a:
# #     b=set(i)
# #     if len(b)==3:
# #         c+=1
# # print(c)









# s = "xyzzaz"
# n=len(s)
# ans=0
# temp=""
# l=0
# k=3
# for i in range(n):
#     temp+=s[i]
#     if i-l==k:
#         temp+=1
#         l+=1
#     print(temp)




# s ="xyzzaz"
# # s = "aababcabc"
# l=0
# n=len(s)
# li=[]
# c=0
# for i in range(n):
#     li.append(s[i])
#     # print(temp)
#     if i-l==3:
#         li.pop(0)
#         l+=1
#     if i-l+1==3 and len(set(li))==3:
#         c+=1
# print(c)


# s ="xyzzaz"
# s = "aababcabc"
# n=len(s)
# a=0
# dicti={}
# l=0
# c=0
# for i in range(n):
#     if s[i] in dicti:
#         dicti[s[i]]+=1
#     else:
#         dicti[s[i]]=1
#     if i-l==3:
#         dicti[s[l]]-=1
#         if dicti[s[l]]==0:
#             dicti.pop(s[l])
#         l+=1
    
#     if i-l+1==3 and len(dicti)==3:
#         c+=1
# print(c)

# # Print first n Fibonacci numbers using swapping
# n = 10
# a = 0
# b = 1

# # print(a, b, end=" ")  # Print first two numbers

# for _ in range(n):  # Already printed 2 numbers
#     # temp = a + b        # Next term
#     # print(a, end=" ")
#     temp=a+b
#     a=b
#     b=temp
    # a=0
    # print(a, end=" ")

    # a, b = b, a+b     # Swapping: update a and b


# val=float("-inf")
# ans=3
# print(max(ans,val))

# nums = [9,4,1,7]
# k = 2
# ans=0
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         for k in range(i,j+1):
#             ans=max(ans,nums[i]-nums[j])
# print(ans)


# # nums = [3,4,8,1,5]
# # nums = [9,4,1,7]
# nums=[87063,61094,44530,21297,95857,93551,9918]
# nums.sort()
# print(nums)
# print(nums[-1]-nums[-2])




# list1=["hello","welcome","something","hello","apple","apple"]
# dicti={}
# for i in range(len(list1)):
#     if list1[i] in dicti:
#         dicti[list1[i]]+=1
#     else:
#         dicti[list1[i]]=1
# print(dicti)


# s="BANANA"
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)




# li=[10,20,30,40]
# p=2
# value=25
# li.append(0)
# # print(li)
# for i in range(len(li)-1,p,-1):

#     li[i]=li[i-1]
# # print(li)
# li[p]=value
# print(li)



# li=[10,20,30,40,50,60,70]
# n=len(li)
# p=[0]*n
# p[0]=li[0]
# for i in range(1,n):
#     p[i]=p[i-1]+li[i]
# print(p)
#  369/*

# *``


# li=[1,2,2,4]
# b=set(li)
# print(b)


# arr = [1, 3, 5, 8, 10]
# diff = 2
# left=0
# right=0
# while left <len(arr) and right<len(arr):
#     if left!=right:

#         diff_value=arr[right]-arr[left]
#         if diff_value==diff:
#             print(arr[left],arr[right])
#             break
#         elif diff_value<diff:
#             right+=1
#         else:
#             left+=1
#     else:
#         right+=1

# arr = [0, 1, 0, 3, 12]
# a=len(arr)
# left=0
# right=a-1
# p=[0]*a
# # strt=arr[0]
# while left<right:
#     if left==right:

#         ans=float("-inf")
#         ab=max(arr[left],arr[right])
#         ans=max(ans,ab)
#         p.append(ans)
#     elif 
    
# print(ans)

    

# def prime(n):
#     n=int(input("enter tehnumber"))
#     is_prime=True
#     list1=[]
#     if n<=1:
#         return "enter a valid number above 1"
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 is_prime=False
#                 list1.append(i )
#             if len(list1)>5:
#                 break
#     if is_prime(n):
#         print(list1)
#     else:
#         print("nothimg")


def print_first_5_primes(num):
    count = 0      
    list1=[]   
    while count < 5:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            list1.append(num)
            count += 1  
        num += 1  
    print(list1)
num=int(input("enter the stating number: "))
print_first_5_primes(num)

# n=10
# for i in range(n-1,-1,-1):
#     for j in range(1,i):
#         print(j*j,end="")
#     print()





