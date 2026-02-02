import json

print("""
### 15. JSON
- Convert dictionary to JSON
- Save JSON to file
- Read JSON from file
- Use JSON as data storage
""")

data = {
        "name": "Leo",
        "age": 27,
        "skills":["Python", "FastAPI"],
        "is_active": True
}

#with open("data.json", "w") as file:
#    json.dump(data, file)


with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file) 

data['favorites'] = "Coding"

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file) 
    
del data['favorites']
print(data)

with open("data.json", "w") as file:
    data = json.dump(data, file, indent=4)


