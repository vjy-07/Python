a=5
b=10
sum=a+b

print("language is: {}".format("python"))
print("sum is: {}".format(sum))
print("sum of {} & {} is {}".format(a,b,sum))

#index based
print("sum of {1} & {0} is {2}".format(a,b,sum))

#value based
print("values are {a} and {b}".format(a=10, b=20))

#f-string
print(f"sum of {a} and {b} is {a+b}")