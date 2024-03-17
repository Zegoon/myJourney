import random

numGend=int(0)
gameDifficulty=int(0)
livesLeft=int(10)

def userPickDiff():
    global gameDifficulty
    gameDifficulty=int(input("Please enter a difficulty from 1 to 3: "))

def genNum(range) -> int:
    global numGend
    numGend=random.randint(1,range)
    return numGend

def userGuess():
    global livesLeft
    guess=int(input("Guess the number: "))
    if guess>numGend:
        print("Number guess is too big!\nTry again!")
        livesLeft-=1
        print("You have",livesLeft,"lives left!")
    elif guess<numGend:
        print("Number guess is too small!\nTry again!")
        livesLeft-=1
        print("You have",livesLeft,"lives left!")
    elif guess==numGend:
        livesLeft=10
        print("Good Job!")

if __name__=='__main__':
    userPickDiff()
    if gameDifficulty==1:
        while livesLeft>0:
            genNum(150)
            userGuess()
            continue
    elif gameDifficulty==2:
        while livesLeft>0:
            genNum(250)
            userGuess()
            continue
    elif gameDifficulty==3:
        while livesLeft>0:
            genNum(350)
            userGuess()
            continue
    else:
        print("Enter a valid number!")
