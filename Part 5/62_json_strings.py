import json

json_str = '{"name": "Vijay","course": "Python"}'
py_obj = json.loads(json_str) #string to pyobject
print(py_obj)
print(type(py_obj))


py_object = {
    "name": "Vijay",
    "isEligible": True
}
json_string = json.dumps(py_object) #pyobj to string
print(type(json_string),json_string)

