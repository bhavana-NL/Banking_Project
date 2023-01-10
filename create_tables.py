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


def customers():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']

    try:
        sql_create = '''
            CREATE TABLE IF NOT EXISTS customers (
                id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(16) NOT NULL,
                last_name VARCHAR(16) NOT NULL,
                username VARCHAR(16) NOT NULL,
                address VARCHAR(16) NOT NULL,
                city VARCHAR(16) NOT NULL,
                state VARCHAR(16) NOT NULL,
                aadhar_no BIGINT NOT NULL,
                mobile_no BIGINT NOT NULL,
                account_no BIGINT NOT NULL,
                password VARCHAR(150) NOT NULL,
                FOREIGN KEY(account_no) REFERENCES accounts(acc_no) ON DELETE CASCADE
            )
        '''
        cur.execute(sql_create)
        print("customers table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)


def cards():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']
    try:
        sql_create = '''
                CREATE TABLE IF NOT EXISTS cards
                 (                 
                    card_no BIGINT PRIMARY KEY,
                    type ENUM('credit','debit') NOT NULL,
                    expiry DATE NOT NULL, 
                    CVV INT NOT NULL,
                    PIN INT NOT NULL
                                       
                )
            '''
        cur.execute(sql_create)
        print("card table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)

def beneficiaries():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']
    try:
        sql_create = '''
                CREATE TABLE IF NOT EXISTS beneficiaries
                 (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    cust_id INT NOT NULL,
                    username VARCHAR(16) NOT NULL,
                    bene_name VARCHAR(16),
                    bene_acc_no BIGINT,
                    FOREIGN KEY(cust_id) REFERENCES customers(id) ON DELETE CASCADE                  
                )
            '''
        cur.execute(sql_create)
        print("beneficiary table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)

def accounts():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']
    try:
        sql_create = '''
                    CREATE TABLE IF NOT EXISTS accounts
                     (
                        acc_no BIGINT PRIMARY KEY,
                        username VARCHAR(16) NOT NULL,
                        card_no  BIGINT NOT NULL,
                        card_type ENUM('credit','debit') NOT NULL,
                        FOREIGN KEY(card_no) REFERENCES cards(card_no) ON DELETE CASCADE                  
                    )
                '''
        cur.execute(sql_create)
        print("accounts table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)
def transactions():
    cur = GLOBALS['cur']

    try:
        sql_create = '''
                    CREATE TABLE IF NOT EXISTS transactions
                     (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        cust_id INT NOT NULL,
                        acc_no  BIGINT NOT NULL,
                        beneficiary_id INT NOT NULL,
                        transaction_type ENUM('W','D') NOT NULL,
                        amount INT NOT NULL,
                        transaction_date TIMESTAMP NOT NULL,
                        FOREIGN KEY(cust_id) REFERENCES customers(id) ON DELETE CASCADE ,    
                        FOREIGN KEY(acc_no) REFERENCES accounts(acc_no) ON DELETE CASCADE             
                    )
                '''
        cur.execute(sql_create)
        print("transactions table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)


def balance():
    cur = GLOBALS['cur']
    conn = GLOBALS['conn']
    try:
        sql_create = '''
                CREATE TABLE IF NOT EXISTS balance
                 (
                    id INT PRIMARY KEY AUTO_INCREMENT,                     
                    cust_id INT NOT NULL,
                    acc_no BIGINT NOT NULL,
                    balance INT NOT NULL,
                    FOREIGN KEY(cust_id) REFERENCES customers(id) ON DELETE CASCADE  

                )
            '''
        cur.execute(sql_create)
        print("balance table created")

    except mysql.Error as err:
        print(f"could not create table: {err})")
        exit(1)




