import mysql.connector as mysql
MY_HOST = 'localhost'
MY_USER = 'bhavana'
MY_PASS = 'mypassword'
DB = 'bank_test'

GLOBALS = {}


def connection():
    mysql_db = None
    mysql_cur = None
    try:
        mysql_conn = mysql.connect(host=MY_HOST, user=MY_USER, password=MY_PASS, database=DB)
        mysql_cur = mysql_conn.cursor()
        mysql_cur.execute("use bank_test")
        print("Using bank database")
        GLOBALS['conn'] = mysql_conn
        GLOBALS['cur'] = mysql_cur
        return mysql_cur, mysql_conn
    except mysql.Error as err:
        print(f"mysql error: {err}")
        exit(1)

#***************************************** CREATE TABLES *************************************************

def customer_info():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']

    try:
        sql_create = '''
            CREATE TABLE IF NOT EXISTS customer_info (
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(16) NOT NULL,
                last_name VARCHAR(16) NOT NULL,
                username VARCHAR(16) NOT NULL,
                address VARCHAR(16) NOT NULL,
                city VARCHAR(16) NOT NULL,
                state VARCHAR(16) NOT NULL,
                aadhar_no BIGINT NOT NULL,
                mobile_no BIGINT NOT NULL,
                card_no BIGINT NOT NULL,
                FOREIGN KEY(card_no) REFERENCES card_info(card_no) ON DELETE CASCADE
            )
        '''
        cur.execute(sql_create)
        print("registration table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)


def card_table():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']
    try:
        sql_create = '''
                CREATE TABLE IF NOT EXISTS card_info
                 (
                    card_no BIGINT PRIMARY KEY AUTO_INCREMENT,
                    type ENUM('credit','debit') NOT NULL,
                    account_no BIGINT  NOT NULL,
                    username VARCHAR(16) NOT NULL,
                    expiry DATE NOT NULL, 
                    CVV INT NOT NULL,
                    mobile_no BIGINT NOT NULL                   
                )
            '''
        cur.execute(sql_create)
        print("card table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)

def beneficiary_table():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']
    try:
        sql_create = '''
                CREATE TABLE IF NOT EXISTS beneficiary
                 (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    user_id INT NOT NULL,
                    username VARCHAR(16) NOT NULL,
                    bene_name VARCHAR(16),
                    bene_acc_no BIGINT,
                    FOREIGN KEY(user_id) REFERENCES customer_info(customer_id) ON DELETE CASCADE                  
                )
            '''
        cur.execute(sql_create)
        print("beneficiary table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)


def transcations():
    cur = GLOBALS['cur']



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
    cur.execute(query,u_name)
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
    cur.execute(query, u_name)
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













