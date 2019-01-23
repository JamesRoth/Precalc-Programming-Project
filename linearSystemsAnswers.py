#James Roth
#1/23/18
#linearSystemsAnswers.py - solving two linear systems for intersection

a=float(input("Enter A (for Ax + By = C):"))
b=float(input("Enter B (for Ax + By = C):"))
c=float(input("Enter C (for Ax + By = C):"))
d=float(input("Enter D (for Ax + By = C):"))
e=float(input("Enter E (for Ax + By = C):"))
f=float(input("Enter F (for Ax + By = C):"))

y=((f*a)-(d*c))/((e*a)-b)
x=(c-(b*y))/a
#NOT WORKING
print("NOT WORKING?    X:",x,"Y:", y)
