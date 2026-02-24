import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
    print('Connection sucessful')
except:
    print('Not able to connect')

cursor=conn.cursor()

# query='CREATE DATABASE 10000CODERS'

# cursor.execute(query)

cursor.execute('use second_datas')

# def insertsingleroe(data):
#     try:
#         create_table="""create table if not exists students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),email VARCHAR(100),course VARCHAR(100),JOIN_DATE DATE)"""

#         name=cursor.execute(create_table)
#         print(name)
#     except:
#         print("got some error")

# def getdeptbynum(dept_num):
#     try:
#         query="""select * from emp where deptno=%s"""
#         print(query)
#         cursor.execute(query,(dept_num,))
#         result=cursor.fetchall()
#         for x in result:
#             print(x)
#     except:
#         print("sometghing went wrong")
# getdeptbynum("30")




conn.commit()

cursor.close()

conn.close()