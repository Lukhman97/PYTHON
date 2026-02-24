nums = [0,2,3,4,6,8,9]
a=[]
for i in range(len(nums)-1):
    if i!=nums[i]:
        a.append(f"{nums[i-1]}"+"->")
print(a)

