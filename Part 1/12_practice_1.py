#1
name = input("enter your name: ")
age = (input("enter your age: "))
print("hello "+ name + ", you are " + age + " years old!")

#2
a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("sum: ", a+b)
print("difference: ", a-b)
print("product: ", a*b)
print("quotient: ", a/b)

#3
val = input("enter a value: ")
print(int(val), type(int(val)))
print(float(val), type(float(val)))
print(str(val),type(str(val)))

#4
print(10+3*2**2)

#5
a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("before swapping: a =", a, "b =", b)
a = a+b
b = a-b
a = a-b
print("after swapping: a =", a, "b =", b)

#6
temp = input("enter temperature in celsius: ")
temp = float(temp)
f = (temp * (9/5)) + 32
print("temperature in fahrenheit: ", f)

#7
radius = int(input("enter radius of circle: "))
area = 3.14 * radius **2
print("area of circle: ", area)

#8
p = float(input("enter principal amount: "))
r = float(input("enter rate of interest: "))
t = float(input("enter time in years: "))
print("S.I : ", (p*r*t)/100)

#9
val = float(input("enter a number: "))
integer_part = int(val)
decimal_part = val - integer_part
decimal_part = round(decimal_part, 2)
print("integer part: ", integer_part)
print("decimal part: ", decimal_part)
