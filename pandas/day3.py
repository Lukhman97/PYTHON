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




# import pandas as pd

# data={
#     'name':["lukhman","Virat","dhoni"],
#     'age':[23,36,42],
#     'city':['HYD',"Delhi","JK"],
# }


# df=pd.DataFrame(data,index = ['A', 'B', 'C'])

# print(df)

# import pandas as pd
# print(pd.__version__)
# print("Pandas loaded successfully!")



# import pandas as pd
# import json
# df=pd.read_excel('Employee_Data_200.xlsx',sheet_name=0)
# print(df['Name'])


# df=pd.read_csv("online_shoppers_intention.csv")
# print(df)

# df=pd.read_csv("online_shoppers_intention.csv")
# df.to_csv('ABCDEF111.csv',index=False)
# print(df)

# df=pd.read_csv("ABCDEF.csv")
# df.loc[0,'CustomerName'] = "Lukhman"
# print(df)


# df=pd.read_csv("online_shoppers_intention.csv")
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.dtypes)

# print(df.iloc[0,10])
# print(df.at[7,"Region"])
# print(df.get("Region"))

# print(df.isnull())

# print(df.dropna())




# ------------------------------------------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# import time

# start=time.time()
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# print(df)
# end=time.time()

# print(start-end)


# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# print(df.loc[1,'Exercise_Level'])

# print(df.iloc[0,17])

# print(df.at[1,'Exercise_Level'])

# print(df.iat[1,17])

# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")

# print(df.get('Exercise_Level'))

# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")

# print((df['age']>=20) &df['Exercise_Level']=='Low')

# print(df[df['age'].isin([20,23,25,30,35])])

# print(df[df['age'].between(20,30)])
# print(df[df['age'].between(20,50)])

# print(df['age'].notnull)





# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# print(df.dropna(axis=0,how="any"))

# print(df['age'].fillna(df['age'].mean()))
# print(df.fillna({'age':58,'name':'lukhman'}))

# print(df.replace({'User_1':"Lukhman","user1@example.com":'user786@mail'}))

# # print(df.drop_duplicates())
# print(df.duplicated())

# df['age']=df['age'].astype(int)

# print(df['age'].describe())


# print(df.rename(columns={'age':'Years'}, inplace=False))


# print(df['Years'].describe())

# print(df.apply(lambda x:x.strip() if isinstance(x,str) else x))

# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# print(df.sort_values(by ='age',ascending=False))
# print(df.sort_index(axis=1))
# df['rank']=df['age'].rank(ascending=False)
# print(df['rank'])




# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# print(df['age'].sum())

# print(df['age'].mean())

# print(df['age'].std())
# print(df['age'].count())
# print(df['age'].var())

# print(df['age'].min())
# print(df['age'].max())

# print(df.groupby('Exercise_Level')['age'].sum())

# print(df.agg({'age':['sum','mean']}))

# print(pd.pivot_table(df,values='age',index=['name'],columns=['user_id'],aggfunc='sum'))



# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# df1=pd.read_csv("ABCDEF.csv")
# print(pd.concat([df,df1],axis=0,ignore_index=True))

# print(pd.merge(df, df1, on='name', how='left'))
# print(df.join(df1))


# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# df1=pd.read_csv("ABCDEF.csv")

# print(df.pivot(index='name',columns='age',values='Blood_Pressure'))

# print(pd.melt(df,id_vars='age'))
# print(df.T)



# import pandas as pd
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# df1=pd.read_csv("ABCDEF.csv")
# print(df.set_index('age',inplace=False,drop=True))

# print(df.reset_index(level=None))

# print(df.reindex([3,2,1,0]))

# print(df.sort_index())


# ------

import pandas as pd
df=pd.read_csv("users_200_10cols_no_fk.csv")

# print(pd.to_datetime(df['last_login']))
# print(pd.to_datetime(df['age']))

# print(df.set_index('last_login'))

# print(df.resample('03').sum())

# print(df['age'].shift(4))

# print(df['age'].rolling(window=2).sum())
# print(df['age'].expanding().sum())

# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv("users_200_10cols_no_fk.csv")
# print(df)

# print(df['age'].apply(lambda x:x+1))
# print(df['city'].map({'India':'IND','USA':'UNITED ARAB'}))


# print(df.plot(x='name', y='age', kind='bar'))
# plt.show()

# # import pandas as pd
# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
# plt.title("Simple Plot")
# plt.show()


import pandas as pd
df=pd.read_csv("users_200_10cols_no_fk.csv")
# print(df['name'].str.upper())
# print(df['name'].str.lower())
print(df.to_string())




# --------------------------------------------------------------------
# 1.data creation----->(pd.DataFrame(),,,,pd.Series)
# 2.data input/output------>(pd.read_csv(),DataFrame.to_csv) same as ecel,and we should connct from sql server to it by importing mysqllite module,json() we should dumpu it
# 3.data inspection--->DataFrame.head()/DataFrame.tail()/DataFrame.descibe(),DataFrame.info(),DataFrame.shape,DataFrame..colums,DataFrame.dtypes,DataFrame.index,
# 4.selection and aceess--->loc[0,'name]---we can use labels,iloc[0,3]----->we can use index locations,at[],DataFrame.get(),query()
# 5.filters and masking---boolen indexing,isin(),between(),isnull(),notnull()

# 6.data cleaning----->dropna(),fillna(),replace(),drop_duplicate()/duplicated(),astype(),rename(),apllymap(),

# 7.sorting and ranking----->sort_values(by='age'),sort_index(),rank,

# 8.aggregations & statistics--->sum,mean,meadia,std,var,min,max,count
# 9.combining &merging------>concat(),merge(),join(),combine_first(),

# 10.reshapes 7pivote--->pivote(),melt(),stack(),unstack(),transpose(),

# 11.index operations-----set_index(),reset_index(),reindex(),sort_index(),

# 12.time series---------to_datetime(),set_index with datetime,resample(),shift(),rolling()/expanding()
# 
# 13.apply tranforms------>apply(),map(),transform(),pipe(),
# 
