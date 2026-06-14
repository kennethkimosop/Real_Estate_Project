#classes are used to create objects

#Create class
class Courses:
    def __init__(self, CS50,Business,Engineering):
        self.CS50 = CS50
        self.Business = Business
        self.Engineering = Engineering

class User:
    #constructor
       
    def greeting(self):
        return f"Hello, my name is {self.name} and I am {self.age}"
    
    def has_birthday(self):
        self.age += 1



class Customer(User):
    def __init__(self, name, email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self,balance):
        self.balance = balance
       
    def greeting(self):
        return f"Hello, my name is {self.name} and I am {self.age} and I owe a balance {self.balance}"

#init customer
john = Customer('John Doe', "john@gmail.com",40)
print(john.name)
john.set_balance(500)
print(john.balance)
print(john.greeting())


details = Courses("Brax", "Angel","Kenneth")
print(details.CS50)

#call method

# Init user object
# brad = User("Brad", "brad@gmail.com", 30)
# kenneth = User("Kenneth Kraig", 'kenkimosop4@gmail.com', 27)

# print(brad.name,brad.age,brad.email)

# print(kenneth.greeting())

#call method
