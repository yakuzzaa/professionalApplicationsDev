class Food:
    def __init__(self, weight, *args, **kwargs):
        self.weight = weight


class Animal:
    def __init__(self, weight, height, age):
        self.weight, self.height, self.age = weight, height, age

    def eat(self, food: Food):
        self.weight += food.weight


class Mammal(Animal):
    def __init__(self, weight, height, age, name):
        super().__init__(weight, height, age)
        self.name = name

    def __str__(self):
        return f'Mammal {self.name}'

    def eat(self, food):
        super().eat(food)
        print(f'Mammal {self.name} ate {food}. Now its weight is {self.weight}')


class Human(Animal):
    def __init__(self, weight, height, age, name, sex):
        super().__init__(weight, height, age)
        self.name = name
        self.sex = sex

    def __str__(self):
        return f'Human {self.name}'

    def eat(self, food):
        super().eat(food)
        print(f'Human {self.name} ate {food}. Now its weight is {self.weight}')


def pet(animal: Animal, food: Food):
    print(f'Petting {animal} with {food}')
    animal.eat(food)


if __name__ == '__main__':
    monkey = Mammal(weight=10, height=120, name='Chimp', age=5)
    evolutioned_monkey = Human(weight=60, height=180, name='Kolya', age=20, sex='Male')

    pet(evolutioned_monkey, monkey)
