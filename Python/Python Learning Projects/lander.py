# Ziwei Hou CS 171-B, ID: zh367
import sys
print('Welcome to Lunar Lander Game.')
#The level players will start on, it'll add one for each level complete.
next_level = 1
#The variables to calculate the altitude and velocity of the rocket.
f = 0
A = 50
V = 0
s = 0
T = 0.1
current_fuel = 0
Gravity = 0
#Variables for the while loops.
valid = False
valid5 = False
#This function checks for valid fuel inputs, computes altitude/velocity, updates levels, and loops it until Altitude becomes 0.
#Only accessible through the previous function, play_level.
def ask_fuel(current_fuel):
  global f
  global valid
  global s
  global T
  global V
  global A
  global Gravity
  global valid
  global next_level
  valid = False
  #While loop for fuel inputs.
  while not valid:
    f = input('Enter the number of fuel to burn:\n')
    valid2 = False
    while not valid2:
      try:
        f = int(f)
		#Fuel inputs cannot be greater than current fuel or less than zero.
        while f > current_fuel or f < 0:
          print("Please enter the fuel as a positive integer that's less or equal to Remaining Fuel.")
          f = int(input('Enter the number of fuel to burn:\n'))
        valid2 = True
		#If Altitude is not 0, it keeps updating and computing for Altitude and Velocity.
        while A != 0:
          current_fuel = current_fuel - f
          V = V + Gravity + (T * f)
          A = A + V
          s = s + 1
          print('After',s,'second(s), Altitude is',round(A,2),'meter(s), velocity is',round(V,2),'m/s.')
          print('Remaining Fuel:',current_fuel,'units.')
		  #If Altitude if above zero and velocity is not in the safe zone of -2m/s and 2m/s, then the variables reset and it crashes.
          if A <= 0 and (V < -2 or V > 2):
            print('Crashed!')
            s = 0
            V = 0
            A = 50
            return
		  #If Altitude is above zero and velocity is in the safe zone of -2m/s and 2m/s, then the variables reset and it lands.
          elif A <= 0 and (V > -2 or V < 2):
            print('Landed Successfully.')
            s = 0
            V = 0
            A = 50
			#Levels increase so players can move on.
            next_level += 1
            return
          f = int(input('Enter the number of fuel to burn:\n'))
		  #Makes sure you write a correct fuel amount in between the range of current fuel and 0.
          while f > current_fuel or f < 0:
            print('Please enter the fuel as a positive integer and less or equal to what you have.')
            f = int(input('Enter the number of fuel to burn'))
	  #Checks for string inputs.	
      except ValueError as e:
        print('Please enter the fuel as a positive integer.')
        f = input('Enter the number of fuel to burn')
#Prints the background information for each level.
def play_level(name,G,fuel):
  global current_fuel
  global Gravity
  global ask_fuel
  print('Entering Level', next_level)
  print('Landing on the', name)
  print('Gravity is',G,'m/s^-2')
  print('Initial Altitude:',round(A,2),'meters')
  print('Initial Velocity:',round(float(V),2),'m/s')
  print('Burning a unit of fuel causes',T,'m/s slowdown.')
  print('Initial Fuel Level:',fuel, 'units')
  print('\nGO')
  #Sets global variables to each level's parameters.
  current_fuel = fuel
  Gravity = G
  ask_fuel(current_fuel)
  #If the player beats all the levels, they win and system will exit.
  if next_level > 11:
    print('Congratulations, you beated the game!\nBye!')
    valid5 = True
    sys.exit()
  return
#This function will set the parameters according to each level, it will be called from the while loop at the bottom.
def do():
  if next_level == 1:
    play_level('Moon',-1.622,150)
    return
  elif next_level == 2:
    play_level('Earth',-9.81,5000)
    return
  elif next_level == 3:
    play_level('Pluto',-0.42,1000)
    return
  elif next_level == 4:
    play_level('Neptune',-14.07,1000)
    return
  elif next_level == 5:
    play_level('Uranus',-10.67,1000)
    return
  elif next_level == 6:
    play_level('Saturn',-11.08,1000)
    return
  elif next_level == 7:
    play_level('Jupiter',-25.95,1000)
    return
  elif next_level == 8:
    play_level('Mars',-3.77,1000)
    return
  elif next_level == 9:
    play_level('Venus',-8.87,1000)
    return
  elif next_level == 10:
    play_level('Mercury',-3.59,1000)
    return
  elif next_level == 11:
    play_level('Sun',-274.13,50000)
    return
#This while loop asks the player if they want to play before the game and after each level.
while not valid5:
  print('Do you want to play level', next_level,'? (yes/no)')
  decision = input()
  while decision != 'yes' and decision != 'no':
    print('Please type exactly "yes" or "no".')
    print('Do you want to play level', next_level,'? (yes/no)')
    decision = input()
  if decision == 'no':
    print('You made it past',next_level-1,'level(s).', '\nThanks for Playing.')
    exit()
  elif decision == 'yes':
    do()


