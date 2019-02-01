#James Roth
#1/31/19
#randomMulti.py - random multiplication problems

from random import randint
correctAns = 0

while correctAns < 5:
    num1 = randint(1,10)
    num2 = randint(1,10)
    ans = num1*num2
    
    guess = int(input("What is", num1, "*", num2))
    if guess == ans:
        correctAns+=1
    else:
        print("Incorrect")
