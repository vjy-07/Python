import json

d={
    "name":"Vijay",
    "age": 5,
    "isStudent": True
}

with open("Part 5/data.json",'r') as f:
    py_obj = json.load(f)
    print(py_obj)
    
with open("Part 5/data.json",'w') as f1:
    json.dump(d,f1, indent = 4, sort_keys=True)