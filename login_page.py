import sql_queries as sq
from sql_queries import *

GLOBALS = sq.GLOBALS

def login_menu():
    u_name = input("Enter your username: ")
    GLOBALS['u_name'] = u_name
    m_no = input("Enter mobile number: ")
    GLOBALS['m_no'] = m_no
    while True:
        menu = (
            "A) Account Info",
            "B) List beneficiaries",
            "C) List cards",
            "D) Add beneficiary",
            "E) Transfer",
            "F) Update account info",
            "G) Change mpin",
            "H) Register new card"
            "Q)  Quit",
        )
        print()
        for s in menu:
            print(s)
        response = input("Select an action or Q to quit > ").upper()
        if len(response) != 1:
            print("\nInput too long or empty")
            continue
        elif response in 'ABCDEFGHQ':
            break
        else:
            print("\nInvalid response")
            continue
    return response

def jump(response):
    connection()
    u_name = GLOBALS['u_name']
    m_no = GLOBALS['m_no']

    if response == 'A':
        account_info(u_name, m_no)

    elif response == 'B':
        list_beneficiaries(u_name)

    elif response == 'C':
        list_cards(u_name)

    elif response == 'D':
        b_name = input("Enter beneficiary name: ")
        b_acc_no = int(input("Enter beneficiary name: "))
        add_beneficiary(b_name, b_acc_no, u_name)

    elif response == 'E':
        transfer()

    elif response == 'F':
        update_acc_info()

    elif response == 'G':
        mpin_change()

    elif response == 'H':
        new_card()

    else:
        print("jump: invalid argument")

def main():
    while True:
        response = login_menu()
        if response == 'Q':
            print("Quitting.")
            exit(0)
        else:
            jump(response)


if __name__ == "__main__":
    main()

