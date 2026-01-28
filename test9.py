print("""### 9. Error Handling
- Use `try / except`
- Handle invalid user input
- Prevent program from crashing
""")

try:
    print(x)
except Exception as e:
    print(e)


try:
    print(x)
except NameError:
    print("Variable x is not defined")

except:
    print("An exception occured")

try: 
    age = int(input("What is your age: "))
    print("Your age is " + str(age))
except Exception as e:
    print(e)
