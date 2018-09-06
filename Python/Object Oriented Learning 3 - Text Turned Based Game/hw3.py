#Ziwei Hou Lab 063 zh367
#Importation of the classes
from hero import hero
from enemy1 import AssistantProfessor
from enemy2 import Professor
from enemy3 import TeachingAssistant
from enemy4 import College
import random

def battle(m1,m2):
    # Just so it is easier to identify later on (The Hero or Enemy).
    attacker = m1
    defender = m2

    # Hero's potion and special attack respectively.
    food = 6
    study = 10

    # Next print out who the hero is battling.
    print("You have encountered {}!".format(m2.getName()))
    print(str(m1.getName()) + ": " + str(m1.getDescription()))
    print('VERSUS')
    print(str(m2.getName()) + ": " + str(m2.getDescription()))

    # Loop until either one is unconscious or timeout.
    healthloop = True
    while m1.getHealth() > 0 and m2.getHealth() > 0:

        # If heal goes below 0, it rounds to 0, else, print the normal health value.
        if m1.getHealth() <= 0:
            print('{}: 0/500 health'.format(heroname))
        else:
            print('{}: {}/500 health'.format(heroname, m1.getHealth()))

        # Print the enemy's total health once at the beginning of each fight.
        while healthloop:
            print('{}: {}/{} health'.format(m2.getName(), m2.getHealth(), m2.maxHealth()))
            healthloop = False

        # Number of food and special attacks left.
        print('Remaining: {} Study sessions, {} servings of food'.format(study, food))
        # Telling the player what each move does.
        print('KEY: procrastinate: basic attack(SWORD), sleep: defend(SHEILD), study: special attack(FIREBALL), food: heal(POTION), exit: exit the game')
        # Asking for player inputs and attack/defend/heal/exit depending on specific values.
        command = input('Enter Command: procrastinate sleep study food exit\n')
        if command == 'procrastinate':
            print('ATTACKED WITH PROCRASTINATION!')
            attacker.basicAttack(defender)
            if m2.getHealth() <= 0:
                print('{}: 0/{} health'.format(m2.getName(), m2.maxHealth()))
            else:
                print('{}: {}/{} health'.format(m2.getName(), m2.getHealth(), m2.maxHealth()))
        elif command == 'sleep':
            print('DEFENDED BY SLEEPING!')
            attacker.defenseAttack(defender)
            print('{}: {}/{} health'.format(m2.getName(), m2.getHealth(), m2.maxHealth()))
        elif command == 'study':
            if study > 0:
                print('YOU ATTACKED BY STUDYING!')
                attacker.specialAttack(defender)
                if m2.getHealth() <= 0:
                    print('{}: 0/{} health'.format(m2.getName(),  m2.maxHealth()))
                else:
                    print('{}: {}/{} health'.format(m2.getName(), m2.getHealth(), m2.maxHealth()))
                study -= 1
            else:
                print('You ran out of study sessions and wasted your turn!')
        elif command == 'food':
            if food > 0:
                print('YOU ATE SOME FOOD!')
                attacker.healHealth()
                print('{}: {}/{} health'.format(m2.getName(), m2.getHealth(), m2.maxHealth()))
                food -= 1
            else:
                print('You ran out of food and wasted your turn!')
        # Exit if they type exit.
        elif command == 'exit':
            print('Thanks for playing!')
            exit()
        # If they type wrong values, they wasted their turn.
        else:
            print('Invalid Command! You wasted your turn!')
            print('{}: {}/{} health'.format(m2.getName(), m2.getHealth(), m2.maxHealth()))

        # While enemy is alive
        if m2.getHealth() > 0:
        # Enemy Attack Statistics
        # 60% chance of standard attack
        # 20% chance of defense move
        # 20% chance of special attack move
            move = random.randint(1, 100)
            if move >= 1 and move <= 60:
                # Attacker uses basic attack on hero!
                defender.basicAttack(attacker)
                print(defender.basicName())
            elif move >= 61 and move <= 80:
                # Defend!
                defender.defenseAttack(attacker)
                print(defender.defenseName())
            else:
                # Special Attack!
                defender.specialAttack(attacker)
                print(defender.specialName())
        # If enemy is death return the winner, else they lose.
        elif m2.getHealth() <= 0:
            return heroname
        else:
            return 'You lost!'

if __name__ == "__main__":
    print('Welcome to Adventure Battle!')

    # Name of hero.
    heroname = str(input('What is the name of your hero?\n'))

    # Asking for number of monster battles.
    monsternum = input('How many monsters will {} battle?\n'.format(heroname))
    while True:
        try:
            monsternum = int(monsternum)
            print('')
            break
        except ValueError:
            continue

    # Four enemies in the list.
    enemy_list = [1, 2, 3, 4]

    random.seed(0)
    # Randomly shuffles the enemy order.
    random.shuffle(enemy_list)

    # Remove the amount of enemies from the list until it reaches the number of enemies they want to fight.
    for n in range(4-monsternum):
        enemy_list.remove(enemy_list[0])

    Mob = None
    # For each number, each enemy corresponds to a number. Then they fight until they reach the end of the list.
    for opponent in enemy_list:
        # RESETS HERO AFTER KILLING AN ENEMY.
        Player = hero(heroname)
        if opponent == 1:
            Mob = AssistantProfessor()
        elif opponent == 2:
            Mob = Professor()
        elif opponent == 3:
            Mob = TeachingAssistant()
        elif opponent == 4:
            Mob = College()
        winner = battle(Player, Mob)
        # If player wins, it prints out the winner.
        if winner == heroname:
            print('Enemy is defeated!')
            print('')
        # Else, it prints you died.
        else:
            print('You died.')
            exit()

    print('You have defeated all enemies and graduated. Good Job.')