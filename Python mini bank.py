import sys 
class Customer: 
    bankname='VermaBANK' 
    def __init__(self,name,balance=0.0): 
        self.name=name 
        self.balance=balance 
    
    def deposit(self,amt): 
        self.balance=self.balance+amt 
        print('Balance after deposit:',self.balance) 

    def withdraw(self,amt): 
        if amt>self.balance: 
            print('Insufficient Funds..cannot perform this operation') 
            sys.exit() 
        self.balance=self.balance-amt 
        print('Balance after withdraw:',self.balance)

    def CheckBalance(self):
         print('Your current balance is:',self.balance)

name=input('Enter Your Name: ') 
c=Customer(name)
print('Hello', name ,'Welcome to',Customer.bankname) 
while True: 
    print('d-Deposit \nw-Withdraw \nb-Check Balance \ne-exit') 
    option=input('Choose your option:') 
    if option=='d' or option=='D': 
        amt=float(input('Enter amount:')) 
        c.deposit(amt) 
    elif option=='w' or option=='W': 
        amt=float(input('Enter amount:')) 
        c.withdraw(amt) 
    elif option=='b' or option=='B':
        c.CheckBalance()
    elif option=='e' or option=='E': 
        print('Thanks for Banking') 
        sys.exit() 
    else: 
        print('Invalid option..Plz choose valid option') 