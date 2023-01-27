# random module for choosing the random move.
import random

global userMove, computerMove
userMove, computerMove = "", ""
userScore, computerScore = 0, 0

def initiateGame () :
    userResponse = input("Enter \'yes\' to get started with the game, and \'no\' to play the next time!")
    if userResponse.lower() == "yes" :
        gameDescription ()
        return
    if userResponse.lower() == "no" :
        print("See you next time!")
    else :
        print("Please enter a valid response!")
        initiateGame ()

def gameDescription () :
    descriptionStatements = ["Rock Paper Scissors is a simple game.", "To win the game, one must stick to the rules...which are simple and strightforward!", "This is how it goes", "Rock beats Scissors...", "Scissors beats Paper...", "Paper beats Rock...", "See...simple, Right...", "Alright, now let's get started!"]
    for i in range (len(descriptionStatements)) :
        print(descriptionStatements[i], end="\n")
    
    chooseNumberOfRounds ()
        
def chooseNumberOfRounds () :
    numberOfRounds = input("Choose the number of rounds for the game...The maximum limit is 20!")
    if numberOfRounds.isdigit() == False :
        print("Please enter a valid number input!")
        chooseNumberOfRounds ()
    elif int(numberOfRounds) <= 0 or int(numberOfRounds) > 20 :
        print("Please enter a valid number, minimum number of rounds is 0, and maximum number of rounds is 20.")
        chooseNumberOfRounds ()
    elif int(numberOfRounds) > 0 and int(numberOfRounds) <= 20 :
        startGame (int(numberOfRounds))

def startGame (numberOfRounds) :
    userScore, computerScore = 0, 0
    computerMoves = ["rock", "paper", "scissors"]
    counter = 0
    while (counter < numberOfRounds) :
        userMove = input("Rock, Paper or Scissors...")
        computerMove = computerMoves[random.randint(0, len(computerMoves)-1)]
        
        if userMove == computerMove :
            print(computerMove)
            print("It's a Tie...")
            counter += 1
        # probabilities when the user wins
        elif (userMove.lower() == "rock" and computerMove.lower() == "scissors") or (userMove.lower() == "paper" and computerMove.lower() == "rock") or (userMove.lower() == "scissors" and computerMove.lower() == "paper") :
            print(computerMove)
            print("You win this round!")
            userScore += 1
            counter += 1
        elif (computerMove.lower() == "rock" and userMove.lower() == "scissors") or (computerMove.lower() == "paper" and userMove.lower() == "rock") or (computerMove.lower() == "scissors" and userMove.lower() == "paper") :
            print(computerMove)
            print("The computer wins this round!")
            computerScore += 1
            counter += 1
        else :
            print("Please play a valid move...")
            # playMove ()
    endGame (userScore, computerScore)
 
def endGame (userScore, computerScore) :
    print("Your score is : {}, and the Computer's score is {}!".format(userScore, computerScore))
    if userScore == computerScore :
        print("Congratulations, you and the computer both win the game!")
    elif userScore > computerScore :
        print("Congratulations, you have successfully defeated the computer!")
    elif computerScore > userScore :
        print("Congratulations.....To the computer for winning the game! Better luck next time!")
        
initiateGame()