class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
            if isinstance(food, Plant):
                if food.edible:
                    self.fed = True
                    print(f'{self.name} съел {food.name}')
                else:
                    self.alive = False
                    print(f'{self.name} съел {food.name} и отравился')
            else:
                None

    def __str__(self):
        return self.name

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

    def __str__(self):
        return self.name

class herbivore(Animal):
    pass

class carnivore(Animal):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

class Flower(Plant):
    pass


a1 = herbivore('Олень')
a2 = carnivore('Лев')
p1 = Fruit('яблоко')
p2 = Flower('паслен')

print(a1.name)
print(a2.name)
print(p1.name)
print(p2.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.fed)
print(a2.alive)