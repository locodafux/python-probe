print("""
### 4. Conditions
- Use `if / else`
- Check if age is:
  - adult
  - minor
- Create a simple password check
""")

age = input("What is your age: ")


if int(age) >= 18:
    print("adult")
else: 
    print("minor")

user_password = "password"
password = input("Please enter your password: ")

if password == user_password: 
    print("Password is correct")
else:
    print("Password is incorrect")
