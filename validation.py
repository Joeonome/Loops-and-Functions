def account_number_validation(account_number):

    if account_number:

        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False

def password_validation(password):

    if password:

        str(password)

        if len(str(password)) >= 8:
            return True



    else:
        print("Password must be at least 8 characters")
        return False

