import random as rand
print("Hello! Can your Luck Save the Girl! | -1 For Quit the Game ")
print("Can You Guess the Number between 1 to 100")

randomNum = rand.randint(0, 100);
chance = 999
print(randomNum)
print('\n')

while (chance > 0) :
    try:
        userVal = int(input("Your Guessing \t"))
    except ValueError:
        userVal = int(input("Your Guessing in Number Please\t"))
        break

    if userVal == -1 :
        print("See you next Time! 😁 \t")
        break
    elif (userVal < randomNum) :
        print(f"You guessed Smaller Number {chance} left ⬇️ \t")
        chance -= 1
    # elif (dtype(userVal) == )
    elif (userVal > randomNum) :
        print(f"You Guessed larger Number {chance} left ⬆️ \t")
        chance -= 1
    elif (userVal == randomNum) :
        print("You Guessed the Perfect Number!😌  \t")
        break
    
