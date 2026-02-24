# class dog:
#     def speak(self):
#         return "Woof!!!!"
    
# class cat:
#     def speak(self):
#         return  "Meow!!!!!!"

# class tiger:
#     def speak(self):
#         return "ROARS!!!!!"

# def animal_sounds(animals):
#     print(animals.speak())

# dog1=dog()
# cat1=cat()
# tiger1=tiger()


# animal_sounds(dog1)
# animal_sounds(cat1)
# animal_sounds(tiger1)




# class sending:
#     def send(self,message):
#         print(f"SMS send : {message}")

# class sendEmail:
#     def send(self,message):
#         print(f"EMAIL send : {message}")

# class notifier:
#     def send(self,message):
#         print(f"Notifier end : {message}")

# def sendmsg(sender,message):
#     sender.send(message)

# sendmsg(sending(),"I your output is 8888")
# sendmsg(sendEmail(),"Your email is readyy")
# sendmsg(notifier(),"VIRUS ALERT,YOU ARE ABOUT TO DIE")


from abc import ABC,abstractmethod

class Vechile(ABC):
    @abstractmethod
    def vechile_range(self,speed):
        pass

class cycle(Vechile):
    def vechile_range(self,speed):
        print(f"ITs range is {speed}KMPH")

class bike(Vechile):
    def vechile_range(self,speed):
        print(f"ITs range is {speed}KMPH")

class car(Vechile):
    def vechile_range(self,speed):
        print(f"ITs range is {speed}KMPH")

class truck(Vechile):
    def vechile_range(self,speed):
        print(f"ITs range is {speed}KMPH")

cycle1=cycle()
bike1=bike()
car1=car()
truck1=truck()

cycle1.vechile_range(20)
bike1.vechile_range(80)
car1.vechile_range(120)
truck1.vechile_range(200)



        

