# class Parent_actor:
#     def __init__(self,pname,pworth):
#         self.pname=pname
#         self.pworth=pworth
#         print(f"{self.pname} is the parent")
        
#     def paserts(self):
#         # self.pworth=pworth
#         print(f"{self.pname} asserts are {self.pworth}")
# class Child_actor(Parent_actor):
#     def __init__(self,pname,cname,pworth,cworth):
#         super().__init__(pname,pworth)
#         self.cname=cname
#         self.cworth=cworth
#         print(f"{self.cname} is come by the reference of {self.pname}")
#         # super().__init__()
        
#     def childs(self):
#         print(f"{self.cname} asserts are {self.cworth}")
# class super1_child(Child_actor):
#     def __init__(self, pname,cname,ccname, pworth,cworth):
#         super().__init__(pname,cname,pworth,cworth)
#         self.ccname=ccname
#         print(f"{self.cname} is come by the reference of {self.pname} and again {self.ccname} came from {self.cname}")
#     def cchilds(self,ccworth):
#         self.ccworth=ccworth 
#         print(f"{self.ccname} asserts are {self.ccworth}")
#     def totalasserts(self):
#         print(f"total asserts of {self.ccname} is {self.pworth + self.ccworth +self.cworth }")


# # obj1=Parent_actor("hari krishna")
# # obj1.paserts(4000000)

# obj1=super1_child("hari krishna","nTr","bargav",20,40)
# # obj1.childs(75)
# obj1.cchilds(15)
# # obj1.childs()
# obj1.totalasserts()
# # obj1.paserts()
        