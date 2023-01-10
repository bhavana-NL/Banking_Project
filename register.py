
import sql_queries as sq
from sql_queries import *
from create_tables import *
GLOBALS = sq.GLOBALS

def new_register():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']

    first_name = input("Enter your first name: ")
    while not first_name.isalpha():
        print("Special characters and digits are not allowed")
        first_name = input("Please enter a valid first name: ")

    last_name = input("Enter your last name: ")
    while not last_name.isalpha():
        print("Special characters and digits are not allowed")
        last_name = input("Please enter a valid last name: ")

    username = input("Enter a username (spaces are not allowed): ")
    while ' ' in username:
        print("Spaces are not allowed")
        username = input("Please enter a valid username: ")

    while check_user(username):
        print("This username already exits. Try another username")
        username = input("Enter a username (spaces are not allowed): ")
        while ' ' in username:
            print("Spaces are not allowed")
            username = input("Please enter a valid username: ")

    address = input("Enter your address: ")
    city = input("City: ")
    while not city.isalpha():
        print("Incorrect city name")
        city = input("Please enter a valid city: ")

    state = input("State: ")
    while not state.isalpha():
        print("Incorrect state name")
        state = input("Please enter a valid state: ")

    aadhar_no = input("Enter aadhar number: ")
    while not len(aadhar_no) == 12 and aadhar_no.isdigit():
        print("Aadhar number has 12 digits. Try again !")
        aadhar_no = input("Please enter valid aadhar number: ")

    mobile_no = input("Enter mobile number: ")
    while not len(mobile_no) == 10 and mobile_no.isdigit():
        mobile_no = input("Please enter a valid 10 digit mobile number: ")

    acc_no = input("Enter account no: ")
    while not len(acc_no) == 16 and acc_no.isdigit():
        acc_no = input("Please enter 16 digit account number provide by bank: ")

    password = input("Please set your password: ")
    pass_validate = input("Please re-enter your password: ")

    while password != pass_validate:
        print("Passwords don't match!")
        password = input("Please set your password: ")
        pass_validate = input("Please re-enter your password: ")

    new_customer = (first_name, last_name, username, address, city, state, aadhar_no, mobile_no, acc_no)
    print(new_customer)

    insert_stat = '''
          INSERT INTO customer_info(first_name , last_name, username , 
          address , city , state, aadhar_no, mobile_no, account_no, password )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''

    try:
        # Executing the SQL command
        cur.execute(insert_stat, new_customer)
        # Commit your changes in the database
        conn.commit()
        print("Data inserted")

        cur.execute("SELECT * FROM customer_info")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except mysql.Error as err:
        # Rolling back in case of error
        conn.rollback()
        print(f"mysql error: {err}")
        exit(1)


new_register()