# Ziwei Hou CS 171-B, ID: zh367
print("Length Conversion Wizard")
print("This program can convert between any of the following lengths below:")
print('\ninches\nfeet\nyards\nmiles\nleagues\ncentimeters\nmeters\ndecameters\nhectometers\nkilometers\n\nNote: You must use the units exactly as spelled above.\n')
varunits = {
  "centimeters":1,
  "decimeters":10,
  "meters":100, 
  "decameters":1000, 
  "hectometers":10000, 
  "kilometers":100000,
  "inches":2.54, 
  "feet":30.48, 
  "yards":91.44,
  "miles":160934.4, 
  "leagues":482803.2
}
#from value
valuein = float(input("Enter Initial Value:\n"))
#from units
inunits = str(input("Enter the Units of the Initial Value:\n"))
#to unit
outunit = str(input("Enter the units you want to convert to:\n"))
# Base unit is a centimeter. In order to convert to "to unit", you must divide by "to unit" to obtain its value in centimeters.
Converter1 = valuein / varunits[outunit] * varunits[inunits]
print("\n",valuein, inunits, "is", Converter1, outunit)