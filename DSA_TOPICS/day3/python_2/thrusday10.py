# n=int(input())
# dicti={}
# for i in range(n):
#     name,*line=input().split()
#     socres=list(map(float,line))
#     dicti[name]=socres
# quirey_name=input()
# avg=sum(dicti[quirey_name])/len(dicti[quirey_name])
# print(avg)
# import re
# s=input()
# # print(len(s))
# for i in range(len(s)):
#     if s[i]==s[i+1]:
#         print(i,i+1) 

# S = input()
# k = input()

# found = False

# for i in range(len(S) - len(k) + 1):
#     if S[i:i+len(k)] == k:
#         print(f"({i}, {i + len(k) - 1})")
#         found = True

# if not found:
#     print("(-1, -1)")

# 1.print digits from num without converting into string

# n=int(input("enter the number: "))
# # n=0
# while n>0:
#     digit=n%10
#     print(digit)

#     n=n//10




# 2.sum of digits in given num

# num=int(input("eneter the number: "))
# sum=0
# for i in range(len(str(num))):
#     digit=num%10
#     sum+=digit
#     num=num//10
# print(sum)


# num=int(input("eneter the number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
# print(sum)


# num=int(input("eneter the number: "))
# sum=0
# # for i in range(len(str(num))):
# while num>0:
#     digit=num%10
#     sum=digit**2+sum
#     num=num//10
# print(sum)

# 3.count digits in given number

# num=int(input("eneter the number: "))
# count=0
# # for i in range(len(str(num))):
# while num>0:
#     digit=num%10
#     count+=1
#     num=num//10
# print(count)


# 4.check palindrome num or not

# num=int(input("eneter the number: "))
# asn=num
# sum=0
# # for i in range(len(str(num))):

# while num>0:
#     digit=num%10
#     sum=sum*10+digit
#     num=num//10
# # print(sum)
# if asn==sum:
#     print("It is pallindrom")
# else:
#     print("Not a plaindrom")

# print(sum)
# 5.check Armstrong num or not

# num=int(input("eneter the number: "))
# asn=num
# sum=0
# # for i in range(len(str(num))):
# while num>0:
#     digit=num%10
#     sum=digit**len(str(asn))+sum
#     num=num//10
# print(sum)
# if asn==sum:
#     print("it is amstrong number")
# else:
#     print("it is not an amstrong number")

# num=int(input("eneter the number: "))
# asn=num
# asn1=num
# count=0
# while num>0:
#     digit=num%10
#     count+=1
#     num=num//10
# # print(count)
# sum=0
# # for i in range(len(str(num))):
# while asn>0:
#     digit=asn%10
#     sum=digit**count+sum
#     asn=asn//10
# # print(sum)
# if asn1==sum:
#     print("it is amstrong number")
# else:
#     print("it is not an amstrong number")


# 6.factors for given num

# num=int(input("Enter the number: "))
# i=1
# while i<num:
#     if num%i==0:
#         print(i,end=" ")
#     i+=1





# 7.what is neon num

# n=int(input("Enter the number: "))
# a=n
# square=n**2
# # print(sum)
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n=n//10
# # print(sum)
# if a==square:
#     print("It is a neon number")
# else:
#     print("It is not a neon number")



# num=int(input("Enter number: "))
# ans=num
# sum=1
# while num>0:
# for i
#     if num==1 and ans==1:
#         sum
#     elif num>=2:
#         sum=num*(num-1)*sum
#     
# print(sum)


# final_value=1
# while ans>0:
#     digit=ans%10
#     final_value=digit*(digit-1)*final_value
#     ans//=10
#     print(ans)

# num=int(input("Enter number: "))
# ans=num
# sum=1
# while num>0:
#     if num==1 and ans==1:
#         sum
#     elif num>=2:
#         sum=num*(num-1)*sum
#     num=num-2
# print(sum)

# num=int(input("Enter number: "))
# ans=num
# final_value=1
# while ans>0:
#     digit=ans%10  #5=num
#     sum=1

#     if num==1 and ans==1:
#         sum
#     elif num>=2:
#         sum=num*(num-1)*sum
#         num=num-2
#     print(sum)
#     ans//=10   #14
# print(final_value)




# num=int(input("Enter number: "))
# # ans=num
# sum1=0
# while num>0:
#     digit=num%10
#     ans=digit
#     sum=1
#     while digit>0:

#         if digit==1 and ans==1:
#             sum
#         elif digit>=2:
#             sum=digit*(digit-1)*sum
#             sum1+=sum
#         digit=digit-2
#     num=num//10
#     print(sum1)

# num=int(input("Enter number: "))
# ans=num
# sum1=0
# while num>0:
#     digit=num%10
#     fact=1
#     for i in range(1,digit+1):
#         fact=fact*i
#     sum1+=fact
#     num=num//10
#     print(sum1)

# while digit>0:
#     if digit==1 and ans==1:
#         sum
#     elif num>=2:
#         sum=digit*(digit-1)*sum
#     num=num-2
#     print(sum)


# num=int(input("Enter number: "))
# ans=num
# sum1=0
# while num>0:
#     digit=num%10
#     fact=1
#     for i in range(1,digit+1):
#         fact=fact*i
#     sum1+=fact
#     num=num//10
#     print(sum1)


# ================================================================================


# 7.what is neon num

# n=int(input("Enter the number: "))
# a=n
# square=n**2
# # print(sum)
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n=n//10
# # print(sum)
# if a==square:
#     print("It is a neon number")
# else:
#     print("It is not a neon number")


# num=int(input("eneter the number: "))
# asn=num
# asn1=num
# count=0
# while num>0:
#     digit=num%10
#     count+=1
#     num=num//10
# # print(count)
# sum=0
# # for i in range(len(str(num))):
# while asn>0:
#     digit=asn%10
#     sum=digit**count+sum
#     asn=asn//10
# # print(sum)
# if asn1==sum:
#     print("it is amstrong number")
# else:
#     print("it is not an amstrong number")


# n=int(input("Enter the number: "))
# num=n+1
# count=0
# # for i in range(1,n+1): 
# if (num)**0.5==int(num**0.5):
#     print(f"{n} is a strong number")
# else:
#     print(f"{n} is not a stong number")



# num=int(input())
# print(num**0.5)
# print(int(num**0.5))



# d={"lukhman":3333,"azeez":7}
# d1={"king":9,"zero":77}
# d2=d|d1
# print(d2)


# 
# arr=[20,44,222,4444,545445,22334545,778763333333,55,1,2,90]
# fst=float("inf")
# sec=float("inf")
# for i in arr:
#     if fst>i:
#         sec=fst
#         fst=i
#     # elif i>sec and i!=fst:
#     #     sec=i
# print(sec)




# arr=[4,5,6,7,888,99,9,99999,9999,444]
# fst=sec=float("-inf")
# for i in arr:
#     if i >fst:
#         sec =fst
#         fst =i
#     elif i>sec and i != fst:
#         sec=i
# print(sec)


