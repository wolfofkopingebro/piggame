from csv import DictReader
import random

playerScore = 0

def takeTurn(): 
    print("----------------------Welcome to Pig-Game!----------------------")
    hold = 'n'
    roll = 'y'
    playerScore = 0
    currentScore = 0
    while roll == 'y' and hold == 'n': 
       
        dice = random.randint(1,6)
        print("You rolled a", dice)
        input("Hit enter to countine")  
        
        if dice == 1:
            print("You rolled a 1 so your score will be 0 this round!")
            roll = 'n'
            currentScore = 0
            roll = input("Do you want to continue? y/n?")
        else: 
            currentScore = currentScore + dice
            print(currentScore)    
            hold = input("Do you want to hold?")

        if hold == "h":
            hold = 'y'
            roll = 'n'
            playerScore =+ currentScore
            print("Your score is:",playerScore)




takeTurn()

