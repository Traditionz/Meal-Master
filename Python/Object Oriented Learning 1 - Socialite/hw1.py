#Ziwei Hou zh367 Lab 063
#Importing the Socialite class from socialite.py
from socialite import Socialite

#Function that will run everything.
def action():
    #Creating an empty list to store the socialites.
    set = []
    #For how many number of socialites the user wants to create, this will loop.
    for n in range(0, num):
        print('Enter Data for Socialite', n+1)
        first = input('Enter First Name:\n')
        last = input('Enter Last Name:\n')
        ID = input('Enter ID:\n')
        pic = input('Enter URL for Picture:\n')
        web = input('Enter URL for website:\n')
        des = input('Enter Website Description:\n')
        #Setting Socialite data through the methods.
        Me = Socialite()
        Me.setLastName(last)
        Me.setFirstName(first)
        Me.setUserID(ID)
        Me.setPicture(pic)
        Me.setWebsite(web)
        Me.setDescription(des)
        #Storing the information from the str method into a variable.
        info = Me.str()
        #Appending the variable into the list.
        set.append(info)
        print('Socialite Created.')
        print('')
    print('=====Socialite Information=====')
    #For each item in the set, it will print out each socialite information.
    for each in set:
        print(each)
        print('')


print('Welcome to CS 172: Socialite Homework')
#While loop for invalid integer inputs.
num = input('How many Socialites do you want to create?\n')
print('')
valid = False
while not valid:
    try:
        num = int(num)
        valid = True
        #Calling to run the function.
        action()
    except ValueError as e:
        print('Please enter an integer.')
        num = input('How many Socialites do you want to create?\n')
