'''Implement a game module that checks input from two sources. when the guess is right 
a level is incremented when the guess is wrong the level is decremented the game 
stops when level hits zero (0). the first level is one. if the first guess is 
wrong, program terminated.'''

import random

Level = 1
Ans = [1,2]


while Level >= 1:
    answer = random.choice(Ans)
    Guess = int(input("Guess a number between 1 and 2: "))

    print("The correct answer is: ", answer)

    if Guess==answer:
        print ("Your answer is correct")
        print ("You advance to level ", Level+1)
        Level +=1
    else:
        print ("Your answer is wrong")
        print ("You're back to level ", Level-1)
        Level -= 1
    continue

print("Game Failed!")

