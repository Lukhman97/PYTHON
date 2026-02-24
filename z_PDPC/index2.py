import mysql.connector
from db import info


try:
    conn=mysql.connector.connect(**info)
    # print(info["user"])
    print("The server is connected")
except:
    print("The server is not connected")

cursor=conn.cursor()

# try:
#     query="CREATE database 10000coders"
#     cursor.execute(query)
# except:
#     print("The query was not executed")

try:
    cursor.execute("use 10000coders")
    print("it was using")
except:
    print("useing the database was not executed")


# try:
#     crete_table="""create table datas_data (emp_id int,emp_name varchar(35),emp_dept_no int,emp_dept_name varchar(44),sal int,age int)"""
#     cursor.execute(crete_table)
#     print("IT was executed")
# except mysql.connector.errors.ProgrammingError as e :
#     print(e)

# def insertintosinglerow(data):
#     try:
#         inserts="""insert into datas_data (emp_id,emp_name,emp_dept_no,emp_dept_name,sal,age) values(%s,%s,%s,%s,%s,%s)"""
#         cursor.execute(inserts,data)
#         print("The data is subjected")
#     except:
#         print("No data")

# insertintosinglerow((2345,"lukhman",3,"ECE",400000,22))
# insertintosinglerow((2346,"lukhman2",3,"ECE",550000,29))
# insertintosinglerow((2347,"lukhman3",4,"cse",800000,28))
# insertintosinglerow((2348,"lukhman4",5,"cse",900000,29))


# def getRecords():
#     try:
#         query='select * from datas_data'
#         cursor.execute(query)
#         results=cursor.fetchall()
#         for row in results:
#             print(row)        
#     except:
#         print('error occurred')

# getRecords()



# def getlimitedrecords(limit):
#     try:
#         query="""select * from datas_data limit %s """
#         cursor.execute(query,(limit,))
#         result=cursor.fetchall()
#         print(result)
#     except:
#         print("some thing went wrong")
#     finally:
#         print("task complted")
# getlimitedrecords(2)


# def getlimitedrecords(limit):
#     try:
#         query="""select * from datas_data order by emp_dept_no desc limit %s """
#         cursor.execute(query,(limit,))
#         result=cursor.fetchall()
#         print(result)
#     except:
#         print("some thing went wrong")
#     finally:
#         print("task complted")
# getlimitedrecords(2)


# def update_the_data(emp_dept_no,emp_name):
#     try:
#         query="""update datas_data set emp_dept_no=%s where emp_name=%s"""
#         cursor.execute(query,(emp_dept_no,emp_name))
#         result=cursor.fetchall()
#         print(result)
#     except:
#         print("some thomng went wromg11")
#     finally:
#         print("it was not excuted")
# update_the_data(3,"lukhamn2")

# def update_the_data(emp_dept_no,emp_name):
#     try:
#         query="""update datas_data set emp_dept_no=%s  where emp_name=%s"""
#         cursor.execute(query,(emp_dept_no,emp_name))
#         result=cursor.fetchall()
#         print(result)
#     except:
#         print("some thomng went wromg11")
#     finally:
#         print("it was not excuted")
# update_the_data([3,"lukhamn2"],["lukhman",6])

# def update_the_data(emp_dept_no,emp_dept_name,emp_name):
#     try:
#         query="""update datas_data set emp_dept_no=%s ,emp_dept_name=%s where emp_name=%s"""
#         cursor.execute(query,(emp_dept_no,emp_dept_name,emp_name))
#         result=cursor.fetchall()
#         for x in result:
#             print(x)
#     except:
#         print("some thomng went wromg11")
#     finally:
#         print("it was not excuted")
# update_the_data(22,"EEE","lukhman")


# def delete_records_by_id(emp_id):
#     try:
#         query="""delete from datas_data where emp_id=%s"""
#         cursor.execute(query,(emp_id,))
#         # result=cursor.fetchall()
#         # print(result)
#         print("excuted")
#     except:
#         print("Wnt wrong")
# delete_records_by_id(int(input("Entre id : ")))

# conn.commit()
# cursor.close()
# conn.close()

