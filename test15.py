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
