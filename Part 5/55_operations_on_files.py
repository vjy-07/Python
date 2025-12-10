f= open("Part 5/sample.txt",'r')

data = f.read()
print(data)

data1 = f.readline()
print(data1)

f.close()

f=open("Part 5/sample.txt",'w')
f.write("file is overwritten")
f.close()
