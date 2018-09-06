# Ziwei Hou CS 171-B, ID: zh367
import sys
import re
print('Welcome to a fun word replacement game.')

#Function that will split the file and ask for inputs. 
def reader():
  splitted = contents.split()
  #The finished story.
  finished = ''
  #Checking for fill-in boxes.
  for index in splitted:
    if index[0] == '[':
	  #Removing dashes.
      c = index.replace('-', ' ')
	  #Checking to see where the ending bracket closes at.
      if c[-1] == ']':
	    #Word inside the fill-in boxes.
        a = c[1:-1]
		#Vowel checker.
        if a[0] == 'a' or a[0] == 'e' or a[0] == 'i' or a[0] == 'o' or a[0] == 'u':
          print('Please give an', a)
		  #Asking for user inputs.
          userinput = input()
          finished = finished + userinput + " "
		#Non-vowel checker.
        elif a[0] != 'a' or a[0] != 'e' or a[0] != 'i' or a[0] != 'o' or a[0] != 'u':
          print('Please give a', a)
          userinput = input()
          finished = finished + userinput + " "
	  #If the fill-in box is next to punctuation, this carries over the punctuation.
      elif c[-1] == ',' or c[-1] == '.':
        a = c[1:-2]
		#Vowel checker.
        if a[0] == 'a' or a[0] == 'e' or a[0] == 'i' or a[0] == 'o' or a[0] == 'u':
          print('Please give an', a)
          userinput = str(input())
		  #Carrying the punctuation.
          userinput2 = userinput + c[-1]
          finished = finished + userinput2 + " "
		#Non-vowel checker.
        elif a[0] != 'a' or a[0] != 'e' or a[0] != 'i' or a[0] != 'o' or a[0] != 'u':
          print('Please give a', a)
          userinput = str(input())
		  #Carrying the punctuation.
          userinput2 = userinput + c[-1]
          finished = finished + userinput2 + " "
	#Adding all the words that are not inside the fill-in boxes.
    else:
      finished = finished + index + " "
	  
  print("Here is your story:\n--------------------")
  print(finished)
  
#Opening and reading the file, and the system exits if it's not found.  
file = input('Enter the name of the file to use:\n')
try:
  valid = True
  contents = open(file).read()
  reader()
except FileNotFoundError as e:
  print('Error Bad File Name')
  sys.exit(0)