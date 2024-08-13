
from show_menu import show_menu
from menu_input import menu_input
from account import Account


account_list = []
num_of_accounts = 0

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
    
    account_list.append(account)

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
        # elif choice == 4:
        #     show_all_account_information()
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("Illegal selection..")
            print()

if __name__ == "__main__":
    main()	
