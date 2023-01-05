
import register as rg
import sql_queries as sq
import login_page as lg
from sql_queries import *
GLOBALS = sq.GLOBALS

def main():
    while True:
        print("\n")
        print("___________________________________________________________________________")
        print("******************* Welcome to Online Banking *******************")
        print("____________________________________________________________________________")
        print("Select 1 for Log In ")
        print("Select 2 for Registration ")

        input1 = int(input("Please select your Choice : "))
        if input1 ==2:
            print("Welcome for registration")
            rg.new_register()

        elif input1 ==1:
            print("Please login")
            lg.login_menu()
        else:
            print("Oops! Wrong option. Try again")
            continue


if __name__ == "__main__":
    main()