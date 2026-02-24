# # pandas is used to data manipulation and data analysis it a python liberrary
# # pandas module mainly works with the tabular data in the from of tables with rows and columns
# # pandas is capabile of offering in-memory 2d table objects called datframes it means i will store the data in main memeory not in the desk top in the form form of 2d table objects called dataframes

# # there are mainly three types of pandas data structures
# # 1.series------------------1dimensional----singlecolumn data
# # 2.dataframes---------------2dimensional---->tabiel---rows and colums
# # 3.pannel-------------------3dimensioanl-----same 2

# # pip install pandas----installaations


# # /*conform to delcare
# import pandas as pd  


# # print(pd.__version__)  # checking version

# # s={'name':"lUkhman",'age':23,'height':6,'city':"hyd"}
# # a=pd.Series(s.values(),index=['a','b','c','d'])
# # print(a)

# # df=pd.read_csv("online_shoppers_intention.csv")
# # print(df)




import pandas as pd

data={
    'name':["lukhman","Virat","dhoni"],
    'age':[23,36,42],
    'city':['HYD',"Delhi","JK"],
}
df=pd.DataFrame(data)
print(df)