try:
    n = int(input("enter a number: "))
    ans = 10/n
except ZeroDivisionError:
    print("Divide by 0 is not allowed")
except ValueError:
    print("Invalid Input")
else:
    print(f"ans = {ans}")