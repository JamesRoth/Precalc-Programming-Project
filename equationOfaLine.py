#James Roth 
#1/24/18
#equationOfaLine.py - finding the equation of a line between two points

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

slope = format((y1-y2)/(x1-x2),".3f")

b = format(y1-(slope*x1),".3f")

print("The equation is Y =", slope, "*x +", b)
