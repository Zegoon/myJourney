import random

#Variables
currentScore = int(0)
currentState=str()
numberRolled=int()
play=str()

#Play menu
def menu():
    print("Welcome to Pig! \n In this game you'll need to roll a dice. \n Every time you roll a number that is not a 1, it adds to the total you have \n If you roll a one then the score resets!\n\n")
    global currentState
    currentState=str(input("Do you want to play (Yes OR No): "))
    if currentState.upper()=="YES":
        return True
    else:
        return False

#Main roll function
def roll():
    global numberRolled
    numberRolled=int(random.randint(1,6))
    return numberRolled

#Does the user want to roll the dice
def doRoll():
    global play
    play=input("Do you want to roll? (Yes OR No): ")
    if play.upper()=="YES":
        return True
    else:
        return False

#Main
if __name__ =='__main__':
    if menu()==True:
        while True:
            if doRoll()==True:
                if roll()==1:
                    currentScore=0
                    print("Oops thats a 1!\nYour current score is a: ", currentScore)
                    break
                else:
                    currentScore=currentScore+numberRolled
                    print("You rolled a: ", numberRolled ,"\n","Your score is: ", currentScore)
                    continue
            else:
                print("Okay :(")
                currentScore=0
                break
    else:
        print("Fine")
