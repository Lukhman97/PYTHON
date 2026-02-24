# # num=int(input())
# # is_perfecrt_square=False
# # for i in range(1,num):
# #     if i**2==num:
# #         is_perfecrt_square=True
# #         break
# # if is_perfecrt_square:
# #     print("it is perfect")
# # else:
# #     print("It isd not perfect")


# # num=int(input())
# # is_sunny=False
# # for i in range(1,num):
# #     if i**2==(num+1):
# #         is_sunny=True
# #         break
# # if is_sunny:
# #     print("it is suunny")
# # else:
# #     print("It is not sunny")


# # num=9
# # a=num*num
# # sum=0
# # while a>0:
# #     digit=a%10
# #     sum+=digit
# #     a=a//10
# # if sum==num:
# #     print("it is neon number")
# # else:
# #     print("it is not neon number")


# # num=int(input())
# # is_prime=True
# # if num<=1:
# #     print("please enter number gretaer than one")
# # else:
# #     for i in range(2,num):
# #         if num%i==0:
# #             is_prime=False
# #             break
# #     if is_prime:
# #         print("it is prime")
# #     else:
# #         print("it is not a prime")

# # # num=int(input())
# # def prime(num):
# #     is_prime=True
# #     if num<=1:
# #         print("please enter number gretaer than one")
# #     else:
# #         for i in range(2,num):
# #             if num%i==0:
# #                 is_prime=False
# #                 break
# #         if is_prime:
# #             return True
# #         else:
# #            return False
# # # op=tuple([i for i in range(2,51) if prime(i)])
# # # op=[i for i in range(2,51) if prime(i)]
# # # op=set([i for i in range(2,51) if prime(i)])

# # op=set([i for i in range(2,51) if prime(i)])


# # print(op)




# # li=["hello","hai","welciome","some","more"]
# # a=[]
# # for i in li:
# #     rev=""
# #     for x in range(len(i)-1,-1,-1):
# #         rev+=i[x]
# #     a.append(rev)

# # print(a)




# def is_sunny(num):
#     is_sunny=False
#     for i in range(1,num):
#         if i**2==(num+1):
#             is_sunny=True
#             break
#     if is_sunny:
#         return True
#     else:
#         return False
# op=[x for x in range(10000) if is_sunny(x)]
# print(op)



# def is_neon(num):
#     num1=num
#     a=num**2
#     sum=0
#     while a>0:
#         digit=a%10
#         sum+=digit
#         a=a//10
#     if sum==num1:
#         return True
#     else:
#         return False
# op=[x for x in range(10000) if is_neon(x)]
# print(op)


# def is_perfect_square(num):
#     is_perfecrt_square=False
#     for i in range(1,num):
#         if i**2==num:
#             is_perfecrt_square=True
#             break
#     if is_perfecrt_square:
#         return True
#     else:
#         return False
# op=[x for x in range(100) if is_perfect_square(x)]
# print(op)

# li=[9,6,4,5,4,3,1,77]
# for i in range(len(li)):
#     for j in range(len(li)):
#         print(i,j)



# def revese(i):
#     rev=""
#     for x in range(len(i)-1,-1,-1):
#         rev+=i[x]
#     if revese:
#         return rev
    
# li=["hello","hai","welciome","some","more","madam"]
# op=[revese(i) for i in li ]
# print(op)




# num=int(input())
# a=1
# if num<=1:
#     b=a
# else:
#     for i in range(2,num+1):
#         a=a*i
#         b=a
# print(b)




# for i in range(6):
#     str=0
#     for j in range(i+1):
#         str=str*10+j
#     print(str)



# for i in range(6):
#     str=0
#     for j in range(1,i+1):
#         str=str*10+j
#     print(str)


# a=1
# for i in range(6):
#     str1=""
#     for j in range(i+1):
#         str1+=str(i)
    
#     print(str1)



# for i in range(6):
#     str1=""
#     for j in range(i+1):
#         str1+=chr(97+i)
#     print(str1)

# for i in range(6):
#     str1=""
#     for j in range(i+1):
#         str1+=chr(97+j)
#     print(str1)


# for i in range(97,123):
#     print(chr(i),end="")


# s="something"
# for i in range(len(s)):
#     str1=""
#     for j in range(i+1):
#         str1+=s[j]
#     print(str1)



# s="something"
# for i in range(len(s)):
#     str1=""
#     for j in range(i+1):
#         str1+=f"{s[i]}"
#     print(str1)




# # str1=""
# for i in range(1,6):
#     str1=""
#     for j in range(1,i+1):
#         str1+=str(i*i)
#     print(str1)





# # str1=""
# for i in range(1,6):
#     str1=""
#     for j in range(1,i+1):
#         str1+=str(j*j)
#     print(str1)





# n=6
# for i in range(n):
#     for j in range(n-i-1):
#         print("*",end="")
#     print()


# n=10
# for i in range(1,n+1):
#     for j in range(1,n-i-1):
#         print(i,end="")
#     print()


# n=8
# for i in range(n):
#     str1=""
#     for j in range(n-i-1):
#         str1+=str(j)
#     print(str1)


# n=8
# for i in range(n):
#     str1=""
#     for j in range(n-i-1):
#         str1+=chr(97+i)
#     print(str1)

# n=8
# for i in range(n):
#     str1=""
#     for j in range(n-i-1):
#         str1+=chr(97+j)
#     print(str1)




# n=6
# for i in range(n):
#     str1=""
#     for j in range(n-i-1):
#         str1+=chr(97+n-i-2)
#     print(str1)

# print(chr(101))


# a=[[5], [5, 9], [5, 9, 1], [5, 9, 1, 8], [5, 9, 1, 8, 7], [9], [9, 1], [9, 1, 8], [9, 1, 8, 7], [1], [1, 8], [1, 8, 7], [8], [8, 7], [7]]
# for i in range(len(a)):
#     print(len(i))

# i="xyx"
# a=set(i)
# print(a)

# li=[9,6,4,5,4,3,1,77,88]
# for i in range(len(li)):
#     for j in range(1+i,len(li)):
#         print(li[j],li[j+1])


# class Node:
#     def __init__(self, data):
#         self.data = data     # store the actual value
#         self.next = None     # store address of next node

# # Step 1: Create first node
# node1 = Node(10)

# # Step 2: Create second node
# node2 = Node(20)

# # Step 3: Create third node
# node3 = Node(30)

# # Step 4: Link the nodes together
# node1.next = node2
# node2.next = node3

# # node3.next remains None by default


# class dog:
#     def __init__(self,name,bread,data,speed):
#         self.name=name
#         self.bread=bread
#         self.data=data
#         self.speed=speed
#     def dog_speed(self):
#         self.speed+=10 
#     def barks(self):
#         print(f"{self.name} is barking.it {self.bread} bread it self says it {self.data},its spped is {self.speed}")
#     # def getdeatils(self,name,bread,data,speed):
#     #     print(f"{self.name} is barking.it {self.bread} bread it self says it {self.data},its spped is{self.speed}")
#     # def dog_speed(self):
#     #     self.speed+=10 

# dog1=dog("jack","lokesh","it is very dangerous",20)
# dog2=dog("jermon","shiperd","it is very silent",20)
# dog3=dog("max","kong","it is very lazzy",30)
# dog1.barks()
# dog1.dog_speed()
# dog1.barks()
# # dog2.barks()
# # dog2.dog_speed()
# # dog3.barks()
# # dog3.dog_speed()
# # dog1.getdeatils()



# Define Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # If head node is the one to delete
        if current and current.data == key:
            self.head = current.next
            return

        # Search for node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key not found
        if current is None:
            print(f"{key} not found in list")
            return

        # Unlink the node
        prev.next = current.next

    # Disp
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


ll = LinkedList()

# Inserting elements
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Linked List:")
ll.display()

# Deleting a node
ll.delete(20)
print("After deleting 20:")
ll.display()

# Trying to delete a non-existent element
ll.delete(100)
