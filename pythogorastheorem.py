from math import hypot
print("What do you want to calculate")
print("1. Hypotenuse")
print("2. Base")
print("3. Height")

operation = input()

if operation == "1":
    base = float(input("Enter Base: "))
    height = float(input("Enter Height: "))
    hy = hypot(base,height)
    print("Hypotenuse = " , hy)

elif operation == "2":
    hypotenuse = float(input("Enter Hypotenuse: "))
    height =  float(input("Enter Height: "))
    bsquared = hypotenuse**2 - height**2
    b = bsquared**0.5
    print("Base = " , b)

elif operation == "3":
    hypotenuse = float(input("Enter Hypotenuse: "))
    base = float(input("Enter Base: "))
    hsquared = hypotenuse**2 - base**2
    h = hsquared**0.5
    print("Height = " , h)

else:
    print("Invalid Entry")