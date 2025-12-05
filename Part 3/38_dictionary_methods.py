info = {
    "name": "john",
    "age": 21,
    "sub":["math","phy","che"]
}
print(info)

print(info.keys())
print(list(info.keys()))

print(info.values())
print(list(info.values()))

print(list(info.items()))

print(info.get("age"))
print(info.get("age2")) #no error (None)

info.update({"city":"delhi"})
print(info)