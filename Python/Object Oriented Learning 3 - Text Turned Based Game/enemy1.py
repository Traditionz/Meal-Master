#Ziwei Hou Lab 063 zh367
from enemy import enemy

class AssistantProfessor(enemy):

    def __init__(self):
        super().__init__()
        self.__name = "Alan Einstein"
        self.__health = 500
        self.__defense_mode = False

    def __str__(self):
        return "I am a Professor named {}. Be prepared to fail.".format(self.__name)

    def getName(self):
        return self.__name

    def getDescription(self):
        return "This Professor loves to study."

    def basicAttack(self, enemy):
        self.__defense_mode = False
        enemy.doDamage(10)

    def basicName(self):
        return "Alan Einstein: Gives you an F on a test."

    def defenseAttack(self, enemy):
        # Defend.
        self.__defense_mode = True

    def defenseName(self):
        return "Alan Einstein: Goes to his office to grade some assignments."

    def specialAttack(self, enemy):
        # Can't Defend and attack.
        self.__defense_mode = False
        enemy.doDamage(20)

    def specialName(self):
        return "Alan Einstein: Fails you with a 0/100 in his class."

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
        self.__health = 500

    def maxHealth(self):
        return '500'