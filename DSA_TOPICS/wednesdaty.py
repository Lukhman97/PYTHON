# nums = [3,2,2,3]
# val = 3
# nums = [0,1,2,2,3,0,4,2]
# ls=[]
# val = 2
# # n=len(nums)
# # count=0
# # for i in nums:
# #     # if i==val:
# #     #     count+=1
# #     if i!=val: 
# #         ls.append(i)
# # print(ls)
# k = 0
# for i in range(len(nums)):
#     if nums[i] != val:
#         nums[k] = nums[i]
#         k += 1
# print(k)



# arr=[4,3,2,1]
# arr=[9]
# ab=[]
# c=[str(i) for i in arr]
# b=''.join(c)
# k=str(int(b)+1)
# for i in k:
#     ab.append(int(i))
# print(ab)



# # nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3
# nums1=[1,2,3,0,0,0]
# m=3
# nums2=[2,5,6]
# n=3


# nums1=[0]
# m=0
# nums2=[1]
# n=1
# nums1=nums1[:m]
# print(nums1)
# for i in nums1[:m]:
#     if nums1[i]==0:
#         nums1.remove(nums1[i])
# for i in nums2:
#     nums1.append(i)
# for i in range(len(nums1)):
#     for j in range(len(nums1)-1):
#         if nums1[j]>nums1[j+1]:
#             nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
# nums1=[1,2,3,0,0,0]
# m=3
# nums2=[2,5,6]
# n=3
# nums1[:m]
# nums1.extend(nums2)

# nums1.sort()
# print(nums1)

# nums1=[1,2,3,0,0,0]
# m=3
# nums2=[2,5,6]
# n=3
# i=m-1
# j=n-1
# k=m+n-1
# while j>=0:
#     if i>=0 and nums1[i]>nums2[j]:
#         nums1[k]=nums1[i]
#         i-=1
#     else:
#         nums1[k]=nums2[j]
#         j-=1
#     k-=1
# print(nums1)

# a=10
# b=20
# print(a<b)


# # s = "A man, a plan, a canal: Panama"
# s="madam"
# ab=""
# for i in s:
#     if i>="A" and i<="Z" or i>="a" and i<="z":
# #         ab+=i
# l=0
# # r=len(ab)
# s="madam"
# is_pal=True
# for i in range(len(s)-1,-1,-1):
#     if l!=s[i]:
#         is_pal=False
#     l+=1
# if is_pal:
#     print("true")
# else:
#     print("False")


# s="madam"


# sk = "0p"
# # s="madam"
# ab=""
# for i in sk:
#     if i>="A" and i<="Z" or i>="a" and i<="z":
#         ab+=i
# s=ab.lower()
# l=0
# r=len(s)-1
# is_pal=False
# if s[l]==s[r]:
#     is_pal=True
#     l+=1
#     r-=1
# print(is_pal)



# x=-121
# ab=str(x)
# print(ab)
# s=ab[::-1]
# # print(s)
# if s==ab:
#     print("TRUE")
# else:
#     print("False")



# nums=[3,0,1]
# nums=[0,1,2]
# nums=[9,6,4,2,3,5,7,0,1]
# nums=[3,19,22,43,24,2,12,32,30,45,21,23,42,31,37,14,25,8,13,20,5,40,41,18,17,47,15,10,33,34,0,44,11,6,48,7,35,27,4,26,39,38,1,16,36,28,9,46,29]
# maxval=nums[0]
# for i in range(len(nums)):
#     if nums[i]>maxval:
#         maxval=nums[i]
# # print(maxval)
# if len(nums)%2==1 or maxval <=2:
#     for i in range(maxval+2):
    
#         if i not in nums:
#             print(i)
# else:
#     for i in range(maxval+1):
        
#         if i not in nums:
#             print(i)