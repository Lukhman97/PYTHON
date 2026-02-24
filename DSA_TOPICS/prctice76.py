arr=[23,2,4,66,88,99,44444444,5555222,44444,66666,3333]
f=s=t=fo=float("-inf")
for i in arr:   #23,2
    if i>f:
        fo=t   
        t=s  #23>-inf,2>23
        s=f #23
        f=i
           #23
    elif i !=f and i>s: #
        fo=t
        t=s
        s=i
    elif i!=f and i!=s and i>t:
        fo=t
        t=i  
    elif  i!=f and i!=s and i!=t and i>fo:#
        fo=i
print(fo)        #






# arr=[23,2,4,66,88,99,44444444,5555222,44444,66666,3333]
# f=s=t=fo=float("inf")
# for i in arr:   #23,2
#     if i<f:
#         fo=t   
#         t=s  #23>-inf,2>23
#         s=f #23
#         f=i
#            #23
#     elif i !=f and i<s: #
#         fo=t
#         t=s
#         s=i
#     elif i!=f and i!=s and i<t:
#         fo=t
#         t=i  
#     elif  i!=f and i!=s and i!=t and i<fo:#
#         fo=i
# print(fo)        #



# arr=[23,2,4,66,88,99,44444444,5555222,44444,66666,3333]
# f=s=t=fo=float("inf")
# for i in arr:   #23,2
#     if i<f:
#         # fo=t   
#         t=s  #23>-inf,2>23
#         s=f #23
#         f=i
#            #23
#     elif i !=f and i<s: #
#         # fo=t
#         t=s
#         s=i
#     elif i!=f and i!=s and i<t:
#         # fo=t
#         t=i  
#     # elif  i!=f and i!=s and i!=t and i<fo:#
#     #     fo=i
# print(t)        #


# s="MCMXCIV"
# total=0
# n=len(s)
# roman_map = {
#         'I': 1, 'V': 5, 'X': 10,
#         'L': 50, 'C': 100,
#         'D': 500, 'M': 1000
#     }
# for i in range(n):
#     if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
#         total -= roman_map[s[i]]
#     # print(i)
#     else:
#         total += roman_map[s[i]]
    
#         # return total
#         # print(i,end=" ")
# print(total)

# s=["flower","flow","flight"]
# # s=""
# for i in s:
#     for j in range(len(i)):
#         # print(i[j])
#         # if i[j] in s[i]:
#         #     print(i[j])
#         if i[j] in i:
#             s+=i[j]
#     print(s,end="")