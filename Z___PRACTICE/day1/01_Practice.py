# x:int="10"
# print(type(x))

# import keyword
# print(keyword.kwlist)


# list1=[10,20,30]
# it=iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))

# nums=["a","b","c"]
# for i,v in enumerate(nums):
#     print(i,v)

# a = [1, 2]
# b = ["x", "y"]

# for i in zip(a, b):
#     print(i)
# a=[10,20,30]
# b=[100,200,300]
# for i in zip(a,b):
#     print(i)

# nums=[10,20,30]
# result=filter(lambda x:x*2,nums)
# print(list(result))

# s="lukhmanssss"
# print(s.count())


# def print_numbers(n):
#     if n > 10:
#         return
#     print(n)
#     print_numbers(n + 1)

# print_numbers(1)


# print(*range(1, 10))

def ad(*args,**kwargs):
    print(args)
    print(kwargs)
ad(1,2,3,name="Lukman",age=30)