# Assignment - 2
# Get random names of the people in the list using For loop, Maximum participant variable and input() function
#and then get your lottery run;

print("----LOTTERY TICKET DRAW----")

participant=[]
maxTicketAvailable = int(input("Enter the maximum number of lottery tickets available: "))

print("\n")
for i in range(0,maxTicketAvailable):
    print("Enter name at index",i)
    item = input()
    participant.append(item)

import random
n = random.randint(0,maxTicketAvailable-1)

print("\nHere goes the winner!!")

participant[n]
print("Yeah..",participant[n],"is the winner of the lottery ticket!!")