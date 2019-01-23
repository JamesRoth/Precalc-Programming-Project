#James Roth
#1/22/18
#distanceFormula.py - distance formula

x1=float(input("Enter x1:"))
y1=float(input("Enter y1:"))
x2=float(input("Enter x2:"))
y2=float(input("Enter y2:"))

ans=(((y1-y2)**2)+((x1-x2)**2))**0.5

print("The distance is:", format(ans,'.3f'))