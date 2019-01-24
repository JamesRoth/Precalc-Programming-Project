#James Roth
#1/23/18
#monetaryGrowth.py - calculating the time it takes for money to grow to a given amount

from math import log

startingAmount=float(input("Enter the starting amount you want:"))
interestRate=float(input("Enter the interest rate:"))
compoundTimes=int(input("Enter the times compounded per year:"))
finalAmount=float(input("Enter the final amount you want:"))

ans=log(finalAmount/startingAmount,10)/(log(1+interestRate/compoundTimes,10)*compoundTimes)

print("To grow from", startingAmount,"to", finalAmount, "it will take", format(ans,".3f"),"years.")
