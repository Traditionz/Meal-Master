#Ziwei Hou Lab 063 zh367
from enemy import enemy

class hero(enemy):

    def __init__(self,name="Bob The Builder"):
        super().__init__()
        self.__name = name
        self.__health = 500
        self.__defense_mode = False

    def __str__(self):
        pass

    def getName(self):
        return self.__name

    def getDescription(self):
        return 'You are a courageous hero who paid for college. Good luck out there.'

    def basicAttack(self, enemy):
        self.__defense_mode = False
        enemy.doDamage(200)

    def basicName(self):
        return "Procrastinate Attack!"

    def defenseAttack(self, enemy):
        # Defend.
        self.__defense_mode = True

    def defenseName(self):
        return "Go home and take a nap."

    def specialAttack(self, enemy):
        # Can't Defend and attack.
        self.__defense_mode = False
        enemy.doDamage(350)

    def specialName(self):
        return "Study Attack!"

    def getHealth(self):
        return self.__health

    def healHealth(self):
        if self.__health >= 350:
            self.__health = 500
        elif self.__health < 350:
            self.__health += 150

    def doDamage(self, damage):
        if self.__defense_mode:
            # Defense Mode Reduces enemy damage by a third.
            self.__health = self.__health - (damage // 3)
        else:
            self.__health = self.__health - damage

    def resetHealth(self):
        self.__health = 500
