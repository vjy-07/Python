#1
def hello():
    print("hello")
hello()
hello() 

#2
def add(a,b):
    s = a+b
    return s
ans = add(2,3)
print(ans)

#3
def avg(a,b,c):
    average = (a+b+c)/3
    return average
ans = avg(3,4,5)
print(ans)

#4
def fun(a,b=2):
    return a+b
print(fun(3))
print(fun(3,4))