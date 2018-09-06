#Ziwei Hou Lab 063 zh36
import abc

class enemy(metaclass=abc.ABCMeta):

    def __init__(self):
        return

    def __str__(self):
        return "Generic Monster Class"

    def getName(self):
        pass

    @abc.abstractmethod
    def getDescription(self):
        pass

    # Allows enemy to attack another with basic attack (common occurrence).
    @abc.abstractmethod
    def basicAttack(self, enemy):
        pass

    # Name of the basic attack.
    @abc.abstractmethod
    def basicName(self):
        pass

    # Allows enemy to attack another with special attack (rare occurrence).
    @abc.abstractmethod
    def specialAttack(self, enemy):
        pass

    # Name of the special attack.
    @abc.abstractmethod
    def specialName(self):
        pass

    # Can't defend while attacking
    @abc.abstractmethod
    def defenseAttack(self, enemy):
        pass

    # Name of defense move
    @abc.abstractmethod
    def defenseName(self):
        pass

    # Get the Values of Health
    @abc.abstractmethod
    def getHealth(self):
        pass

    # Allows enemy to be damaged by another.
    @abc.abstractmethod
    def doDamage(self, damage):
        pass

    # Health reset before next enemy encounter.
    @abc.abstractmethod
    def resetHealth(self):
        pass

    # If the hero heals, this enables him to heal
    @abc.abstractmethod
    def healHealth(self):
        pass