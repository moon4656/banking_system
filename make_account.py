
from account import Account
import banking_main

def make_account():
    
    print("[계좌 개설]")
    print("계좌ID:")
    id = input()
    print("이  름:")
    name = int(input())
    print("입금액:")
    amount = int(input())

    account = Account(id, name)
    account.deposit(amount)
    
    banking_main.account_list.append(account)
    