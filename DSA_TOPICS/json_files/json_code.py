# import json
# # data1={"name":"lukhman","age":22}
# data1=["lukhman","shaik","22","45.88","987.66"]
# with open("./data11.json","w") as f:
#     ab=json.dumps(data1)
#     f.write(ab)
#     print(type(ab))
#     bc=json.loads(ab)
#     print(type(bc))



import json

file_name="data11.json"
with open("data11.json","r") as f:
    ab=json.load(f)
    ab["prodcuts"].append("king")
    ab["ages"].append(999999)
    ab["city"]="Andra Pradesh"
    

with open("data11.json","w") as f:
    bc=json.dump(ab,f)
    print(ab)
    



