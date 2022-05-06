print("""Welcome to the sus checker, answer a few questions to find out if the object you found is sus.

""")
colour = input("What colour is the object? ")
colour = colour.lower()
shape = input("Is the object a square/rectangle with a circular top? ")
shape = shape.lower()
if shape == "yes":
    shapeFinal = True
elif shape == "y":
    shapeFinal = True
else:
    shapeFinal = False
visor = input("Is there a protrusion or pattern on the object that could resemble a visor? ")
if visor == "yes":
    visorFinal = True
elif visor == "y":
    visorFinal = True
else:
    visorFinal = False
if colour == "red" and shapeFinal == True and visorFinal == True:
    print("""
The object is indeed sus
    
Amogus moment""")
else:
    print("""
The object is not sus, you are safe""")