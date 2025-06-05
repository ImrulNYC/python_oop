class BankAccount:
    MIN_BALANCE=100

    def __init__(self,owner,balance=0):
        self.owner=owner
        self._balance=balance

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"Bank account is {self.owner} is ${self._balance}")
        else:
            print('deposit must be greater than positive')

    
   
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <=5
    
    def __log_transaction(self,transcation, amount):

account1=BankAccount("Alice", 500)
account1.deposit(300)