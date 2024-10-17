password = input("Please enter in a password:")

if len(password) >= 8:
    if not password.isalpha() and not password.isdigit() :
        print("Your password is valid")
    else:
        print("Your password must contain at least 8 characters, and a mix of letters and numbers")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")