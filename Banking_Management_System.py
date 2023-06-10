"""
Admin E-Mail   : admin@bank.com
Admin Password : admin
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
        Bank.bank_info['bank_balance'] = 5000
        Bank.bank_info['bank_loan'] = 0
        # self.bank_balance = 10000
        # self.bank_loan = 0

    def create_account(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.new_user = vars(Person(email, password))
        id = self.new_user['user_id']
        if id not in self.user_list:
            self.user_list[id] = []
        self.user_list[id].append(self.new_user)
        print(self.user_list)
        print("\n\t***Account Created Successfully.")
        print("\t***Your user id: ", id, "\n")

    def total_balance(self):
        return self.bank_balance
    
    def total_loan(self):
        return self.bank_loan
    
    def off_loan_feature(self):
        return False

class Transaction:
    id_counter = 10100
    balance = 0
    def __init__(self, type, amount) -> None:
        self.transaction_id = Transaction.id_counter
        self.type = type
        self.amount = amount
        if type == 'deposit':
            Transaction.balance += amount
        elif type == 'withdrawal':
            Transaction.balance -= amount
        self.balance = Transaction.balance
        Transaction.id_counter += 1

class User(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.user_balance = 0

    def deposit(self, user_id, amount):
        # transaction history
        info = Transaction('deposit', amount)
        self.user_list[user_id].append(vars(info))
        # bank info
        if user_id not in self.bank_info:
            self.bank_info[user_id] = amount
        else:
            self.bank_info[user_id] += amount
        print("\n\t***Deposit successfully.***")
        print("\tYour Current Balance: ", self.bank_info[user_id],"\n")

    def withdrawal(self, user_id, amount):
        # transaction history
        info = Transaction('withdrawal', amount)
        self.user_list[user_id].append(vars(info))
        # bank info
        if user_id not in self.bank_info:
            self.bank_info[user_id] = amount
        else:
            self.bank_info[user_id] -= amount
        print("\n\t***Withdrawal successfully.***")
        print("\tYour Current Balance: ", self.bank_info[user_id],"\n")

        #-------------------------
        # print(self.user_list)
        # if amount > self.user_balance:
        #     print("\nInsufficient Balance!!\n")
        # elif amount > self.bank_balance:
        #     print("\nThe Bank Is Bankrupt.\n")
        # else:
        #     self.user_balance -= amount
        #     self.bank_balance -= amount
        #     print("\nYour balance: ", self.user_balance)
        #     print("Withdeawal successfully\n")

    def check_balance(self):
        return self.user_balance

    def money_transfer(self):
        pass

    def transaction_history(self):
        pass

    def take_loan(self, amount):
        if amount > self.user_balance*2:
            print("\nYou have not enough deposit!!\n")
        elif amount > self.bank_balance:
            print("\nBank has not enough money.\n")
        else:
            self.bank_balance -= amount
            self.bank_loan += amount
            print("bank balance: ", self.bank_balance)
            print("bank loan: ", self.bank_loan)
            print("\nYou got a loan successfully.\n")

while True:
    bank = Bank()
    user = User()

    print(f"\n{'*'*15} Welcome to Bank Of Phitron! {'*'*10}")
    print("1. Create an account.\n2. Already have an account.\n3. Exit.")
    option = int(input("Choice an option: "))
    loan_feature = True
    if option == 1:
        bank.create_account()
    elif option == 2:
        user_id = int(input("Enter your User ID: "))
        password = input("Enter your password: ")
        flag = 0
        # print(bank.user_list[user_id][0][password])
        pword = bank.user_list[user_id][0]['password']
        if id == 12345 and password == "admin":
            while True:
                print(f"\n{'*'*15} Welcome Admin, to Bank Of Phitron! {'*'*10}")
                print("1. Create an account.\n2. Check Total Balance.\n3. Check Total Loan.\n4. Off Loan Feature.\n5. Exit.\n")
                choice = int(input("Choice an option: "))
                if choice == 1:
                    bank.create_account()
                elif choice == 2:
                    tot_bal = bank.total_balance()
                    print("Total Balance: ", tot_bal)
                elif choice == 3:
                    loan = bank.total_loan()
                    print("Total Loan: ", loan)
                elif choice == 4:
                    loan_feature = bank.off_loan_feature()
                    print("Loan feature Off Successfully")
                elif choice == 5:
                    break
                else:
                    print("Choice a valid option")
        else:
            if user_id not in bank.user_list:
                print("\n\t***You are not a valid user.\n")
            elif pword == password:
                while True:
                    print(f"\n{'*'*15} Welcome to Bank Of Phitron! {'*'*10}")
                    print("1. Deposit Money.\n2. Withdrawal Money.\n3. Check Balance.\n4. Transfer Money.\n5. Check Transaction History.\n6. Take Loan From Bank\n7. Exit.\n")
                    choice = int(input("Choice an option: "))
                    if choice==1:
                        dps_amount = int(input("Enter deposit amount: "))
                        user.deposit(user_id, dps_amount)
                    elif choice==2:
                        wdr_amount = int(input("Enter deposit amount: "))
                        user.withdrawal(user_id, wdr_amount)
                    elif choice==3:
                        bal = user.check_balance()
                        print(f"\nYour total balance is: {bal}/=\n")
                    elif choice==4:
                        transfer_amount = int(input("Enter transfer amount: "))
                        user.money_transfer(transfer_amount)
                        # Not implemented
                    elif choice==5:
                        user.transaction_history()
                        # Not implemented
                    elif choice==6:
                        if loan_feature:
                            loan_amount = int(input("Enter loan amount: "))
                            user.take_loan(loan_amount)
                        else:
                            print("\nLending is temporarily suspended.\n")
                    elif choice==7:
                        break
                    else:
                        print("Choice a valid option")
            else:
                print("\n\t***Wrong Password!***\n")
    elif option == 3:
        break
    else:
        print("Choice a valid option")


""""
if member['email'] == email and member['password']==password:
                    flag=1
                    break
"""