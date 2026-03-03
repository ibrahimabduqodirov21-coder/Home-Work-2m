from os import strerror


class Hero:
    def __init__(self, name, lvl, hp, strenght):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strenght = strenght
    def greet(self):
        return f'я {self.name} мой уровен {self.lvl} '
    def attack(self):
        self.strenght -= 1
        return f'{self.name} - наносит удар'
    def rest(self):
        self.hp += 1
        return f'{self.name} - отдыхает '


man = Hero('Man', 1, 100, 100)

Hero1 = Hero('Hero1', 1, 100, 100)
print(Hero1.greet())
print(Hero1.attack())
print(Hero1.rest())

print(man.greet())
print(man.attack())
print(man.rest())

