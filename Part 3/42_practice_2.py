#1
s=input("enter a string: ")
s1 = s[::-1]
if(s==s1):
    print("palindrome")
else:
    print("not a palindrome")
    
#2
lst = [1,2,3,4,5,6]
total=0
for i in lst:
    total += i
print(total/len(lst))

#3
l1 = list(map(int, input("enter list1 elements: ").split()))
l2 = list(map(int, input("enter list2 elements: ").split()))

res = l1+l2
res.sort()
print(res)

#4
t = (1,2,3,4,5,6,7,8,9)
even=[]
odd=[]
for i in t:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(tuple(even))
print(tuple(odd))

#5
students = {}

while True:
    print("\nMENU")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    # A - Add a student
    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    # B - Update marks
    elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found!")

    # C - Search for a student
    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} → {students[name]} marks")
        else:
            print("Student not found!")

    # D - Display all students
    elif choice == 'D':
        if len(students) == 0:
            print("No students in the list.")
        else:
            print("\nSTUDENT RECORDS:")
            for name, marks in students.items():
                print(f"{name} : {marks}")

    # Exit option
    elif choice == 'E':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter A, B, C, D, or E.")

#6
words =["apple","banana","kiwi","cherry","mango"]
dict = {}
for i in words:
    dict[i]=len(i)
print(dict)

7
n = input("enter a string: ")
spaces=0
for i in n:
    if(i == " "):
        spaces += 1
print(spaces)

#8
list1 = list(map(int, input("enter list1 elements: ").split()))
list2 = list(map(int, input("enter list2 elements: ").split()))

list1 = set(list1)
list2 = set(list2)

if list1.intersection(list2):
    print("common elements present")
else:
    print("no common elements")

#9
l1 = [1,2,2,3,4,5,5]
s = set()
d = set()

for i in l1:
    if i in s:
        d.add(i)
    else:
        s.add(i)
if d:
    print(d)
else:
    print("no duplicates found")

#10
n = input("enter a string: ")
chars = []
for i in n:
    if i!=" ":
        chars.append(i)
s = set(chars)
print(s)
print(len(s))