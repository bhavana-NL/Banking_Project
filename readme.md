## Welcome to "Banking Project"

### Tables in the "bank" database
- customers: 
    * id
    * first_name
    * last_name
    * username
    * address
    * city
    * state
    * aadhar number
    * mobile number
    * account number

- cards:
    * id
    * card number
    * type
    * expiry
    * cvv
    * pin
  
- accounts:
    * account number
    * username
    * card number
    * card type
  
- beneficiaries:
    * id
    * username
    * beneficiary_name
    * beneficiary_acc_number

- transactions:
    * id
    * customer id
    * account number
    * beneficiary id
    * transaction type
    * amount
    * date of transaction
  
- balance:
    * id
    * customer id
    * account number
    * current balance
