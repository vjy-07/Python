# 1
age = int(input("enter your age: "))

if(age>=18):
    print("you can vote")
    print("you can drive")
else:
    print("Not eligible to vote")

# 2
color = input("enter the color: ")

if(color == 'red'):
    print("stop")
elif(color == 'yellow'):
    print("get ready")
elif(color == 'green'):
    print("go")
else:
    print("invalid color")
    
# 3
age = int(input("enter your age: "))

if(age<13):
    print("child")
elif(age>=13 and age<18):
    print("teenager")
else: 
    print("adult")

# 4
username = input("enter username: ")
password = input("enter password: ")

if(username == "admin" and password == "1234"):
    print("login successful")
elif(username != 'admin'):
    print("incorrect username")
else: 
    print("incorrect password")
     
# 5
n = int(input("enter a number: "))
if(n%5 == 0):
    print("divisible by 5")
else:
    print("not divisible by 5")
