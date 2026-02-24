# amount=7500
# money=[5000,2000,1000,500,200,100,50,20,10,5,2,1]
# d={}
# for i in money:
#     # while amount>=0:
#         if amount>i:
#             digit=amount%i
#             d[i]=1
#         amount=digit%i
#         print(amount)
# print(d)

# # print(2500%2000)



# amount=7651
# money=[5000,2000,1000,500,200,100,50,20,10,5,2,1]
# d={}
# for i in money:
#     if amount>=i:
#         value=amount//i
#         d[i]=value
#         amount=amount%i

# print(d)


# Output: {200: 3, 100: 1, 50: 1}
# Tank needs 750L of water. You have containers of sizes 200L, 100L, 50L. Find the minimum number of containers.


# needs=750
# sizes=[200,100,50]
# d={}
# for i in sizes:
#     if needs>=i:
#         # print(i)

#         count=needs//i
#         d[i]=count
#         needs=needs%i
#         # print(needs)
# print(d)

# n1      = "111"  #7
# n2      = "100"  #4
# c        = 0
# k        = 0
# sum   = 0
# for i in range(len(n1)-1,-1,-1):
#     sum += int(n1[i])*(2c)
#     c+=1
# for i in range(len(n2)-1,-1,-1):
#     sum += int(n2[i])*(2k)
#     k+=1
# print(str(bin(sum)[2:]))


# s = input("Enter :")
# res = s[0]
# c = 1
# for i in range(1,len(s)) :
#     if s[i] == s[i-1] :
#         c+=1
#         if c < 3:
#             res+=s[i]
#     else:
#         c =1
#         res+=s[i]        
# print(res)

# n = int(input("enter :"))
# total = n 
# w = n
# while w >= 3 :
#     e = w//3
#     total+=e
#     w = e+w%3
# print(total)



# n1      = "111"  #7
# n2      = "100"  #4
# c        = 0
# k        = 0
# sum   = 0
# for i in range(len(n1)-1,-1,-1):
#     sum += int(n1[i])*(2c)
#     c+=1
# for i in range(len(n2)-1,-1,-1):
#     sum += int(n2[i])*(2k)
#     k+=1
# print(str(bin(sum)[2:]))


# s = input("Enter :")
# res = s[0]
# c = 1
# for i in range(1,len(s)) :
#     if s[i] == s[i-1] :
#         c+=1
#         if c < 3:
#             res+=s[i]
#     else:
#         c =1
#         res+=s[i]        
# print(res)

# n = int(input("enter :"))
# total = n 
# w = n
# while w >= 3 :
#     e = w//3
#     total+=e
#     w = e+w%3
# print(total)


# n1      = "111"  #7
# n2      = "100"  #4
# c        = 0
# k        = 0
# sum   = 0
# for i in range(len(n1)-1,-1,-1):
#     sum += int(n1[i])*(2c)
#     c+=1
# for i in range(len(n2)-1,-1,-1):
#     sum += int(n2[i])*(2k)
#     k+=1
# print(str(bin(sum)[2:]))


# s = input("Enter :")
# res = s[0]
# c = 1
# for i in range(1,len(s)) :
#     if s[i] == s[i-1] :
#         c+=1
#         if c < 3:
#             res+=s[i]
#     else:
#         c =1
#         res+=s[i]        
# print(res)

# n = int(input("enter :"))
# total = n 
# w = n
# while w >= 3 :
#     e = w//3
#     total+=e
#     w = e+w%3
# print(total)



# n1      = "111"  #7
# n2      = "100"  #4
# c        = 0
# k        = 0
# sum   = 0
# for i in range(len(n1)-1,-1,-1):
#     sum += int(n1[i])*(2c)
#     c+=1
# for i in range(len(n2)-1,-1,-1):
#     sum += int(n2[i])*(2k)
#     k+=1
# print(str(bin(sum)[2:]))


# s = input("Enter :")
# res = s[0]
# c = 1
# for i in range(1,len(s)) :
#     if s[i] == s[i-1] :
#         c+=1
#         if c < 3:
#             res+=s[i]
#     else:
#         c =1
#         res+=s[i]        
# print(res)



# n1      = "111"  #7
# n2      = "100"  #4
# c        = 0
# k        = 0
# sum   = 0
# for i in range(len(n1)-1,-1,-1):
#     sum += int(n1[i])*(2c)
#     c+=1
# for i in range(len(n2)-1,-1,-1):
#     sum += int(n2[i])*(2k)
#     k+=1
# print(str(bin(sum)[2:]))


# s = input("Enter :")
# res = s[0]
# c = 1
# for i in range(1,len(s)) :
#     if s[i] == s[i-1] :
#         c+=1
#         if c < 3:
#             res+=s[i]
#     else:
#         c =1
#         res+=s[i]        
# print(res)



# s=" aaabbbbccddddd"
# # Input:  aaabbbbccddddd  
# # Output: aabbccdd

# rev=s[0]
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c+=1
#         if c<3:
#             rev+=s[i]
#     else:
#         c=1
#         rev+=s[i]
# print(rev)



# Input:  aaabbc  
# Output: a3b2c1


# s="aaabbc"
# rev=s[0]
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c+=1
#         if c<=1:
#             rev+=s[i]
#     else:
#         c=1
#         rev+=s[i]
# print(rev)
    

# s="aaabbc"
# rev=s[0]
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i]:
#         c+=1
#         rev+=""
#         if c>=2:
#             rev+=f"{c}"
#             # rev+=f"{s[i]}{c}"
#     else:
#         c=1
#         rev+=f"{c}"
#         # rev+=f"{s[i]}{c}"
# print(rev)




# s = input("Enter string: ")
# res = ""
# count = 1
# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         count += 1
#     else:
#         res += s[i-1] + str(count)
#         count = 1
# res += s[-1] + str(count)
# print(res)



# s="aaaaaabbbbbbbbbc"
# rev=""
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c+=1
#     else:
#         # c=1
#         rev+=s[i-1]+f'{c}'
#         c=1
# rev+=s[-1]+f'{c}'
# print(rev)



# # Input:  aaabbcdd  
# # Output: bc

# s="aaabbcdd"


# Input:  a2b3  
# Output: aabbb

# s="a2b3c7"
# a=""
# for i in range(0,len(s),2):
#     a+=s[i]*int(s[i+1])
# print(a)
    
# s="aaabbbcde"
# rev=""
# c=1
# i=0
# while i<len(s):
#     c=1
#     while  i+1 <len(s) and s[i]==s[i+1]:
#         c+=1
#         i+=1
#     if c==1:
#         rev+=s[i]
#         # c=1
#     i+=1
# print(rev)
        
# s="aaabbbcde"
# # s = input("Enter string: ")
# res = s[0]

# for i in range(1, len(s)):
#     if s[i] != s[i - 1]:
#         res += s[i]

# print("Output:", res)


# s="aaabccddeee"
# rev=[]
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c+=1
#     else:
#         rev.append((s[i-1],c))
#         c=1
# rev.append((s[-1],c))
# print(rev)



# print(5*(5+1)//2)


# s = input("Enter string: ")


# res= []
# count = 1
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         res.append((s[i - 1], count))
#         count = 1
# res.append((s[-1], count))
# print("Output:", res)




# class Father:
#     def __init__(self, fname, fasset):
#         self.fname = fname
#         self.fasset = fasset

#     def show_assets(self):
#         print(f"Father: {self.fname}, Assets: ₹{self.fasset}")


# class Child(Father):
#     def __init__(self, name, asset, fname, fasset):
#         super().__init__(fname, fasset)
#         self.child_name = name
#         self.child_asset = asset

#     def show_assets(self):
#         super().show_assets()
#         print(f"Child: {self.child_name}, Assets: ₹{self.child_asset}")


# class GrandChild(Child):
#     def __init__(self, name, asset, child_name, child_asset, fname, fasset):
#         super().__init__(child_name, child_asset, fname, fasset)
#         self.grandchild_name = name
#         self.grandchild_asset = asset

#     def show_assets(self):
#         super().show_assets()
#         print(f"Grandchild: {self.grandchild_name}, Assets: ₹{self.grandchild_asset}")

#     def total_family_assets(self):
#         total = self.fasset + self.child_asset + self.grandchild_asset
#         print(f"\nTotal assets of 3 generations: ₹{total}")


# # --- Example Usage ---
# g = GrandChild("Aryan", 20000, "Ravi", 50000, "Shankar", 100000)
# g.show_assets()
# g.total_family_assets()





# print(0 and 1 or 2 and 3)

# 🔢 2.


# print(not 0 or not 1)

# 🔢 3.


# print('a' in 'apple' and 'e' in 'tree')

# 🔢 4.


# print('py' in 'python' and 'on' in 'python')

# 🔢 5.


# print(5 and [] or "Done")

# 🔢 6.


# print(' ' in 'hello world')

# 🔢 7.

# x = 'a'
# print(x in ['A', 'a', 'b'])

# 🔢 8.


# print(not ('' in 'hello'))

# 🔢 9.


# print(0 or [] or {} or None or "Python")

# 🔢 10.


# print(not True and not False or False)

# 🔢 11.


# print('o' not in 'hello' or 'z' not in 'zebra')

# 🔢 12.


# print("on" in "python" and "py" not in "python")

# 🔢 13.


# x = []
# print(x in [[], (), {}])

# 🔢 14.


# print([] == [] and [] is [])

# 🔢 15.

# print('a' in ['apple', 'banana', 'grapes'])
# val = [100]
# for i in val:
#     val.append(i + 1)
#     if i > 102:
#         break
# print(val)




# data = [1, 2, 3]
# # print(data + data * 2)


# class A:
#     def __init__(self, val):
#         self.val = val
#     def show(self):
#         print("A:", self.val)

# class B(A):
#     def show(self):
#         print("B:", self.val)

# class C(A):
#     def show(self):
#         print("C:", self.val)

# class D(B, C):  # Multiple Inheritance
#     pass

# d = D(50,30)
# d.show()

# 4



# li=[1,2,3,4]
# # for i in range(len(li)-1):

# li[-2],li[-1]=li[0],li[1]
# print(li)




# list1 = [1, 2, 3, 4, 5, 6]  # Example list

# # if len(list1) > 5:
#     # Move last two elements to the front
# print(list1[-2:])
# print(list1[:-2])
# list1 = list1[-2:] + list1[:-2]

# print(list1)



# n=7
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ",end="")
#     for j in range(0,i):
#         print(i,end=" ")
#     print()


