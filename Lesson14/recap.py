class animal():
    count = []

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        self.count.append(name)

    def get_number_animals(self):
        return len(self.count)

class dog(animal):
    def __init__(self, name, age, pow):
        super().__init__(name, age)
        self.pow = pow

    def communicate(self):
        return "Wuff"

class fish(animal):
    def __init__(self, name, age, fin):
        super().__init__(name, age)
        self.fin = fin


#animals = [animal("bello", 23), animal("goldi", 4)
a = dog("Bello", 23, 4)
b = fish("Goldi", 4, 8)


print(a.get_number_animals())
print(b.name)
print(a.communicate())