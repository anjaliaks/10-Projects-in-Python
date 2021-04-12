import random

number = random.randint(1,20)
player = int(input("Enter Your Guessed Number Between 1-20 : "))

i=0

while(True):
    
    if player == number:
        print("Your Guess is right")
        break
    elif number > player :
        print("Guess is low")
        player = int(input("Enter Your Guess Again : "))
    
    elif number < player :
        print("Guess is high")
        player = int(input("Enter Your Guess Again : "))
        
    else:
        print("Not a Number")
        

    i+=1
    
Score = 20-i
print("Your score is",Score)


