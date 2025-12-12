#1
f = open("Part 5/sample.txt", 'a')
f.write("some text appended")
f.close()

#2
f=open("Part 5/sample2.txt", 'x')
f.write("created a new file")
f.close()

#3
f=open("Part 5/sample2.txt", 'r+')
f.write("123")
print(f.read())
f.close()

#4
f=open("Part 5/sample2.txt", 'w+')
f.write("123")
print(f.read())
f.close()


#5
f=open("Part 5/sample2.txt", 'a+')
f.write("123")
print(f.read())
f.close()