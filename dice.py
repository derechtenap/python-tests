import random as rand


def rollDice():
    return rand.randint(1, 6)


# First roll...
print('I rolled:', rollDice())

while 1:

    # Roll again?
    userInput = str(input('Do you want to roll again? (Y/N)')).upper()

    if (userInput == 'N'):
        print('Okay! I wont roll again.')
        break
    elif (userInput != 'Y'):
        print('Please use Y or N!')
    else:
        print('I rolled:', rollDice())
