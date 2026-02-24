# sa = "3[a]2[bc]"
# s=sa.replace("[","").replace("]","")
# ab=""
# for i in range(len(s)):
#     if s[i].isalpha():
#         for s[i] in range(int(s[i-1])):
#             ab+=s[i]
# print(ab)



# s = "Hello World"
# a=s.split()
# print(len(a[-1]))

# s = ["h","e","l","l","o"]
# l=0
# r=len(s)-1
# while l<r:
#     s[l],s[r]=s[r],s[l]
#     l+=1
#     r-=1
# print(s)

# arr=[10,20,30,40,50]
# n=len(arr)
# pos=2
# arr.append(0)
# # arr[n]=arr[n-1]
# # arr[n-1]=arr[n-2]
# # arr[n-2]=arr[n-3]
# # arr[2]=25
# for i in range(n,pos,-1):
#     arr[i]=arr[i-1]
# arr[2]=25
# print(arr)

# arr=[10,20,25,30,40,50]
# pos=1
# for i in range(pos,len(arr)-1):
#     arr[i]=arr[i+1]
# arr.pop()
# print(arr)



# arr=[2,4,6,8,10]
# n=len(arr)
# # p=[0]*n
# # p[0]=arr[0]
# for i in range(1,n):
#     # p[i]=p[i-1]+arr[i]
#     arr[i]=arr[i]+arr[i-1]
#     print(arr)


# li=[5,9,1,8,7]
# n=len(li)
# l=0
# temp=0
# for i in range(n):
#     temp+=li[i]
#     if i-l+1==4:
#         temp-=li[l]
#         l+=1

#     if i-l+1==3:
#         print(temp)


# arr=[5,7,9,4,6,3]
# n=len(arr)
# l=0
# temp=0
# ans=0
# for i in range(n):
#     temp+=arr[i]
#     if i-l+1==4:
#         temp-=arr[l]
#         l+=1

#     if i-l+1==3:
#         ans=max(ans,temp)
# print(ans)


arr=[1, 2, 3, 4, 6]
target=6
l=0
r=len(arr)-1
while l<r:
    s=arr[l]+arr[r]
    if s==target:
        print(arr[l],arr[r])
        break
    elif s<target:
        l+=1
    else:
        r-=1
