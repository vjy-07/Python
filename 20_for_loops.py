# 1
string = "vijay"
for char in string:
    print(char)


# 2
string = "hello"
if "o" in string:
    print("found")


# 3
for i in range(5):
    print(i+1)

# 4
word = "artificial intelligence"

count = 0
for i in word:
    if(i=="i"):
        count +=1
print("count of i is: ",count)

# 5
word = "artificial"
count = 0
for i in word:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print("vowel count: ",count)