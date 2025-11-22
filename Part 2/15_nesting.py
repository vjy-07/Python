username = input("Enter your username: ")
password = input("Enter your password: ")
if (username == "admin" and password == "pass"):
    print("success")
else:
    if(username != "admin"):
        print("invalid username")
    else:
        print("invalid password")
