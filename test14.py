print("""
### 14. Classes (Basics)
- Create a class
- Use `__init__`
- Create objects
- Store and access object data
""")

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)



p1 = Person("Leo", 27)
p2 = Person("Ann", 26)

p1.myfunc()
p2.myfunc()
