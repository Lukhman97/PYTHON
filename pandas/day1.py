
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

# ab=pd.read_csv("ABCDEF.csv")
# print(ab)


# data={
#     'name':["lukhman","Virat","dhoni"],
#     'age':[23,36,42],
#     'city':['HYD',"Delhi","JK"],
# }

# ab=pd.DataFrame(data)

# a=ab.to_csv("ABCDEF.csv",index=False)
# print(a)

# ab=pd.read_csv("ABCDEF.csv")
# print(ab.head(n=10))
# print(ab.tail(n=10))
# print(ab.info)
# print(ab.info())
# print(ab.describe())
# print(ab.shape)
# print(ab.columns)
# print(ab.index)
# print(ab.dtypes)
# print(ab.loc[0,["DeliveryDays","ProductName","Category"]])
# print(ab.iloc[199,1])
# print(ab.at[0,"Category"])
# print(ab.iat[0,1])
# print(ab.get("Category"))
# print(data.get("name"))

# # print(ab.query('OrderID >1150 and Price>1500'))
# filter1=ab[ab["DeliveryDays"]>=8]
# print(filter1)


# filter1=ab[(ab["DeliveryDays"]>=8) & (ab["Price"]>1500)]
# print(filter1)


# mask = ab.mask(data['age'] < 28)
# print(data[mask])

# a=data[(data['age']>20) & (data['city']=='HYD')]
# print(a)
# # import pandas as pd
# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [22, 30, 35, 28],
#     'City': ['NY', 'LA', 'NY', 'SF']
# })

# # Filter people older than 25 and in NY
# result = df[(df['Age'] > 25) & (df['City'] == 'NY')]
# print(result)



# a=df[(df['Age'] > 25) & (df['City'] == 'NY')]
# print(a)

# a=ab[ab["CustomerName"].isin(["Customer_3","Customer_14"])]
# print(a)

# a=ab[ab['DeliveryDays'].between(4,7)]
# print(a)

# a=ab[ab['DeliveryDays'].notnull()]
# print(a)


# a=ab[ab['DeliveryDays'].isnull()]
# print(a)


# a=ab.dropna(axis=1,how="any",thresh=None,subset=None,inplace=False)
# print(a)

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', None],
#     'Age': [25, None, 35, None],
#     'City': ['NY', 'LA', None, None]
# }

# df = pd.DataFrame(data)
# a=df.dropna(axis=0,how="any")
# print(a)

# df=pd.DataFrame(data)
# df=pd.DataFrame(ab)
# a=df.fillna(value=2,method=None,inplace=False)
# print(a)


# df=pd.DataFrame(data)
# # a=df.replace(to_replace="NY",value="KY")
# # print(a)

# ab=pd.read_csv("ABCDEF.csv")
# a=ab.drop_duplicates(subset=None)
# print(a)
# a=df.drop_duplicates(subset=None)
# print(a)


# a=10
# b=20
# print(a+b)
# if a:
# print(b)

# def add(*a,**b):
#     print(a)
#     print(b)
# # add(12,33,4,55,563,323,222,name="lukhman",'age':23,"height":5.9,'rollno':343)
# add(12,33,4,55,563,323,222,name="lukhmna", age=23, height=5.9, rollno=343)

# a=lambda x:x+100
# print(a(10))
# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# fact(6)

# file=open("ABCDEF.csv","a+")
# file.write("Lukhman shaik")
# file.close()

# file=open("ABCDEF.csv","r")
# a=file.read()
# print(a)
# import json

# # Write JSON
# with open("data.json", "w") as f:
#     json.dump(data, f)

# # Read JSON
# with open("data.json", "r") as f:
#     result = json.load(f)
#     print(result)

# 
# 
# class BANKACCOUNT:
#     def __init__(self,balance):
#         self.__balance=balance

#     def deposit(self,amount):
#         self.amount=amount
#         print(f"deposited amount is {self.amount}.Total balance is {self.amount+self.__balance}")
#     def get_balance(self):
#         print(f"You balance is {self.amount+self.__balance} ")
# ob=BANKACCOUNT(20000)
# ob.deposit(10000)
# ob.get_balance()


# import threading

# def print_numer():
#     for i in range(1,5):
#         print(i)

# t1=threading.Thread(target=print_numer)
# t2=threading.Thread(target=print_numer)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# import threading

# def print_numbers():
#     for i in range(1,5):
#         print(i)

# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_numbers)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# from multiprocessing import Process

# def print_numbers():
#     for i in range(5):
#         print(i)

# p1 = Process(target=print_numbers)
# p2 = Process(target=print_numbers)
# if __name__ == "__main__":


#         p1.start()
#         p2.start()

#         p1.join()
#         p2.join()