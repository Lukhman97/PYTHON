# def fun(num):
#     is_prime=True
#     if num<=1:
#         is_prime=False
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 is_prime=False
#                 break
#         return is_prime
# num=int(input())
# if fun(num):
#     print("prime number")
# else:
#     print("Not a prime number")


# def fun(num):
#     i=1
#     is_squre=False
#     if num<1:
#         return False
#     else:
#         while i*i<=num:
#             if i*i==num:
#                 is_squre=True
#                 break
#             i+=1
#         return is_squre

# num=int(input())
# if fun(num):
#     print("IT is square")
# else:
#     print("NOt")
    


# num=int(input())
# def fun(num):
#     num1=num
#     num2=num
#     c=0
#     while num>0:
#         digit=num%10
#         c+=1
#         num//=10
#     sum1=0
#     while num1>0:
#         digit1=num1%10
#         sum1+=digit1**c
#         num1//=10
#     if num2==sum1:
#         return True
#     else:
#         return False
# a=[]
# for i in range(1,100000):
#     if fun(i):
#         a.append(i)
# print(a)
    
    

# r=5
# for i in range(1,r):
#     for k in range(r-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


# r=10
# for i in range(r):
#     for k in range(r-i):
#         print(' ',end="")
#     for j in range(i+1):
#         print(chr(97+j-32),end=" ")
#     print()


# str1="aaaaaaabbbbbbccc"
# str2=""
# count=1
# for i in range(1,len(str1)):
#     if str1[i]==str1[i-1]:
#         count+=1
#         if count>=2:
#             str2+=str1[i-1]
#             break
            
#     else:
#         str2+=str1[i-1]+str(count)
#         count=1
        
        
# str2+=str1[-1]+str(count)
# print(str2)



# str1="aaaaaabbbbbbcccccdddd"
# result=""
# c=0
# for i in range(1,len(str1)):
#     if str1[i]==str1[i-1]:
#         c+=1
#         if c<=3:
#             result+=str1[i]
#     else:
#         c=1
#         result+=str1[i]
# result=str1[0]+result
# print(result)


# str1="lukhmanshaik"
# s=""
# for i in str1:
#     s=i+s
# print(s)

# s="madam12"

# print(s[::-1])

# n=int(input())
# is_prime=True

# if n<=1:
#     is_prime=False
# else:
#     for i in range(2,n):
#         if n%i==0:
#             is_prime=False
#             break
# if is_prime:
#     print("It is prime")
# else:
#     print("It is not a prime")


# a="lukhmanshaikaa"
# dic={}
# for i in a:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]+=1
# # sorted_by_keys = dict(sorted(dic.items()))
# # print(sorted_by_keys)

# ab=dic.keys()

# print(ab)
# k=[]
# for i in range(len(ab)):
   
#     for j in range(i+1,len(ab)):
#         if ab[i]>ab[j]:
#             ab[j],ab[j+1]=ab[j+1],ab[j]
# sorted_by_keys = {}
# for k in ab:
#     sorted_by_keys[k] = dic[k]
# print(ab)





# a=1
# sum1=1
# while a<=5:
#     if a ==1:
#         sum1+=a
#     else:
#         sum1*=a

#     a+=1
# print(sum1)


# n=int(input())
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)


li=[1,33,4,4,45,5,5,555,6,666,66,6,6,67,7,88,90]
a=sec=li[0]
for i in li:
    if i>a :
        sec=a
        a=i
    elif i>sec and i!=a:
        sec=i
print(sec)
