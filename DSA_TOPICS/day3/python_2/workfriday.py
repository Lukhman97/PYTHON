# 1. Add all elements of a list.

list1=[2,6,5,4,7,8,3,9,1,2,3,9]
sum=0
for i in list1:
    sum+=i
print(sum)

# 2. Find max and min in a list.
list1=[22,4,44,66,77,55,1,33]
minval=list1[0]
for i in range(len(list1)):
    if minval>list1[i]:
        minval=list1[i]
print(minval)

list1=[22,4,44,66,77,55,1,33,11111]
maxval=list1[0]
for i in range(len(list1)):
    if maxval<list1[i]:
        maxval=list1[i]
print(maxval)


# 3. Count even and odd numbers in a list.

list1=[22,4,44,66,77,55,1,33,11111]
count1=0
count2=0
for i in list1:
    if i%2==0:
        count1+=1
    else:
        count2+=1
print(f"Even count is {count1} and Odd count is {count2}")


# 4. Reverse a list without using reverse().

list1=[22,4,44,66,77,55,1,33,11111]
a=[]
for i in range(len(list1)-1,-1,-1):
    a.append(list1[i])
print(a)
    

# 5. Remove duplicates from list.
list1=[22,44,44,66,55,55,1,22,1,1,1,1,1,1,1,1,1,33,11111]
a=[]
for i in list1:
    if i  not in a:
        a.append(i)
print(a)

# 6. Sort a list of strings by length.
list1=["lukhmana","virat","hai","josheph","dhonia"]
dicti={}
a=[]
for i in range(len(list1)):
    dicti[list1[i]]=len(list1[i])
    b=sorted(dicti.values())
for length in b:
    for key in dicti:
        if dicti[key] == length :
#             a.append(key)
# print(dicti)
# print(b)
print(a)




# 7. Find the second largest number in the list.
list1=[22,44,44,66,55,55,1,22,1,1,1,1,1,1,1,1,1,33,11111]
# a=sorted(list1)
# print(a)
for i in range(len(list1)):
    for j in range(0,len(list1)-1-i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1[-2])
# 8. Find sum of all nested list elements.
sum=0
list1=[[2,5,8,4],[2,4,3,9],[6,8,3,7]]
for i in list1:
    for j in i:

        sum+=j
print(sum)

# 9. Check if two lists are equal.
list1=[1,2,3,4,5]
list2=[1,2,3,4,5,6]
if list1==list2:
    print("Equal")
else:
    print("not equal")


# 10. Merge two lists and sort them.
list1=[2,5,6,7,9]
list2=[9,6,7,22 ,3,444,555,666,777,88,6666]
a=list1+list2
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

# 11. Convert tuple to list and back.
t = (4, 5, 6)
lst = list(t)      # Tuple → List
t = tuple(lst)
print(lst)
print(t)  # List → Tuple



# 12. Check if the tuple contains a value.

t=(1,2,3,4,5,6)
if 2 in t:
    print("Yes it is there")

# 13. Unpack a tuple into variables
t=(1,2,3,4,54,6)
a,b,c,d,e,f=t
print(a,b,c,d,e,f)


# 14. Create a list of squares using comprehension.

op=[x*x for x in range(1,20)]
print(op)

# 15. Count how many times a number appears in a list.
list1=list(map(int,input().split()))
n=int(input("Enter the number: "))
c=0
for i in list1:
    if n==i:
        c+=1
print(c)


# 16. Find index of element in tuple.

t=(22,33,444,55,66,6677,777)
# for i in range(len(t)):
a=t.index(55)
print(a)



# 17. Slice a tuple from index 1 to 3.
t=(22,33,444,55,66,6677,777)
a=t[1:3]
print(a)

# 18. Replace element in list with another.
li=[22,33,444,55,66,6677,777]
li[0]=222
print(li)


# 19. Filter only strings from mixed lists.


list1=["lukhman","king","hero",1,3,5,7,8,9,9,99]
for i in list1:
    if i not in range(0,10*20):
        print(i)



# 20. Take input of the list from the user and print sum.

list1=list(map(int,input().split()))
sum=0
for i in list1:
    sum+=i

print(sum)

