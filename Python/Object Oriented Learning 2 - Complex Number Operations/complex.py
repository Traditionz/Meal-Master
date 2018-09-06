#Ziwei Hou zh367 CS172-063

class ComplexNumber:

    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y

    # Returns the string in complex number form without the '+' if it's negative, else '+'.
    def __str__(self):
        if self.__y < 0:
            return "{:}{:}i".format(self.__x,self.__y)
        else:
            return "{:}+{:}i".format(self.__x,self.__y)

    # Returns the string without the "i". It COULD BE returning self.__x=x instead.
    def getReal(self):
        return "{:}+{:}".format(self.__x,self.__y)

    # Returns the string with the "i". It COULD BE returning self.__y=y instead.
    def getImaginary(self):
        return "{:}+{:}i".format(self.__x,self.__y)

    # From the given formula, we add the two numbers, then we return it so we can get te complex version.
    def __add__(self, other):
        a = other.__x + self.__x
        b = other.__y + self.__y
        return ComplexNumber(round(a,2),round(b,2))

    # From the given formula, we subtract the two numbers, then we return it so we can get te complex version.
    def __sub__(self, other):
        a = other.__x - self.__x
        b = other.__y - self.__y
        return ComplexNumber(round(a,2),round(b,2))

    # From the given formula, we multiply the two numbers, then we return it so we can get te complex version.
    def __mul__(self, other):
        a = (other.__x * self.__x) - (other.__y * self.__y)
        b = (other.__x * self.__y) + (other.__y * self.__x)
        return ComplexNumber(round(a,2),round(b,2))

    # From the given formula, we divide the two numbers, then we return it so we can get te complex version.
    def __truediv__(self, other):
        a = ((other.__x * self.__x) + (other.__y * self.__y)) / ((other.__x ** 2) + (other.__y ** 2))
        b = ((-1 * other.__y * self.__x) + (other.__x * self.__y)) / ((other.__x ** 2) + (other.__y ** 2))
        return ComplexNumber(round(a,2),round(b,2))

    # From the given formula, we raise a complex number to a power n or 'other' times.
    def __pow__(self, other):
        c = ComplexNumber(1,0)
        for i in range(other):
            c *= self
        return c

# Test Runs from pdf.
if __name__ == "__main__":
    c1 = ComplexNumber(4,3)
    c2 = ComplexNumber(2,8)
    print(c1)
    print(c1 + c2)
    print(c1-c2)
    print(c1 * c2)
    print(c1 / c2)
    print(c1 ** 3)