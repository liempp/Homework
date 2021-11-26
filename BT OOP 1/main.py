class BankAccount:
    def __init__(self, account_number, account_name, balance = 0):
        self._account_number = account_number
        self._account_name = account_name
        self._balance = int(balance)
        self.set_balance(balance)
      

    def get_account_number(self):
        return self._account_number

    def get_account_name(self):
        return self._account_name

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Balance không hợp lệ ")
    def withdraw(self,amount):
        if 0< amount < self._balance:
            self._balance -= amount
        else:
            print("withdraw giá trị không hợp lệ!")
        
    def deposit(self, amount):
        if int(amount) > 0:
            self._balance += amount
        else:
            print("deposit nhập vào không hợp lệ!")
    

    
    def display(self):
        print(f"{self.get_account_number()} - {self.get_account_name()}- {self.get_balance()}")

bala = BankAccount(1, "test", 3000)
bala.display()
bala.deposit(40000)
bala.display()
bala.withdraw(1)
bala.display()