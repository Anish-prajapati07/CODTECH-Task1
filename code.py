
def checkPassword(password):
    upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
    length = len(password)

    if (length < 6):
        print("Password must be at least 6 characters long!\n")
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upperChars += 1
            elif (password[i].islower()):
                lowerChars += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialChars += 1

    if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if (length >= 10):
            print("The strength of password is strong.\n")
        else:
            print("The strength of password is medium.\n")
    else:
        print("\nPassword is weak")
        print("\nFeedback\n")
        if (upperChars == 0):
            print("Password must contain at least 1 uppercase character\n")
        if (lowerChars == 0):
            print("Password must contain at least 1 lowercase character\n")
        if (specialChars == 0):
            print("Password must contain at least 1 special character\n")
        if (digits == 0):
            print("Password must contain at least 1 digit\n")

password = input("Enter password: ")
checkPassword(password)
