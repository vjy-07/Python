info=[
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie","Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

s=set()
for i in info:
    s.add(i[1])
print(s)
    
for name, course in info:
    if(course=="English"):
        print(name)

dict = {}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)