from create_tables import *
import create_tables as ct

connection()
GLOBALS = ct.GLOBALS

print(GLOBALS)

#****************************************** REGISTRATION FUNCTIONS *************************************************

def check_user(u_name):
    cur = GLOBALS['cur']
    query = '''
        SELECT id
        FROM customers 
        WHERE username = %s
    '''
    cur.execute(query, (u_name,))
    if len(cur.fetchall()) >= 1:
        return True
    else:
        return False



#****************************************** LOGIN FUNCTIONS *************************************************

def account_info(u_name, mobile):
    cur = GLOBALS['cur']
    info_query = '''
        SELECT * FROM customer_info 
        WHERE username = %s
            mobile_no = %s
    '''
    u_info = (u_name, mobile)
    cur.execute(info_query,u_info)
    print("Account details:")
    print(cur.fetchone()[0])

def list_beneficiaries(u_name):
    cur = GLOBALS['cur']
    query = '''
        SELECT * FROM beneficiary
        WHERE username = %s
        '''
    cur.execute(query,(u_name,))
    result = cur.fetchall()
    print("List of beneficiaries: ")
    for row in result:
        print(row)

def list_cards(u_name):
    cur = GLOBALS['cur']
    query = '''
            SELECT card_no , type, expiry 
             FROM card_info
            WHERE username = %s
            '''
    cur.execute(query, (u_name,))
    result = cur.fetchall()
    print("List of cards for user {}: ".format(u_name))
    print("Displaying card number, debit/credit AND expiry")
    for row in result:
        print(row)

def add_beneficiary(b_name, b_acc_no, u_name):
    cur = GLOBALS['cur']
    query = '''
                INSERT INTO beneficiary(username, bene_name, bene_acc_no)   
                 VALUES (%S, %S, %s)
                '''
    bene_data = (u_name, b_name, b_acc_no)
    cur.execute(query, bene_data)
    result = cur.fetchall()
    print("Details of beneficiary added")
    print(cur.fetchone()[0])













