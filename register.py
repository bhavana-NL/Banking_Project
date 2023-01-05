
import sql_queries as sq
from sql_queries import *

GLOBALS = sq.GLOBALS

def new_register():
    connection()
    customer_info()
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']
    first_name = ""
    last_name = ""
    username = ""
    while True:
        input1 = input("Enter your first name: ")
        if input1.isalpha() :
            first_name = input1
        else :
            print("Special characters and digits are not allowed")
            continue
        input2 = input("Enter your last name: ")
        if input2.isalpha() :
            last_name = input2
        else :
            print("Special characters and digits are not allowed")
            continue
        input3 = input("Enter a username: ")
        if ' ' in input3:
            print("Spaces are not allowed")
            continue
        else:
            username = input3
        ############ Check whether the username exists in the database ###################

        input4 = input("Enter your address: ")
        address = input4
        input5 = input("City: ")
        if input5.isalpha():
            city = input5
        else:
            print("Incorrect city name")
            continue
        input6 = input("State: ")
        if input6.isalpha():
            state = input6
        else:
            print("Incorrect state name")
            continue
        input7 = input("Enter aadhar number: ")
        if len(input7) != 12 and input7.isdigit():
            print("Digits are missing. Try again!")
            continue
        elif len(input7) == 12 and input7.isdigit():
            aadhar_no = int(input7)
        else:
            print("Incorrect input :( PS: Aadhar number has 12 digits. Try again !")
            continue
        input8 = input("Enter mobile number: ")
        if len(input8) != 10 and input8.isdigit():
            print("Digits are missing. Try again!")
            continue
        elif len(input8) == 10 and input8.isdigit():
            mobile_no = int(input8)
        else:
            print("Incorrect input :( PS: mobile number has 10 digits. Try again !")
            continue

        input9 = input("Enter card no: ")
        new_customer = (first_name,last_name,username,address,city,state, aadhar_no, mobile_no)
        print(new_customer)
        insert_stat = '''
          INSERT INTO customer_info(first_name , last_name, username , address , city , state, aadhar_no, mobile_no )
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

        break
