class bank():
    owner=""
    balance=""
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        return "Hello "+ owner.capitalize()
    def display(self):
        return "your balance is :Rs",self.balance,"/-"
    def deposit(self):
        amount=int(input())
        self.balance+=amount
        return "your balance after deposit is :Rs",self.balance,"/-"
    def withdraw(self):
        amount=int(input())
        if(amount<=self.balance):
            return "your balance after withdraw is :Rs",self.balance-amount,"/-"
        else:
            return "Amount to be withdraw exceeds balance"
