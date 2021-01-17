import random
from datetime import datetime

class Bank:
    users = []
    active_user = None
    def create_account(self):
        global users
        self.name = input("enter the name")
        self.fname = input("enter tha father's name")
        while True:
            self.adhar_card = input("Enter your adhar card number: ")
            if not self.adhar_card.isdigit():  # check if a string contains a number with .isdigit()
                print("Enter only numbers\n")
                continue
            elif len(self.adhar_card) != 10:
                print("Enter 10 digits\n")
                continue
            else:
                break
        self.account_number = int(''.join(str(random.randint(0, 9)) for _ in range(12)))
        self.password = int(input("enter the password"))
        try:

            self.birthday = input("Enter your date of birth (day/month/year) : ")
            self.bday = datetime.strptime(self.birthday, '%d/%m/%Y')
        except:
            print("date format is wrong")
        self.initial_amount = int(input("enter your initial amount"))
        self.users.append({
            'name': self.name,
            'fahername': self.fname,
            'adhar_card': self.adhar_card,
            'account_number': self.account_number,
            'password': self.password,
            'birthday': self.bday,
            'current_balance': self.initial_amount})
        print("your account is auccesfully created ")
        #printdata()

    #def printdata(self):
        print("\t\t\t\t\t\t*********************** ACCOUNT CREATED SUCCESFULLY ***************************")
        print("\t\t\t\t\t\t\t\t\tname : ",self.name)
        print("\t\t\t\t\t\t\t\t\tfather's name : ",self.fname)
        print("\t\t\t\t\t\t\t\t\taadhar card number : ",self.adhar_card)
        print("\t\t\t\t\t\t\t\t\taccount number is : ",self.account_number)
        print("\t\t\t\t\t\t\t\t\tDOB : ",self.bday)
        print("\t\t\t\t\t\t\t\tinitial amount is : ",self.initial_amount)

    def login(self):
        global active_user
        global users
        print('LOGIN SCREEN'.center(50, '*'))
        self.account_number = int(input("enter your account number"))
        self.all_account_number = [x['account_number'] for x in self.users]
        if self.account_number in self.all_account_number:
            self.password = int(input("enter password : "))
            if self.users[self.all_account_number.index(self.account_number)]['password'] == self.password:
                self.active_user = self.all_account_number.index(self.account_number)
                print("you are succesfully logged in")
            else:
                print("password is incorrect")
        else:
            print("wrong account number")

    def add_money(self):
        if self.active_user != None:
            self.active_user_current_balance = self.users[self.active_user].get('current_balance')
            print("your current balance is ", self.active_user_current_balance)
            self.add_amount = int(input("enter the amount you want to add"))

            self.active_user_current_balance += self.add_amount
            self.users[self.active_user]['current_balance'] = self.active_user_current_balance
            #self.users[0]['current_balance'].update(self.active_user_current_balance)

            print("your updated balance is :", self.active_user_current_balance)
        else:
            print("login required")

    def show_balance(self):
        if self.active_user != None:
            self.show_current_balance = self.users[self.active_user].get('current_balance')
            print("your current balance is : ", self.show_current_balance)


ch = ''
b= Bank()
while ch != 4:
    # system("cls");
    print("\tMAIN MENU")
    print("\t1. create account")
    print("\t2. Login")
    print("\t3. add money")
    print("\t4. BALANCE ENQUIRY")
    print("enter you choice 1 to 4")

    ch = input()
    # system("cls");

    if ch == '1':
        b.create_account()
    elif ch == '2':
        b.login()
    elif ch == '3':
        b.add_money()
    elif ch == '4':
        b.show_balance()
    elif ch == '5':
        b.printdata()
    elif ch == '6':
        reciever_account_number = int(input("enter the reciever account number"))
        send_money = int(input("enter the amount"))
        b.transfer_money(reciever_account_number,send_money)
    else:
        print("Invalid choice")
