# class person:
#     name = "please enter the name"
#     email="example@gmail.com"
#     phome = "0000-0000000"
#     address = "your address"
#     def info(self):
#         print(f"Name : {self.name}\nEmail : {self.email}\nPhone : {self.phome}\nAddress : {self.address}")


# sami  = person()
# sami.name = "samiullah baig"
# sami.address = "D67 block d qalandarabad"
# sami.phome = "03182814121"
# sami.info()
# print("------------------------------")
# asad = person()
# asad.name = "asad baig"
# asad.address = "qallandarabad"
# asad.email = "asadbaig1998@gmail.con"
# asad.info()


# class person:

#     print("welcome to the class")
#     def __init__(self , name , age ,car_name) :
#         self.name = name
#         self.age = age 
#         self.car_name = car_name

#     def info(self):

#         print(f"your name is {self.name}\nyour age is {self.age}\nyour car name is {self.car_name}")


# name = input("Enter your name : ")    
# age = int(input("Enter the age : "))
# car_name = input("Enter your car name : ")
# one = person(name,age,car_name)
# tow = person(name,age,car_name)
# one.info()
# tow.info()



cars=[]

while True:
    
    car_name = input(f"Enter the name of the car number  : ").lower()
    if car_name == "exit":
        break
    cars.append(car_name)
    
print(f"here is the list of the cars :  {cars}")