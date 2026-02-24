
# # 1. fruits = [ "apple", "mango", "banana"]
# #     Write a program to:
# #     Print the 1st & last fruit 
# #     Print the total number of fruits
# #     Replace "mango" with "pineapple"
# #     Print the upload list

# fruits = [ "apple", "mango", "banana"]
# print(fruits[1] )
# print(fruits[-1])
# print(len(fruits))
# fruits[-2]= "pineapple"
# print(fruits)

# # 2. x=[ "harish, "naresh", "suresh", "Mahesh" ]
# #     Write a program to:
# #     Print the id()
# #     Update "suresh" to "kiran"
# #     Print the list again
# #     Print the id() after the change

# x= ["harish", "naresh", "suresh", "Mahesh" ]
# for i in x:
#     print(id(i))
# x[2]="kiran"
# print(x)
# for i in x:
#     print(id(i))



# # 3. data = [1, 2, [4, 5], [6, 7], 8, ["something"]]
# #      Write a program to:
# #      Print 4 from the nested list
# #      Print 6 from the nested list
# #      Print the letter "m" from the string "something"


# data = [1, 2, [4, 5], [6, 7], 8, ["something"]]
# print(data[2][0])
# print(data[3][0])
# print(data[5][0][2])


# # 4. mixed = [1, 2, "hi", 12.5, True]
# #      Write a program to:
# #      Print both the element & its data type in the following format:


# mixed = [1, 2, "hi", 12.5, True]
# for i in range(len(mixed)):
#     print(type(mixed[i]))

# # Value: 1, type: <class 'int'>
# # Value: hi, Type: <class 'str'>
 