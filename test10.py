print("""
10. Files
- Create a `.txt` file
- Write data to file
- Read data from file
- Append new data to file
""")

file_path = "new_file.txt"
content = "Hello World"

try:
    with open(file_path, 'w') as file:
        file.write(content)
    print("file created")
except Exception as e: 
    print(e)

print("Read data from file")

try:
    with open(file_path, 'r') as file:
        file_content = file.read()
    print(file_content)
except Exception as e: 
    print(e)


print("Append new data to file ")
forAppendContent = 'Hello Leo'

try:
    with open(file_path, 'a') as file:
       file.write('\n' + forAppendContent)
    print("appended a content to the file")
except Exception as e: 
    print(e)

print("Reading the file again.")

try:
    with open(file_path, 'r') as file:
        file_content = file.read()
    print(file_content)
except Exception as e: 
    print(e)
