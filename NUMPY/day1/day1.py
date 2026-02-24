# import numpy as nu

# x=nu.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# y=nu.array(["hai"])

# # print(type(x))

# # print(nu.ndim(x))
# # print(nu.shape(x))
# # print(nu.size(x))

# # print(x.dtype)

# print(y.dtype)



# a="aaaabbbccccc"
# s=""
# c=1
# for i in range(1,len(a)):
#     if a[i-1]==a[i]:
#         c+=1
#     else:
#         s+=a[i-1]+f"{c}"
#         c=1
# s+=a[i-1]+f"{c}"
# print(s)



import numpy as np

# array1=[1,33,55,56,78,2,3,4,5,6,7,8,9,10,11,12]
# a=np.reshape(array1,(4,4))
# print(a)

# arr = np.arange(8)
# new_arr = arr.reshape(2, 2, 3)
# print(new_arr)

# arr=[[12,3,5,6,7,8],[12,34,56,78,45,99]]
# a=np.array(arr).flatten()
# print(a)


# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])

# arr3=np.concatenate((arr1,arr2))
# print(arr3)


# arr1=np.array([1,2,3,4,5,6,7,8])
# a=np.where(arr1%2==1)
# print(a)

# arr1=np.array([1,2,3,3,4,5,6,7,8,8,9,9,9])
# a=np.unique(arr1)
# print(a)

# arr1=np.array([5,10,15,20,25,30,35])
# b=np.clip(arr1,1,20)
# print(np.unique(b))


# a=np.dot([1,2],[3,4])
# print(a)

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# # c=np.dot(a,b)
# # print(c)


# d=np.transpose(b)
# print(d)

# arr1=np.random.rand(3,2)
# print(arr1)

# arr1=np.random.rand(1,4)
# print(arr1)

# arr1=np.random.randint(1,100,size=4)
# print(arr1)


# arr1=np.random.randn(10)
# print(arr1)


# arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])

# a=arr1.shape
# print(a)

# b=arr1.ndim
# print(b)

# c=arr1.size
# print(c)


# from numpy.linalg import inv

# a=inv([[1,2],[3,4]])
# print(a)

# import numpy as np
# a=np.zeros((3,4),dtype=int)
# print(a)

# import numpy as np
# a=np.random.randint(10,50,5)
# print(a)

# arr = np.arange(12)
# b=arr.reshape(3,4)
# print(b)

# import pandas as pd
# s=pd.Series([10,20,30,40])
# print(s)
# s=pd.Series([10,20,30,40],index=['a','b','c','d'])
# print(s)

import pandas as pd


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['NY', 'LA', 'SF']
# }

# data={
#     'name':["lukhman","Virat","dhoni"],
#     'age':[23,36,42],
#     'city':['HYD',"Delhi","JK"],
# }

# df=pd.DataFrame(data,index=['a','b','c'])
# print(df)

ab=pd.read_excel("Ecommerce_Messy_Dataset.xlsx")
print(ab.to_string())