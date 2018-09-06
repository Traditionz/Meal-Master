#Ziwei Hou Lab 063 zh367
from enemy import enemy

class Professor(enemy):

    def __init__(self):
        super().__init__()
        self.__name = "Albert Turing"
        self.__health = 625
        self.__defense_mode = False

    def __str__(self):
        return "I am not Professor {}, I am Dr. {}".format(self.__name,self.__name)

    def getName(self):
        return self.__name

    def getDescription(self):
        return "This Professor is loves to give lectures."

    def basicAttack(self, enemy):
        self.__defense_mode = False
        enemy.doDamage(15)

    def basicName(self):
        return "Albert Turing: Gives you a six hour lecture."

    def defenseAttack(self, enemy):
        # Defend
        self.__defense_mode = True

    def defenseName(self):
        return "Albert Turing: Goes to Lunch Break."

    def specialAttack(self, enemy):
        # Can't Defend and attack.
        self.__defense_mode = False
        enemy.doDamage(21)

    def specialName(self):
        return "Albert Turing: Gives you a ten hour Final."

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
        self.__health = 625

    def maxHealth(self):
        return '625'