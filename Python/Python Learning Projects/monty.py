#Ziwei Hou, Lab 068, ID: zh367
import random

#The while loop is to test if the user entered any incorrect values for seed1.
seed1 = input('Enter Random Seed:\n')
valid1 = False
while not valid1:
  try:
    n = int(seed1)
    valid1 = True
    random.seed(seed1)
  except ValueError as e:
    print('Your input for Seed is a not a number!')
    seed1 = input('Enter Random Seed:\n')
print('Welcome to the Monty Hall Analysis')
print("Enter 'exit' to quit.")

# The standard list for GOAT, GOAT, and CAR.
L = ['G', 'G', 'C']

#Global variables to calculate which door is picked by who AND the number of switch/stay wins to calculate percentages.
StayWins = 0
SwitchWins = 0
monty = 0
player = 0

#The action function shuffles the doors while randomly picking a number for monty and the player.
def action():
  random.shuffle(L)
  print('Doors:', L)
  global monty
  global player
  player = random.randint(1,3)
  monty = random.randint(1,3)
  valid3 = False
  while not valid3:
  #The player door cannot be the same as monty's door, so it loops until they are not equal.
    if player != monty:
      valid3 = True
      valid4 = False
      while not valid4:
	  #This converts the integers from [1 to 3] to [0 to 2] in order to follow the order of list "L".
        if L[monty - 1] != 'C':
          monty = monty - 1
          player = player - 1
          valid4 = True
        else:
          monty = random.randint(1,3)
    else:
      monty = random.randint(1,3)
  #This prints the door monty and the player selected.
  print('Player Selects Door', player+1)
  print('Monty Selects Door', monty+1)
  #This check to see if monty picked a door that is not car, since monty can only pick a door of the goat.
  if L[player] == 'G':
    global SwitchWins
    SwitchWins = SwitchWins + 1
    print('Player should switch to win.')
  else:
    global StayWins
    StayWins = StayWins + 1
    print('Player should stay to win.')

#This function performs the test as many times the user wants.
def tries():
  for x in range(0,int(test)):
    print('Game', x+1)
    action()

#This contains all the other functions and prints out the results of the tests the user has entered.
def do():
  tries()
  staypercent = StayWins / int(test) * 100
  switchpercent = SwitchWins / int(test) * 100
  print('Stay Won', round(staypercent,2), '% of the time.')
  print('Switch Won', round(switchpercent,2), '% of the time.')

#This while loop resets the global variables for further tests, checks for input errors, and exits upon the exact word(case-sensitive): 'exit'.
valid5 = False
while not valid5:
  StayWins = 0
  SwitchWins = 0
  monty = 0
  player = 0
  test = input('How many tests should we run?\n')
  if test == 'exit':
    exit()
  valid2 = False
  while not valid2:
    try:
      n = int(test)
      valid2 = True
      do()
    except ValueError as e:
      test = input('Please enter a number:\n')