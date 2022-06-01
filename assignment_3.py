from math import cos


class BankAccount():


    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    def deposit(self,d):
        
        self.balance+=d


    def withdrawal(self,w):
        
        if w>self.balance:
            print("Impossible operation! Insufficient balance!")
        else:
            self.balance-=w

    def bankFees(self):
        self.balance-=(self.balance*5)/100

    def display(self):
        return f"AccountNumber: {self.accountNumber} Name: {self.name} Balance: {self.balance}$"

costumer=BankAccount(12345,"Emrah",500)
print(costumer.display())
costumer.deposit(745)
print(costumer.display())
costumer.withdrawal(327)
print(costumer.display())
costumer.bankFees()
print(costumer.display())


    