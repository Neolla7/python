login = "login"
password = "password"

login_input = input("please, enter login: ")
password_input = input("please, enter password: ")

if login_input != login:
    print("wrong login")
if password_input != password:
    print("wrong password")
if login_input == login and password_input == password:
    print("welcome")