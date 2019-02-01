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
    
    #asking the user to give the answer to the multiplication problem
    guess = int(input("What is "+str(num1)+"*"+str(num2)))
    #did they get it right?
    if guess == ans:
        correctAns+=1
    else:
        print("Incorrect! The correct answer is: "+str(ans))
