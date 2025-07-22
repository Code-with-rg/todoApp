import re

while True:
    password = input("Enter The Strong Password :")
    cap = re.search('[A-Z]', password)
    small = re.search('[a-z]', password)
    digits = re.search('[0-9]', password)
    specialCharacter = re.search('[!@#$%^&*]', password)
    if not cap:
        print("Password Must have the any One capital latter")
    elif not specialCharacter:
        print("Password mush have the any one special character at any place")
    elif not digits:
        print("Password must have the Number man !!")
    elif len(password) < 16:
        print("password should be longer than the 16 characters")

    else:
        print(f"{password} is greater strong !! ")
        break
