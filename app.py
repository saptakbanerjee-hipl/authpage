print("Facebook")

print("Create an Account")

first_name = input("Enter your first name: ")
print("You entered " + first_name)

last_name = input("Enter your last name: ")
print(f"You entered {last_name}")

email = input("Enter your email")
print(f"You entered {email}")

password = input("Enter your password: ")
print(f"You entered {password}")

print("User Created")

print("Login")

login_email = input("Enter your username: ")
login_password = input("Enter your password: ")

if login_email == email:
    if login_password == password:
        print(f"Welcome {first_name}")
    else:
        print("Email & password does not match")
else:
    print("Email does not match")

