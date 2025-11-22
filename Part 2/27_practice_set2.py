#1
n=int(input("Enter a number: "))
i=1
while(i<=10):
    print(n*i)
    i=i+1


#2
i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1


#3
word = "apple and apples"
vow = 0
for char in word:
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        vow += 1
print("Number of vowels:", vow)

#4
n = int(input("enter a number: "))
ans = 0;
for i in range(1,n+1):
    ans+=i
print("Sum is:", ans)