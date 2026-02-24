import requests as re
import json as jn



# import requests as re
# response = re.get('http://127.0.0.1:8000/second_datas/emp/')
# response=re.get('https://fakestoreapi.com/products')
# # print(response.json())

# for i in response.json():
#     print(i['id'])



details={ 'title': 'Fjallraven11111 - Foldsack No. 1 Backpack, Fits 15 Laptops', 'price': 1109.95, 'description': 'Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) i1111n the padded sleeve, your everyday', 'category': "men's clothing11", 'image': 'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png', 'rating': {'rate': 3.9, 'count': 1120}}

ree=re.post('https://fakestoreapi.com/products',data=details)

print(ree.json())


