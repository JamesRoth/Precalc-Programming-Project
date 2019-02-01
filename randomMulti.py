#James Roth
#1/31/19
#randomMulti.py - random multiplication problems

from random import randint
correctAns = 0

while correctAns < 5: #loop until 5 correct answers are guessed
    #RNG
    num1 = randint(1,10)
    num2 = randint(1,10)
    #correct answer
    ans = num1*num2
    
    question = str("What is",num1,"*",num2)
    
    print(question)
    
    guess = int(input(question))
    if guess == ans:
        correctAns+=1
    else:
        print("Incorrect")
