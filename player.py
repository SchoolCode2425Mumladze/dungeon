import random

class player:
    def __init__(self):
        self.max_hp = 10
        self.hp = 10
        self.exp = 1
        self.weapon = None
        self.potion = None
    def damage(self, hp):
        self.hp = max(0, self.hp - hp)
    def hill(self, hp):
        self.hp += hp
    def exp_up(self, exp):
        self.exp += exp
