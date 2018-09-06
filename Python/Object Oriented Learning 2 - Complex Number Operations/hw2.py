#Ziwei Hou zh367 CS172-063
import complex
import sys

# Setting the Complex number as z from arguments 1 and 2 from the terminal/command.
z = complex.ComplexNumber(float(sys.argv[1]), float(sys.argv[2]))
# Setting the third argument as y
y = int(sys.argv[3])
# Setting the number 1 as a complex number or else you'll get an error when you multiply an int and complex number.
one = complex.ComplexNumber(1,0)

# Defining a from the formula, where c grabs from z and k is the number of times to do the summation.
def a(c, k):
    # The sum starts at a complex number 0 so we can add complex to complex.
    sum = complex.ComplexNumber(0,0)
    # For every n in the range of k, we add the next c^n to the sum.
    for n in range(int(k) + 1):
        sum += c ** n
    return sum

# Defining b, where this formula is the geometric series formula.
def b(c, k):
    return (one - c ** (k + 1)) / (one - c)

print('For complex number',z,'and k={}:'.format(y))
print('a({},{}) ='.format(z,y),a(z,y))
print('b({},{}) ='.format(z,y),b(z,y))


