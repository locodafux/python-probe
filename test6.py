import os

def clear_terminal():

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    print(os.name)

clear_terminal()
print("""
6. Loops
- Use `for` loop
- Loop through a list
- Use `range()`
- Print numbers 1–10
- Print all items in a list
""")

fruitLists = ['apple', 'orange']

for fruits in fruitLists:
    print(fruits + " fruit")

x = range(1, 11)

for n in x:
    print(n)
