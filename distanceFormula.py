#James Roth
#1/22/18
#distanceFormula.py - distance formula

x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))

ans=(((y1-y2)**(y1-y2))+((x1-x2)**(x1-x2)))**0.5

print("The distance is:", ans)