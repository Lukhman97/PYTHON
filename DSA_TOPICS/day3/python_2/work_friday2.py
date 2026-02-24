#Beginner:
#1. Generate 5 random floats between 0 and 1.

import random
for i in range(5):
    b=round(random.uniform(0,1),2)
    print(b)



# 2. Dice roll simulator using random.randint.
import random
print(random.randint(1,6))

# 3. Convert 90 degrees to radians.
import math 
degree=90
print(math.radians(degree))


# 4. Factorial of a user-given number.
def fact(num):
    if num<=1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("Enter the number: "))
print(fact(num))


num=int(input())
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)


# 5. Shuffle a list of 10 integers.
import random
list1=[22,44,44,66,55,55,1,22,1,1,1,1,1,1,1,1,1,33,11111]
random.shuffle(list1)
print(list1)

# Intermediate:
# 1. Lottery draw of 6 unique numbers from 1 to 49.
import random
for i in range(6):
    print(random.randrange(1,50))


# 2. Approximate using Monte Carlo.


import random

heads = 0
total_tosses = 10000  # Number of simulations
tails=0
for _ in range(total_tosses):
    toss = random.choice(['heads', 'tails'])
    if toss == 'heads':
        heads += 1
    else:
        tails+=1

print(heads,tails)
probability = heads / total_tosses
print("Estimated probability of heads:", probability)

# 3. Calculate compound interest using math.pow.

import math
p = 1000       
r = 5          
t = 3
a=p*(pow((1+r/100),t))
c=a-p
print(c)
# 4. Trigonometry calculator using degrees.
import math
degree=60
angle=math.radians(degree)
print(angle)
a=round(math.sin(angle),3)
print(a)


# 5. Roll two dice 1000 times and plot the sum frequency.
import random

sums = []

for _ in range(1000):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    sums.append(total)

print("Sums of 1000 dice rolls:")
print(sums)
