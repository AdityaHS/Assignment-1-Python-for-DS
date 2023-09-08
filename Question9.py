def setup_pswrd():
    while True:
        password = input("Enter a password : ")

        if len(password) < 5:
            print("Password must be at least 5 characters long.")
            continue

        if '&' not in password:
            print("Password must contain the symbol '&'")
            continue

        HasLower = False
        HasUpper = False
        for char in password:
            if char.islower():
                HasLower = True
            elif char.isupper():
                HasUpper = True

        if not (HasLower and HasUpper):
            print("Password must contain at least one uppercase and one lowercase letter.")
            continue

        print("Password has been set successfully!")
        break


setup_pswrd()