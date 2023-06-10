class Person:
    def __init__(self, email, password) -> None:
        self.email= email
        self.password= password

class Bank:
    user_list = []

    def __init__(self) -> None:
        self.bank_balance = 10000
        self.bank_loan = 0

    def create_account(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.new_user = Person(email, password)
        self.user_list.append(vars(self.new_user))

    def total_balance():
        pass
    def total_loan():
        pass
    def off_loan_feature():
        pass

class User(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.user_balance = 0

    def deposit(self, amount):
        self.user_balance += amount
        self.bank_balance += amount
        print("\nYour balance: ", self.user_balance)
        print("Deposit successfully.\n")

    def withdrawal(self, amount):
        if amount > self.user_balance:
            print("\nInsufficient Balance!!\n")
        elif amount > self.bank_balance:
            print("\nThe Bank Is Bankrupt.\n")
        else:
            self.user_balance -= amount
            self.bank_balance -= amount
            print("\nYour balance: ", self.user_balance)
            print("Withdeawal successfully\n")

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
            print("\nYou got a loan successfully.\n")

while True:
    bank = Bank()
    user = User()

    print(f"\n{'*'*15} Welcome to Bank Of Phitron! {'*'*10}")
    print("1. Create an account.\n2. Already have an account.\n3. Exit.")
    option = int(input("Choice an option: "))

    if option == 1:
        bank.create_account()
    elif option == 2:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        flag = 0
        if email == "admin@bank.com" and password == "admin":
            while True:
                print(f"\n{'*'*15} Welcome Admin, to Bank Of Phitron! {'*'*10}")
                print("1. Check Total Balance.\n2. Check Total Loan.\n3. Off Loan Feature.\n4. Exit.\n")
                choice = int(input("Choice an option: "))
                if choice == 1:
                    bank.total_balance()
                elif choice == 2:
                    bank.total_loan()
                elif choice == 3:
                    bank.off_loan_feature()
                elif choice == 4:
                    break
                else:
                    print("Choice a valid option")
        else:
            for member in bank.user_list:
                if member['email'] == email and member['password']==password:
                    flag=1
                    break
            if flag:
                while True:
                    print(f"\n{'*'*15} Welcome to Bank Of Phitron! {'*'*10}")
                    print("1. Deposit Money.\n2. Withdrawal Money.\n3. Check Balance.\n4. Transfer Money.\n5. Check Transaction History.\n6. Take Loan From Bank\n7. Exit.\n")
                    choice = int(input("Choice an option: "))
                    if choice==1:
                        dps_amount = int(input("Enter deposit amount: "))
                        user.deposit(dps_amount)
                    elif choice==2:
                        wdr_amount = int(input("Enter deposit amount: "))
                        user.withdrawal(wdr_amount)
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
                        loan_amount = int(input("Enter loan amount: "))
                        user.take_loan(loan_amount)
                    elif choice==7:
                        break
                    else:
                        print("Choice a valid option")
            else:
                print("You are not a valid user.")
    elif option == 3:
        break
    else:
        print("Choice a valid option")









# class Bank:
#     pass

# def main():
#     pass
# if __name__ == '__main__':
#     main()