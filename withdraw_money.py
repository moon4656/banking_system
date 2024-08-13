from account import Account
import banking_main

def withdraw_money():
    print('[출    금]')
    id = int(input('계좌ID: '))
    withdraw_money = int(input('입금액: '))

    for ac in banking_main.account_list:
        if not (id in ac.account_id):
            print('유효하지 않는 ID입니다')
            return
        if ac.balance - withdraw_money < 0:
            print('잔액부족')
            return
        
        ac.balance -= withdraw_money
        print('출금완료')
        return