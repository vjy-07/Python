sq = [i*i for i in range(6)]
print(sq)

odd = [i*i for i in range(6) if i%2!=0]
print(odd)

list1 = [-1,2,-3,4,-5,6]
list1 = [0 if i<0 else i for i in list1]
print(list1)

words = ["hello", "python"]
words = [i.upper() for i in words]
print(words)