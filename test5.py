print("""
### 5. Lists
- Create a list of items
- Access items by index
- Add items to a list
- Remove items from a list
- Count list length
---
""")
print("- Create a list of items")
frutLists = ['apple', 'orange']
print(type(frutLists))
print(frutLists)
print("- Access items by index")
print(frutLists[1])
print("- Add items to a list: kiwi")
frutLists.append('kiwi')
print(frutLists)
print("- Remove items from a list: apple")
frutLists.remove('apple')
print(frutLists)
print("- Count list length")
print(len(frutLists))
print("- Loop through the list")
for fruit in frutLists:
    print(fruit)
