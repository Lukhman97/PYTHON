a=[]
b=[]
def fun(operation,*values):
    # a=[]
    a.append([operation]+list(values))
no_of_values=int(input("Enter number of input sets: "))
for i in range(no_of_values):
    user_input=input("enter the operation and its values: ")
    operation,*values=user_input.split()
    values=list(map(float,values))
    n=int(input())
if a[0]=="insert":


    fun(operation,*values)
# print(a)
for k in a:
    if k[0]=="insert":
        b.insert()


a = []

def fun( operation, *values):
    # for i in range(n):
    a.append([operation] + list(values))
num_sets = int(input("Enter number of input sets: "))

for _ in range(num_sets):
    user_input = input("Enter operation and values (e.g., add 1 2 3): ")
    operation, *values = user_input.split()
    values = list(map(float, values))  # Convert to float or int as needed
    # n = int(input("Enter n: "))
    fun( operation, *values)

print(a)


# Initialize an empty list
my_list = []

# Read number of commands
n = int(input())

# Loop over each command
for _ in range(n):
    command = input().split()

    if command[0] == "insert":
        i = int(command[1])
        e = int(command[2])
        my_list.insert(i, e)

    elif command[0] == "print":
        print(my_list)

    elif command[0] == "remove":
        e = int(command[1])
        my_list.remove(e)

    elif command[0] == "append":
        e = int(command[1])
        my_list.append(e)

    elif command[0] == "sort":
        my_list.sort()

    elif command[0] == "pop":
        my_list.pop()

    elif command[0] == "reverse":
        my_list.reverse()
print(my_list)


# # 1.
# a=4.89
# print(int(a))

# # 2.
# a="7"
# print(int(a)*5)

# # 3.

# a=int(input())
# print(float(a))

# 4.

# a='3.1415'
# print(float(a)+1)



# 3. Problems on complex()
# 5. Create a complex number from real and imaginary inputs.


# a=10
# b=20
# c=complex(a,b)
# print(c)

# 6. Return square of a complex number using complex().

# a=100+121j
# print(int((a.real)**2))
# print((int(a.imag)**2))


# 4. Problems on round()
# 7. Round 6.72849 to 2 decimal places.

# a=6.72849
# print(round(a,2))


# # 8. Round user-input float to nearest integer.
# # import random
# a=float(input())
# b=round(a)
# print(b)


# # 5. Problems on min() and max()
# # 9. Find min and max from [2, 5, 1, 9, -3, 6].
# a=[2, 5, 1, 9, -3, 6]
# print(min(a))
# print(max(a))


# # 10. Find the largest of three numbers using max().

# a,b,c=map(int,input().split())
# print(max(a,b,c))





# # 11. Find alphabetically first name from ["Zara", "Bob", "Alice"].


# a=["Alice","Zara", "Bob"]
# print(max(a))
# print(min(a))


# # 6. Problems on pow()
# # 12. Find 2 ** 5 using pow().

# print(pow(2,5))



# # 13. Get base and exponent from user, return result.

# base=int(input())
# exponent=int(input())
# result=pow(base,exponent)
# print(result)

# # 14. Use pow(x, y, z) to find (x**y) % z with inputs x=2, y=3, z=5.

# print(pow(2,3)%5)

# # 7. Problems on divmod()
# # 15. Use divmod() for 23 divided by 5.

# print(divmod(23,5))


# # 16. Write function to return quotient and remainder.

# quotient=int(input())
# remainder=int(input())
# print(divmod(quotient,remainder))

# # 17. Convert number to binary using repeated divmod(num, 2).

# quotient=int(input())

# result1=divmod(quotient,2)
# quotient1 = result1[1]
# # print(quotient1)
# result2=divmod(quotient1,2)
# quotient2 = result1[1]
# divmod(quotient2,2)
# quotient3 = result2[0]
# print(quotient1,quotient2,quotient3)

# # 8. Problems on abs()
# # 18. Print absolute value of a user-input number.

# a=-12.4
# print(abs(a))


# # 19. Get absolute difference between two numbers.

# a=6
# b=15
# print(abs(a-b))

# # 20. Compute Manhattan distance from (x, y) to origin.

# a=-7
# b=8
# print(abs(a)+abs(b))

# # Bonus Practice
# # 21. Multiply two string inputs as integers.

# a='7'
# b='9'
# print(int(a)*int(b))

# # 22. Round pow(5, 3) / 7 to 3 decimal places.

# print(round(pow(5,3)/7,3))
# # 23. Print largest absolute value from [-2, -8, 3, 7].
# b=[]
# a=[-2, -8, 3, 7]
# for i in a:
#     b.append(abs(i))
# print(max(b))


# # 24. Round user float input, then use as exponent for 2.

# a=float(input())
# b=round(a)
# exp=pow(b,2)
# print(exp)