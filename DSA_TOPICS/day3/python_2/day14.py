# for i in range(5):
#     print(i)
#     if i==5:
#         break


# for i in range(5):
#     # print(i)
#     if i==5:
#         break
    # print(i)


# for i in range(1,10):
#     print(i)
#     if i==5:
#         continue


# for i in range(1,10):
  
#     if i==5:
#         continue
#     i+=1
#     print(i)





# i=1
# while i<=12:
#     print(i)


#     i+=1




# a=True
# while(a):
#     print("WASTe of time")
#     break


# a=1
# while a<=20:
#     if a&1==0:
#         print(a,end=" ")
#     a+=1

# a=2
# while a<=20:
#     print(a,end=" ")
#     a+=2

# s="hello"
# for i in range(len(s)):
#     for j in range(1,len(s)-1):
#         l=i
#         r=i-1-len(s)
#         print(i,j)


# s="hello"
# a=""
# for i in range(len(s)-1,-1,-1):
#     a+=s[i]
# print(a)
# if a!=s:
#     print("it is palindrom")
# # else:
#     print("ccc")
    # print(s[i],end="")



# s=input()
# a=""
# for i in range(len(s)-1,-1,-1):
#     a+=s[i]
# print(a)
# if a!=s:
#     print("it  not is palindrom")
# else:
#     print("iT is palindrom")
# reverse a number intlo string using while loop
# reverse a number using while loop

# s=input()
# i=0
# a=""
# while i>=len(s):
#     a+=s[len(s)-i-1]
#     print(a)
#     # print(s)
#     i+=1
# if a==s:
#     print("It is palindrom")
# else:
#     print("not a palindrom")

# s=input()
# i=len(s)
# a=""
# while i>=1:
#     a+=s[i-1]
#     print(a)
#     i-=1
# if a==s:
#     print("it is palindrome")
# else:
#     print("NOt a palibrome")


# s=int(input())
# b=str(s)
# i=len(b)
# a=""
# while i>=1:
#     a+=b[i-1]
#     i-=1
# print(int(a))


# s=input()
# n=len(s)
# ans=""
# while n>0:
#     ans+=s[n-1]
#     n-=1
#     # print(s[n-1])
# print(ans)

# n=153
# print(a)

# num=int(input())
# ans=0
# n=len(str(num))
# # n=len(num)
# n1=0
# while n>0:
#     ans=num%10
#     a=ans*10+
#     n1=num//10
#     print(ans,n1)
#     n-=1
# # print(ans,n)

# n=int(input())
# # ans=0
# revers=0
# n1=len(str(n))
# for i in range(n1):
#     ans=n%10
#     revers=revers*10+ans
#     # b=ans *10+
#     n=n//10
# print(revers)




# s=input()
# i=len(s)
# a=""
# while i>=1:
#     a+=s[i-1]
#     # print(a)
#     i-=1
# if a==s:
#     print("it is palindrome")
# else:
#     print("NOt a palibrome")

# n=int(input())
# ans=0
# for i in range(len(str(n))):
#     idgit=n%10
#     ans=ans*10+idgit
#     n=n//10
# print(ans)


# s=input()
# i=len(s)
# a=""
# while i>=1:
#     a+=s[i-1]
#     # print(a)
#     i-=1
# if a==s:
#     print("it is palindrome")
# else:
#     print("NOt a palibrome")


# n=int(input())
# ans=0
# while n>0:
#     digit=n%10
#     ans=ans*10+digit
#     n=n//10
# print(ans)


# n=int(input())
# ans=0
# b=len(str(n))
# while n>0:
#     digit=n%10
#     ans=digit**b+ans
#     n=n//10
#     print(ans)
    







# n=int(input())
# ans=0
# while n>0:
#     digit=n%10
#     ans=ans*10+digit 
#     n=n//10
# print(ans)


# n=int(input())
# ans=0
# b=len(str(n))
# while n>0:
#     digit=n%10
#     ans=digit ** b+ans
#     n=n//10
# print(ans)


# str1="madam"
# palindrom=True
# for i in range(len(str1)//2):
#     if str1[i]!=str1[-(i+1)]:
#         palindrom=False
#         break
    
# if palindrom:
#     print("It is a palindrom")
#         # break
# else:
#     print("it is not.palindrom")
#         # break




name,*line=input().split()
socres=list(map(floaat,line))
name,*line=input().split()
socres=list(map(float,line))
