#pillers
# 1. Abstraction: hides the complex inner working of an object,exposing only the essential ports for interaction
# 2. Encaptulation: involves wrapping data and methods that operate on that data within one unit, such as a class. This protects a data from external inteference and misuse,improving security and maintanability 

class ATM:
    def __init__(self,balance):
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)

sbi = ATM(1000)         

print(sbi.__balance)

class Database:
    def __init__(self):
        #self.storage = {} # public
        #self._storage = {} # protected
        self.__storage = {} # private

    def write(self,key,value):
        self.__storage[key]  = value

    def read(self,key):
        if key in self.__storage:
            print( self.__storage[key])
        else:
            print("DB item not available")    

        

db = Database() 
db.write("subscibers","1000k")
#db.read("subscibers")
db.write("name","srujan")
#db.read("name")
print(db.__storage)

# Encaptulation method

class BankAccount:
    def __init__(self,acc_num,balance=0):
        self.__acc_num = acc_num
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")

        else: print("Invalid deposi amount")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")

        else: print("Invalid amount")    

account = BankAccount("12345",10000)        
account.deposit(500)
account.withdraw(300)

print("Balance(via method):", account.__balance()) 