import random
print("------Welcome to Our game 'GUESS THE NUMBER'------")
print("-----It's a win if you have guessed it in 10 tries-----")
print("-----ENJOY!!!!-----")
randNum = random.randint(1,101)        #Random nubers between 1 to 100
myGuess = 0                            #pre-declaration of user-input variable
Life = 0                               #Life-line or trials
while myGuess != randNum:              #looping through until its correct
    myGuess = int(input("Your Guess?(1-100):\n"))        #User input until it's correct
    Life+=1
#Iterate until user has guess the number corectly within 10 tries 
    if (myGuess < randNum):          
        print("Go higher")
    elif(myGuess > randNum):
        print("Go lower")
    elif myGuess == randNum:
        if Life > 10:                #if it exceeds 10 trails, It's an L
            print("You Lost!!!!!")
            print(f"You completed in {Life} tries")
        else:
            print("YAY!!!... You won!!!!")              #if it contains inbetween 10 trails, It's a W
            print(f"You completed in {Life} tries")
        break
        
    

