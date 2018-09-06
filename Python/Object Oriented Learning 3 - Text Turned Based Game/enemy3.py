#Ziwei Hou Lab 063 zh367
from enemy import enemy

class TeachingAssistant(enemy):

    def __init__(self):
        super().__init__()
        self.__name = "Mr. Krabs"
        self.__health = 450
        self.__defense_mode = False

    def __str__(self):
        return "Hello, I'm Mr. Crabs, and I'll be helping you today."

    def getName(self):
        return self.__name

    def getDescription(self):
        return "This Teaching Assistant just wants to get paid."

    def basicAttack(self, enemy):
        self.__defense_mode = False
        enemy.doDamage(9)

    def basicName(self):
        return "Mr. Krabs: Gives you that look."

    def defenseAttack(self, enemy):
        # Defend.
        self.__defense_mode = True

    def defenseName(self):
        return "Mr. Krabs: Goes to the bathroom for 45 minutes."

    def specialAttack(self, enemy):
        # Can't Defend and attack.
        self.__defense_mode = False
        enemy.doDamage(18)

    def specialName(self):
        return "Mr. Krabs screams: 'Why don't you understand this?'"

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
        self.__health = 450

    def maxHealth(self):
        return '450'