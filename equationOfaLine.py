#James Roth 
#1/24/18
#equationOfaLine.py - finding the equation of a line between two points

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

slope = float((y1-y2)/(x1-x2))

if y1-y2 == 0:
    print("y =", y1)

elif x1-x2 == 0:
    print("x =", x1)

b = format(y1-(slope*x1),".3f")

#just formatting
slope = format(slope, ".3f")
slope = str(slope) + "x"

#more formatting, so it says - b if b is > 0 not + -b
elif float(b) >= 0:
    print("The equation is Y =", slope, "+", b)

elif float(b) < 0:
    print("The equation is y =", slope, b)