import random
import math


class Monster:
    def __init__(self, name, hp, attack_range):
        self.name = name
        self.hp = hp
        self.attack_range = attack_range


    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def attack(self):
        return random.randint(*self.attack_range)

    def defense_attack(self):
        return round(random.randint(*self.attack_range) * 0.3)

    def sup_attack(self):
        self.super_atat = True

    def super_attack(self):
        self.super_atat = False
        return random.randint(*self.attack_range) * 2
    def defens_super_attack(self):
        self.super_atat = False
        return round((random.randint(*self.attack_range)* 2) * 0.3)

class slime(Monster):
    def __init__(self):
        super().__init__("Слизень", hp=5, attack_range=(1, 1))

class Gobline:
    def __init__(self):
        super().__init__("Гоблин", hp=10, attack_range=(2, 4))







Gobline = Gobline()