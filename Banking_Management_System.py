class Person:
    def __init__(self, email, password) -> None:
        self.email= email
        self.password= password

class Bank:
    user_list = []

    def __init__(self) -> None:
        self.__bank_balance = 10000

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
        self.__user_balance = 0

    def deposit(self, amount):
        self.__user_balance += amount
        self.__bank_balance += amount

    def withdrawal(self, amount):
        if amount < self.__user_balance:
            self.__user_balance -= amount
            self.__bank_balance -= amount
        else:
            print("Insufficient Balance!!")


while True:
    bank = Bank()

    print(f"\t{'*'*10}Welcome to Bank Of Phitron!{'*'*10}")
    print("1. Create an account.\n2. Already have an account.\n3. Exit.")
    option = int(input("Choice an option: "))

    if option == 1:
        bank.create_account()
    elif option == 2:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email == "admin@bank.com" and password == "admin":
            while True:
                print(f"\t{'*'*10}Welcome Admin, to Bank Of Phitron!{'*'*10}")
                print("1. Check Total Balance.\n2. Check Total Loan.\n3. Off Loan Feature.\n4. Exit.")
                option = int(input("Choice an option: "))
                if option == 1:
                    bank.total_balance()
                elif option == 2:
                    bank.total_loan()
                elif option == 3:
                    bank.off_loan_feature()
                elif option == 4:
                    break
                else:
                    print("Choice a valid option")

        else:
            pass
    else:
        break









# class Bank:
#     pass

# def main():
#     pass
# if __name__ == '__main__':
#     main()