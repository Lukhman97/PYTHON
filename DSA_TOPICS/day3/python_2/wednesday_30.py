# num=int(input("Enter the number: "))
# num1=num
# num2=num
# c=0
# while num>0:
#     digit=num%10
#     c+=1
#     num=num//10
# sum=0
# while num1>0:
#     digit1=num1%10
#     sum+=digit1**c
#     num1=num1//10
# print(sum)
# if num2==sum:
#     print("It is amstrong number")
# else:
#     print("it is niot an amstrong numbetr")



# def is_amstrong(num):
#     num1=num
#     num2=num
#     # count=0
#     sum=0
#     # c=len(str(num))
#     while num>0:
#         digit=num%10
#         sum=digit**len(str(num1))+sum
#         num=num//10
#     # print(sum)
#     if num1==sum:
#         return True
#     else:
#         return False
    
# op=[i for i in range(0,1000000) if is_amstrong(i)]
# print(op)



# def is_prime(num):
#     num1=num
#     isprime=True
#     if num<=1:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# start=int(input())
# end=int(input())
# op=[i for i in range(start,end+1) if is_prime(i)]
# print(op[:5])


# def fibba(num):
#     num1=num
#     is_fibbi=True
#     a=0
#     b=1
#     for i in range(num):
#         print(a,end=" ")
#         # a,b=b,a+b
#         temp=a+b
#         a=b
#         b=temp
# num=int(input())
# fibba(num)    


# num=1234
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum*10+digit
#     num=num//10
# print(sum)




# num=100
# a=0
# b=1
# while a<num:
#     print(a,end=" ")
#     a,b=b,a+b


# val=[100]
# for i in val:
#     val.append(i+1)
#     if i>102:
#         break
# print(val)


# student = {
#     "name": "Lukhman",
#     "age": 21,
#     "course": "Python",
#     "marks": 87,
#     "passed": True
# }
# for keys in student.values():


    # print(keys)



# n=int(input("enter the number of i puts:"))
# dict={}
# for i in range(n):
#     key=(input())
#     value=float(input())
#     dict[key]=value
# print(dict)


# n=int(input("enter the number of i puts:"))
# dict=[]
# for i in range(n):
#     key=(input())
#     value=float(input())
#     dict.append(tuple([key,value]))
# print(dict)

# dicti= {
#     "name": "Lukhman",
#     "age": 21,
#     "course": "Python",
#     "marks": 87,
#     "passed": True
# }

# dicti["name"]="kinguuu"
# dicti["age"]=27
# del dicti["name"]
# dicti.pop("age")
# dicti.clear()
# for keys,values in dicti.keys:
#     print(keys,values)


# def is_strong(num):
#     sum1=0
#     while num>0:
#         digit=num%10
#         # sum+=digit
#         # num=num//10
#         i=1
#         fact=1
#         while i<=digit:
#             fact=fact*i
#             i+=1
#         sum1+=fact
#         num=num//10
#     print(sum1)
# num=int(input())
# is_strong(num)



# num=int(input())
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# print(sum," si")


# n=int(input())
# a=n*n
# sum=0
# while a>0:
#     dogit=a%10
#     sum+=dogit
#     a=a//10
# print(sum)


# for i in range(1,11):
#     exp=f"10 x {i}={10*i}"
#     modified=exp.replace("0","*")
#     print(modified)


# n='ABCE'
# for i in range(len(n)):
#     print(chr(ord(n[i])+32),end="")


# n="abcdef"
# b=''
# for i in n:
#     a=chr(ord(i)-32)
#     print(a)
# #     b+=a
# # print(b)


# a="AlukhmanL"
# b=""
# for i in a:
#     if i>="A" and i<="Z":
#         b+=chr(ord(i)+32)
#     else:
#         b+=i
# print(b)



# a="aaaabbbbbbccccdddddd"

# rev=""
# c=1
# # i=1
# for i in range(1,len(a)):
#     if a[i]==a[i-1]:
#         c+=1
#         if c>=3:
#             rev+=""

#     else:
#         rev+=a[i+1]
#         c=1
# # rev+=a[-1]
# print(rev)

    

# a = "aabbbbbbccccdddddd"

# rev = ""
# c = 1

# for i in range(1, len(a)):
#     if a[i] == a[i - 1]:
#         c += 1
#     else:
#         if c >= 3:
#             rev += a[i - 1] *3
#         c = 1
# # Handle last group
# if c >= 3:
#     rev += a[-1] *3

# print(rev)


# n=16
# a=int(n**0.5)
# if a*a==n:
#     print("it is a prefevcty")
# else:
#     print("not perfect")




# a=[2,4,8,99,3,46,66,777]/
# maxvale=a[0]
# for i in range(1,len(a)):
#     if maxvale<a[i]:
#         maxvale=a[i]
# print(maxvale)


# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j]<a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)



