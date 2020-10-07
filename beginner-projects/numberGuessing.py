import random

# Returns an number between 1 and 10
randomNum = random.randint(1, 10)


while 1:
    # Input needs to be an Integer!
    userInput = int(input('Enter an number: '))
    if (randomNum == userInput):
        print('Horay! You gussed the correct nummer! --> AI selected', randomNum)
        # Stop the loop...
        break
    else:
        print('Ah... You selected the wrong number! Try again!')
