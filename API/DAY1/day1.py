import requests as re
import json as jn

# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",      # or 127.0.0.1
#     user="root",           # your MySQL username
#     password="lukhman786",  # your MySQL password
#     database="second_datas"  # existing database name
# )

# cur = conn.cursor()
# print(cur)


# request1=re.get('https://fakestoreapi.com/products')

request1=re.get('http://127.0.0.1:8000/second_datas')


print(request1.json())

# for i in request1.json():
#     print(i["id"])


# details={
#     "name":"lukhman",
#     "age"
# }