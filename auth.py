# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import random

import validation

"""
This is an improved mock ATM program.
This Program assumes that there is only one registered user--> 'user', and that every other person is just
 a new customer.
"""

database = {'user': [1234512345, 'joe@yahoo.com', "Joe", "Onome", "JoePassword", 20000]}


def init():
    print("Welcome to bankPHP")

    try:
        have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    except ValueError:
        print("Input must be 1 or 2")
        init()

    if have_account == 1:

        login_user()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login_user():
    print("********* Login ***********")

    account_number_user = input("What is your account number? \n")

    is_valid_account_number_user = validation.account_number_validation(account_number_user)

    if account_number_user == str(database["user"][0]):

        password = input("What is your password \n")

        is_valid_password = validation.password_validation(password)

        if is_valid_password:

            if password == str(database["user"][4]):

                bank_operation_user()
            else:
                print('Invalid account or password')
                login_user()
        else:
            print('Invalid account or password')
            login_user()
    else:
        print("Account Number/Password Invalid: check that you have up to 10 digits and only integers, and that you "
              "are "
              "registered with us")
        login_user()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = input("What is your password \n")

        is_valid_password = validation.password_validation(password)

        if is_valid_password:
            bank_operation()

        else:
            print('Invalid account or password')
            login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        login()


def register():
    print("****** Register *******")

    email = str(input("What is your email address? \n"))

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    is_valid_password = validation.password_validation(password)

    if is_valid_password:

        account_number = generation_account_number()

        database["user_details"] = [account_number, first_name, last_name, email, password, 0]

        user_created = database["user_details"]

        if user_created:
            print("Your Account Has been created")
            print(" == ==== ====== ===== ===")
            print("Your account number is: %d" % account_number)
            print("Make sure you keep it safe")
            print(" == ==== ====== ===== ===")

            login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation_user():
    user = [database["user"][2], database["user"][3]]

    print("Welcome %s %s " % (user[0], user[1]))

    try:
        selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    except ValueError:
        print("Input must be 1, 2, 3 or 4")
        bank_operation_user()

    if selected_option == 1:
        deposit_operation_user()

    elif selected_option == 2:
        withdrawal_operation_user()

    elif selected_option == 3:
        logout()

    elif selected_option == 4:
        exit()

    else:

        print("Invalid option selected")
        bank_operation_user()


def bank_operation():
    user = [database["user_details"][1], database["user_details"][2]]

    print("Welcome %s %s " % (user[0], user[1]))

    try:
        selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    except ValueError:
        print("Input must be 1, 2, 3 or 4")
        bank_operation()

    if selected_option == 1:

        deposit_operation()

    elif selected_option == 2:

        withdrawal_operation()

    elif selected_option == 3:

        logout()

    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation()


def withdrawal_operation_user():
    print("****** Withdrawal ******")
    current_balance_user = database["user"][5]

    print("Your current balance is %d" % current_balance_user)

    try:
        withdrawal_amount_user = int(input("How much will you like to withdraw? \n"))

    except ValueError:
        print("Please enter a valid number")
        withdrawal_operation_user()

    if withdrawal_amount_user <= current_balance_user:
        print("Transaction Successful!")
        new_current_balance_user = current_balance_user - withdrawal_amount_user
        print("Your current balance is %d" % new_current_balance_user)
        bank_operation_user()

    else:
        print("Insufficient funds, what will you like to do?")

        try:
            other_operation_user = int(input("(1) Try again (2) Exit \n"))
        except ValueError:
            print('Please enter a valid number')
            withdrawal_operation_user()

        if other_operation_user == 1:
            withdrawal_operation_user()

        elif other_operation_user == 2:
            init()

        else:
            print("Please enter a valid number")
            withdrawal_operation_user()


def withdrawal_operation():
    print("****** Withdrawal ******")
    current_balance = database["user_details"][5]

    print("Your current balance is %d" % current_balance)
    print("You cannot make any withdrawal at this time")
    bank_operation()


def deposit_operation_user():
    print("***** Deposit *****")
    current_balance = database["user"][5]
    print("Your current balance is %d" % current_balance)

    try:
        deposit_amount_user = int(input('How much do you want to deposit \n'))

    except ValueError:
        print('Please enter a valid number')
        deposit_operation_user()

    print('Your have successfully deposited %d' % deposit_amount_user)
    current_acc_balance = current_balance + deposit_amount_user
    print('Your new account balance is %d' % current_acc_balance)

    try:
        other_operations_user = int(input("What would you like to do? \n (1) Other Operations (2) Exit \n"))
    except ValueError:
        print('Invalid character entered, exiting...')
        exit()
    except UnboundLocalError:
        pass

    if other_operations_user == 1:
        bank_operation_user()

    elif other_operations_user == 2:
        exit()

    else:
        print("Invalid number entered, exiting...")
        exit()


def deposit_operation():
    print("***** Deposit *****")
    current_balance = database["user_details"][5]
    print("Your current balance is %d" % current_balance)

    try:
        deposit_amount = int(input('How much do you want to deposit \n'))

    except ValueError:
        print('Please enter a valid number')
        deposit_operation()

    print('Your have successfully deposited %d' % deposit_amount)
    current_acc_balance = current_balance + deposit_amount
    print('Your new account balance is %d' % current_acc_balance)

    try:
        other_operations = int(input("What would you like to do? \n (1) Other Operations (2) Exit \n"))
    except ValueError:
        print('Invalid character entered, exiting...')
        exit()
    except UnboundLocalError:
        pass

    if other_operations == 1:
        bank_operation()

    elif other_operations == 2:
        exit()

    else:
        print("Invalid number entered, exiting...")
        exit()


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


def exit():
    print('***** Thank you for banking with us! *****')


init()
