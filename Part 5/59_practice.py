data = True
line = 1
word = "python"
with open("Part 5/practice.txt", 'r') as f:
    while data:
        data=f.readline()
        if(word in data):
            print(f"{word} found at line {line}")
            break
        
        line +=1
           