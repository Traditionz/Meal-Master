import math
def bunnies(rabbits, foxes, years):
    A = 0.04
    B = 0.0005
    G = 0.2
    S = 0.00005
    Lister = []
    for n in range(years):
        tempr = rabbits + math.floor(rabbits * (A-B * foxes))
        tempf = foxes - math.floor(foxes * (G-S * rabbits))
        rabbits = tempr
        foxes = tempf
    Lister.append(rabbits)
    Lister.append(foxes)
    return (rabbits,foxes)
if __name__ == "__main__": 
    print("Welcome to Predator-Prey Model.")
    rabbits = int(input('Enter Initial Rabbit Population:\n'))
    foxes = int(input('Enter Initial Fox Population:\n'))
    years = int(input('Enter Number of Years to Simulate:\n'))
    ans1, ans2 = bunnies(rabbits, foxes, years)
    print('After',years,'years there will be',ans1,'rabbits.')
    print('After',years,'years there will be',ans2,'foxes.')