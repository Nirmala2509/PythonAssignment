#Create backend page for username and password

user_name = input("Enter the username: ")
password = input("Enter the password: ")

count = 0
max_attempts = 3

while count < max_attempts:
    re_password = input("Re-enter the password: ")

    if re_password == password:
        print("Login Successful!!")
        break
    else:
        count += 1
        if count < max_attempts:
            print(f"Wrong password! You have {max_attempts - count} attempt(s) left.")
        else:
            print("Time out!!! Too many incorrect attempts.")
