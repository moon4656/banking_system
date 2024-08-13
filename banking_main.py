
from show_menu import show_menu
from menu_input import menu_input
from account import Account

account_list = []
num_of_accounts = 0

def make_account():
    
    global num_of_accounts    
    
    print("[계좌 개설]")
    print("계좌ID:")
    id = input()
    print("이  름:")
    name = input()
    print("입금액:")
    amount = int(input())

    account = Account(id, name)
    account.deposit(amount)
    
    account_list.append(account)
    num_of_accounts += 1


def deposit_money():
    print('[입    금]')
    id = input('계좌ID: ')
    deposit_money = int(input('입금액: '))

    for ac in account_list:
        if id in ac.account_id:
            ac.balance += deposit_money
            print('입금완료')
            return
    
    print('유효하지 않는 ID입니다')

def withdraw_money():
    print('[출    금]')
    id = input('계좌ID: ')
    withdraw_money = int(input('입금액: '))

    for ac in account_list:
        if not (id in ac.account_id):
            print('유효하지 않는 ID입니다')
            return
        if ac.balance - withdraw_money < 0:
            print('잔액부족')
            return
        
        ac.balance -= withdraw_money
        print('출금완료')
        return

def show_all_account_information():
    for ac in account_list:
        print(f'계좌ID: {ac.account_id}')
        print(f'이    름: {ac.customer_name}')
        print(f'잔    액: {ac.balance}')

    

def main():
    
    """Main function to run the banking system."""
    while True:
        show_menu()
        choice = menu_input()
        print()

        if choice == 1:
            make_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            show_all_account_information()
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("Illegal selection..")
            print()

if __name__ == "__main__":
    main()	
