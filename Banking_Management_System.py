"""
*****************************************
*   Author  : nasirul866               *
*   Created : 10-06-2023   10:04:19    *
*****************************************
Project Name : Banking Management System.
Required Info:
=========================================
|     Admin User ID ------ : 12345      |
|     Admin Password ----- : admin      |
|     Bank Initial Balance : 5000       |
|     Bank Initial Loan -- : 0          |
|     Users Initial Balance: 0          |
=========================================
"""
class Person:
    id_counter = 100
    def __init__(self, email, password) -> None:
        self.user_id = Person.id_counter
        self.email= email
        self.password= password
        Person.id_counter += 1

class Bank:
    user_list = {}
    bank_info = {}

    def __init__(self) -> None:
        pass

    def create_account(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.new_user = vars(Person(email, password))
        id = self.new_user['user_id']
        if 'bank_balance' not in self.bank_info:
            self.bank_info['bank_balance'] = 5000
        if 'bank_loan' not in self.bank_info:
            self.bank_info['bank_loan'] = 0
        if 'loan_feature' not in self.bank_info:
            self.bank_info['loan_feature'] = True
        if id not in self.bank_info:
            self.bank_info[id] = 0
        if id not in self.user_list:
            self.user_list[id] = []
        self.user_list[id].append(self.new_user)
        print("\n\t***Account Created Successfully.")
        print("\t***Your user id: ", id, "\n")

    def total_balance(self):
        print("\n\t*** Bank Available Balance: ", self.bank_info['bank_balance'], "\n")
    
    def total_loan(self):
        print("\n\t*** Bank Total Loan: ", self.bank_info['bank_loan'], "\n")
    
    def off_loan_feature(self):
        self.bank_info['loan_feature'] = False
        print("\n\t*** Loan feature Off Successfully. ***\n")

class Transaction:
    id_counter = 10100
    balance = 0
    def __init__(self, type, amount, bal) -> None:
        self.transaction_id = Transaction.id_counter
        self.type = type
        self.amount = amount
        if type == 'deposit':
            Transaction.balance = bal + amount
        elif type == 'loan':
            Transaction.balance = bal + amount
        elif type == 'recive':
            Transaction.balance = bal + amount
        elif type == 'withdrawal':
            Transaction.balance = bal - amount
        elif type == 'send':
            Transaction.balance = bal - amount
        Transaction.id_counter += 1
        self.balance = Transaction.balance

class User(Bank):
    def __init__(self) -> None:
        super().__init__()

    def deposit(self, user_id, amount):
        bal = self.bank_info[user_id]
        # transaction history
        info = Transaction('deposit', amount, bal)
        self.user_list[user_id].append(vars(info))
        # bank info
        if user_id not in self.bank_info:
            self.bank_info[user_id] = amount
            self.bank_info['bank_balance'] += amount
        else:
            self.bank_info[user_id] += amount
            self.bank_info['bank_balance'] += amount
        print("\n\t***Deposit successfully.***")

    def withdrawal(self, user_id, amount):
        # bank info
        if user_id not in self.bank_info:
            print("\n\t***Insufficient Balance!***\n")
        elif amount > self.bank_info[user_id]:
            print("\n\t***Insufficient Balance!!***\n")
        elif amount > self.bank_info['bank_balance']:
            print("\n\t***The Bank Is Bankrupt.***\n")
        else:
            bal = self.bank_info[user_id]
            self.bank_info[user_id] -= amount
            self.bank_info['bank_balance'] -= amount
            print("\n\t***Withdrawal successfully.***")
            # transaction history
            info = Transaction('withdrawal', amount, bal)
            self.user_list[user_id].append(vars(info))

    def check_balance(self, user_id):
        if user_id not in self.bank_info:
            print("\n\t*** Balance not found! ***\n")
            print("\n\t*** Please Deposit First! ***\n")
        else:
            print("\n\t***Your Current Balance: ", self.bank_info[user_id]," ***\n")

    def money_transfer(self, user_id, reciver_id, amount):
        if user_id not in self.bank_info:
            print("\n\tUser id not found!")
        elif reciver_id not in self.bank_info:
            print("\n\tReciver id not found!")
        else:
            bal = self.bank_info[user_id]
            # sender bank info
            self.bank_info[user_id] -= amount
            # sender transaction history
            info = Transaction('send', amount, bal)
            self.user_list[user_id].append(vars(info))
            # reciver bank info
            self.bank_info[reciver_id] += amount
            # reciver transaction history
            info = Transaction('recive', amount, bal)
            self.user_list[reciver_id].append(vars(info))
            print("\n\t*** Money Transferred Successfully. ***\n")

    def transaction_history(self, user_id):
        length = len(self.user_list[user_id])
        print("\n\t****Your Transaction History: ")
        for i in range(1, length):
            my_dict = self.user_list[user_id][i]
            str_repr = ', '.join([f"{key}: {value}" for key, value in my_dict.items()])
            print("\t", str_repr)
        print()

    def take_loan(self, user_id, amount):
        val = self.bank_info[user_id]
        if amount > val*2:
            print("\n\t***You have not enough deposit!***\n")
        elif amount > self.bank_info['bank_balance']:
            print("\n\t***Bank has not enough money.***\n")
        else:
            bal = self.bank_info[user_id]
            self.bank_info['bank_balance'] -= amount
            self.bank_info['bank_loan'] += amount
            self.bank_info[user_id] += amount
            print("\n\t***You got a loan successfully.***\n")
            # transaction history
            info = Transaction('loan', amount, bal)
            self.user_list[user_id].append(vars(info))

while True:
    bank = Bank()
    user = User()

    print(f"\n{'*'*15} Welcome to Bank Of Phitron! {'*'*10}")
    print("1. Create an account.\n2. Already have an account.\n3. Exit.")
    
    option = 0
    try:
        option = int(input("Choice an option: "))
    except:
        print("\n\t***Choice a valid option!***\n")
    finally:
        if option == 1:
            bank.create_account()
        elif option == 2:
            user_id = input("Enter your User ID: ")
            password = input("Enter your password: ")
            flag = 0
            if user_id == "12345" and password == "admin":
                while True:
                    print(f"\n{'*'*15} Welcome Admin, to Bank Of Phitron! {'*'*10}")
                    print("1. Create an account.\n2. Check Total Balance.\n3. Check Total Loan.\n4. Off Loan Feature.\n5. Exit.\n")
                    choice = 0
                    try:
                        choice = int(input("Choice an option: "))
                    except:
                        print("\n\t***Choice a valid option!***\n")
                    finally:
                        if choice == 1:
                            bank.create_account()
                        elif choice == 2:
                            bank.total_balance()
                        elif choice == 3:
                            bank.total_loan()
                        elif choice == 4:
                            bank.off_loan_feature()
                        elif choice == 5:
                            break
                        else:
                            print("\n\t***Choice a valid option!***\n")
            else:
                user_id = int(user_id)
                if user_id not in bank.user_list:
                    print("\n\t***You are not a valid user.\n")
                else:
                    pword = bank.user_list[user_id][0]['password']
                    if pword == password:
                        while True:
                            print(f"\n{'*'*15} Welcome to Bank Of Phitron! {'*'*10}")
                            print("1. Deposit Money.\n2. Withdrawal Money.\n3. Check Balance.\n4. Transfer Money.\n5. Check Transaction History.\n6. Take Loan From Bank\n7. Exit.\n")
                            choice = 0
                            try:
                                choice = int(input("Choice an option: "))
                            except:
                                print("\n\t***Choice a valid option!***\n")
                            finally:
                                if choice==1:
                                    dps_amount = int(input("Enter deposit amount: "))
                                    user.deposit(user_id, dps_amount)
                                elif choice==2:
                                    wdr_amount = int(input("Enter withdrawal amount: "))
                                    user.withdrawal(user_id, wdr_amount)
                                elif choice==3:
                                    user.check_balance(user_id)
                                elif choice==4:
                                    reciver_id = int(input("Enter reciver id: "))
                                    transfer_amount = int(input("Enter transfer amount: "))
                                    user.money_transfer(user_id, reciver_id, transfer_amount)
                                elif choice==5:
                                    user.transaction_history(user_id)
                                elif choice==6:
                                    if bank.bank_info['loan_feature']:
                                        loan_amount = int(input("Enter loan amount: "))
                                        user.take_loan(user_id, loan_amount)
                                    else:
                                        print("\n\t***Lending is temporarily suspended.***\n")
                                elif choice==7:
                                    break
                                else:
                                    print("Choice a valid option")
                    else:
                        print("\n\t***Wrong Password!***\n")
        elif option == 3:
            break
        else:
            print("\n\t***Choice a valid option")

# ======================== The End ============================= #
