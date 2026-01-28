import os

def clear_terminal():

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


clear_terminal()

print("""
7. Dictionaries
- Create a dictionary
- Access values using keys
- Add new key-value pairs
- Update existing values
- Loop through dictionary items
""")      

dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2025 
}

print(dictionary)
print(type(dictionary))
print(dictionary["brand"])
dictionary['color'] = 'red'
print(dictionary)
dictionary['color'] = 'blue'
print(dictionary)
dictionary['year'] = 2026
print(dictionary)
print(len(dictionary))


print('item keys in dictionary')
for items in dictionary:
    print(items)
print('\n')
print('item values in dictionary')
for value in dictionary.values():
    print(value)
print('\n')
