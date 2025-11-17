#1
salary = int(input("Enter your  salary: "))
if salary< 30000:
    tax = salary * 5/100
elif salary>=30000 and salary<=70000:
    tax = salary * 15/100
else:
    tax = salary * 25/100
print("tax is :", tax)


#2
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
for i in range (num1, num2+1):
    if(i%2==0):
        print(i)

#3
def digits(n):
    while n>0:
        digit = n%10
        print(digit)
        n=n//10
n = int(input("enter a number: "))
print(digits(n))


#4
def digcount(n):
    count =0
    while n>0:
        digit = n%10
        count+=1
        n=n//10
    return count
n=int(input("enter a number: "))
print("count is: ",digcount(n))

#5
def sumofdig(n):
    sum=0
    while n>0:
        digit = n%10
        sum+=digit
        n=n//10
    return sum
n=int(input("enter a number: "))
print("sum is: ",sumofdig(n))


#6
for i in range(1, 101):
    if i%3==0 and i%5==0:
        print(i)
        
#7
while(True):
    n=input("enter a number:")
    if( n == "quit"):
        break
    if int(n)<0:
        print("negative number")
    else:
        print("positive number")
    
    
#8
def calculator(a,b, operation):
    match operation:
        case "add":
            return a+b
        case "sub":
            return a-b
        case "mul":
            return a*b
        case "div":
            return a/b
        case _:
            return "invalid operation"
a = int(input("enter first number: "))
b = int(input("enter second number: "))
operation = input("enter operation (add, sub, mul, div): ")
print("result is: ", calculator(a,b,operation))

#9
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input("enter a number: "))
print(is_prime(n))

#10
secret_number = 7
while True:
    guess = int(input("guess the number : "))
    if guess > secret_number:
        print("too high")
    elif guess < secret_number:
        print("too low")
    else:
        print("congratulations! you guessed it right.")
        break