
# example of a builder class
class Cat:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def meow(self):
        print('meow')

    def howold(self):
        print(f'age is {self.age}')

c = Cat('freya', 12)
c.meow()
c.howold()

class CatBuilder:
    
    def __init__(self):
        self.isBuilt = False

    def addName(self, name: str):
        self.name = name

    def addAge(self, age: int):
        self.age = age

    #def addisBuilt(self):
    #    self.isBuilt = False

    def build(self):
        if (self.isBuilt == True):
            raise Exception
        self.isBuilt = True
        return Cat(self.name, self.age)

builder = CatBuilder()
builder.addAge(12)
builder.addName('Freya')
cat2 = builder.build()

cat2.meow()
cat2.howold()


cat3 = builder.build()
