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

