#James Roth
#1/23/18
#exponentialFunction.py - finding a third value and creating an exponential equation

x1=float(input("Enter x1:"))
y1=float(input("Enter y1:"))
x2=float(input("Enter x2:"))
y2=float(input("Enter y2:"))
x3=float(input("Enter x3:"))

#caclualting each value for the exponential equation
a=y1
b=y2/a
x=(x3-x1)/(x2-x1)

#calculating the y (answer) for the equation
ans=a*b**x

print("F (",str(x3),"):",format(ans,".3f"))
