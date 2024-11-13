class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}.")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}.")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}.")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}.")
            self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

lion = Predator(name="Лев")
deer = Mammal(name="Олень")
rose = Flower(name="Роза")
apple = Fruit(name="Яблоко")

lion.eat(apple)
print(lion.fed, lion.alive)

deer.eat(rose)
print(deer.fed, deer.alive)



