#Ziwei Hou Lab 063 zh367
from enemy import enemy

class College(enemy):

    def __init__(self):
        super().__init__()
        self.__name = 'University'
        self.__health = 1000
        self.__defense_mode = False

    def __str__(self):
        return "Hello, we are College University!"

    def getName(self):
        return self.__name

    def getDescription(self):
        return "Welcome to University!"

    def basicAttack(self, enemy):
        self.__defense_mode = False
        enemy.doDamage(24)

    def basicName(self):
        return "University: Takes ten grand."

    def defenseAttack(self, enemy):
        # Defend.
        self.__defense_mode = True

    def defenseName(self):
        return "University: Snowstorm, school is closed."

    def specialAttack(self, enemy):
        # Can't Defend and attack.
        self.__defense_mode = False
        enemy.doDamage(42)

    def specialName(self):
        return "University: Takes all your money."

    def getHealth(self):
        return self.__health

    def healHealth(self):
        pass

    def doDamage(self, damage):
        if self.__defense_mode:
            # Defense Mode Reduces enemy damage by a third.
            self.__health = self.__health - (damage // 3)
        else:
            self.__health = self.__health - damage

    def resetHealth(self):
        self.__health = 1000

    def maxHealth(self):
        return '1000'