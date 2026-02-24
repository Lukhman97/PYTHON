# import mysql.connector

# # 🔹 MySQL connection details
# conn = mysql.connector.connect(
#     host="localhost",       # or your server IP
#     user="root",            # your MySQL username
#     password="lukhman786",  # your MySQL password
#     database="second_datas" # your database name
# )

# print("✅ MySQL Connection Successful!")

# # 🔹 Create cursor and fetch data
# cursor = conn.cursor()
# cursor.execute("SHOW TABLES;")

# for table in cursor:
#     print(table)

# # Close connection
# cursor.close()
# conn.close()


import requests

response = requests.get("http://127.0.0.1:5000/")
print(response.json())

