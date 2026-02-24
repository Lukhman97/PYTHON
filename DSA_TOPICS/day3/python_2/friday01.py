# a=15*15 //3 
# print(a)


# class is the perfecvt exmaple for encapulation


# public: if we declare an attribute in one class then we can acesses it in any where in the orogram 
#   ------ we can also call it has public acess modifier/


# class sample:
#     def __init__(self):
#         self._name="Lukhman"

# obj1=sample()
# print(obj1._name)

# obj1._name -----> we can acess without restrictions
# _name ------>we are not supposed to acess but we can acees
# __name ----->private---->we cant acees out of thge class but we can hack it using the namemanifyin apporaoch which is notrecommanded but we can acees by caling the class name with public



# class parent:
#     def __init__(self):
#         self.__name="lukhman shailk"
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print(self._parent__name)   #it is restrickewd to parent class only
# obj1=child()
# # print(obj1._child__name)


# class sample:
#     def __init__(self):
#         self.__name="lukhman"
#     def getdetials(self):
#         return self.__name
    
# obj=sample()
# print(obj.getdetials())


# class demo:
#     def __init__(self):
#         self.name="kinhuu"
# obj=demo()
# obj.name="Lukhman"
# print(obj.__dict__)


# class demo:
#     def __init__(self):
#         self._name="kinhuu"
# obj=demo()
# obj._name="Lukhman"
# print(obj.__dict__)



# class demo:
#     def __init__(self):
#         self.__name="kinhuu"
# obj=demo()
# obj.__name="Lukhman"
# print(obj.__dict__)


# class demo:
#     def __init__(self):
#         self.__name="kinhuu"

#     def setdetails(self):
#         self.__name="lukhman"
# obj=demo()
# obj.__name="Lukhman"
# print(obj.__dict__)
# obj.setdetails()
# print(obj.__dict__)



