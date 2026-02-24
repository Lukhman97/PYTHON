# str=input()
# l=[]
# d=""

# for i in str:
#     a=ord(i)
#     l.append(a)
#     b=sorted(l)
#     if d==' ':
#         print("_")
# for j in b:
#     c=chr(j)
#     d+=c
# print(d,end="")




# #simple intrest
# p=int(input("Enter principle values :"))
# t=int(input("Enter time values :"))
# r=int(input("Enter rate of intrest values :"))
# simple_intrest = (p*t*r)/100
# print(f"simple_intrest:{simple_intrest}")

# #Temperature Conversion from c to f
# c = int(input("Enter °c values"))
# f = (c*(9/5))+32
# print(f"{c}°c is equal to {f}°f")

# #Average of Three Numbers
# v1,v2,v3 = map(int,input("Enter 3 valus :").split())
# average = (v1+v2+v3)/3
# print(f"Average of Three Numbers is {average}")

# #Area of the circle
# r = int(input("Enter radius :"))
# area = 3.14 * (r**2)
# print(f"Area of the cricle is {area}")


# s=input()
# n=len(s)//2
# m=len(s)
# valid=True
# for i in range(n+1):
#     l=s[i]
#     r=s[m-1-i]
#     if l!=r:
#         valid=False
# if valid:
#     print("Yes")
# else:
# #     print("No") 

# s=[1,2,3,4,5,6]
# n=3
# m=n*2
# for i in range(n):
#     l=s[i]
#     r=s[-1-i]
#     print(l,r)


# def table(n):
#     for i in range(1,11):
#         print(str(n)+"*"+str(i)+"="+str(n*i))
# table(5)