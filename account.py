class Account:
    def __init__(self):
        self.account_id = 0
        self.balance = 0
        self.customer_name = ''

    
    def account(self, account_id, customer_name):
        self.account_id = account_id
        self.customer_name = customer_name

    def get_account_id(self):
        return self.account_id
    
    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money
    
    def show_account_infomation():
        pass
