import json

# JSON string
json_str = '{"name": "Uzair", "age": 30, "city": "Lahore"}'

# json.loads: Deserialize JSON string to a Python object
python_obj = json.loads(json_str)

# json.load: Deserialize JSON from a file-like object
with open('data.json', 'r') as file:
    json_obj = json.load(file)

# json.dump: Serialize Python object to JSON and write to a file
python_obj = {"name": "Uzair", "age": 30, "city": "Lahore"}
with open('data.json', 'w') as file:
    json.dump(python_obj, file)

# json.dumps: Serialize Python object to JSON string
python_obj = {"name": "Uzair", "age": 30, "city": "Lahore"}
json_str = json.dumps(python_obj)
