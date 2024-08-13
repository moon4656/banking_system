from account import Account
import banking_main

def deposit_money():
    print('[입    금]')
    id = int(input('계좌ID: '))
    deposit_money = int(input('입금액: '))

    for ac in banking_main.account_list:
        if id in ac.account_id:
            ac.balance += deposit_money
            print('입금완료')
            return
    
    print('유효하지 않는 ID입니다')
