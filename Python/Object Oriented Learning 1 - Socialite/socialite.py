#Ziwei Hou zh367 Lab 063
class Socialite:
    #Basic init function to set each parameter and variable to itself.
    def __init__(self,last='',first='',pic='',web='',des='',ID=''):
        self.__last = last
        self.__first = first
        self.__pic = pic
        self.__web = web
        self.__des = des
        self.__ID = ID

    #Coming the strings into the Socialite info format.
    def str(self=None):
        return 'Name:' + ' ' + str(self.__first) + ' ' + str(self.__last) + '\n' \
               + 'User ID:' + ' ' + str(self.__ID) + '\n' \
               + 'Picture:' + ' ' + str(self.__pic) + '\n' \
               + 'Website:' + ' ' + str(self.__web) + '\n' \
               + 'Website Description:' + ' ' + str(self.__des)

    #Methods that will implement the info from inputs upon command.
    def setLastName(self,last):
        self.__last = last

    def setFirstName(self,first):
        self.__first = first

    def setPicture(self,pic):
        self.__pic = pic

    def setWebsite(self,web):
        self.__web = web

    def setDescription(self,des):
        self.__des = des

    def setUserID(self,ID):
        self.__ID = ID

    #Returning each to itself (Accessor Methods)
    def getLastName(self):
        return self.__last

    def getFirstName(self):
        return self.__first

    def getPicture(self):
        return self.__pic

    def getWebsite(self):
        return self.__web

    def getDescription(self):
        return self.__des

    def getUserID(self):
        return self.__ID




