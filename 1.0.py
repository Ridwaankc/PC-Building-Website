#importing library
import random

#Creating array for bot
Choices = ["ROCK", "PAPER", "SCISSORS"]

#Creating Other variables
GameOptions = ""
Choice = ""


#Creating bot
def opponent():
  ChoiceOpp = random.randint(0, 2)

  print(Choices[ChoiceOpp])
  return Choices[ChoiceOpp]


#Deciding game winner
def game(ChoiceOpp, Choice):
  if ChoiceOpp == Choice:
    print("\nDraw")
  elif ChoiceOpp == "ROCK" and Choice == "PAPER" or ChoiceOpp == "SCISSORS" and Choice == "ROCK" or ChoiceOpp == "PAPER" and Choice == "SCISSORS":
    print("\nYou Win")
  else:
    print("\nYou Lose")


#Starting statements



Choice = input("Pick between Rock, Paper, and Scissors\n")

#Checking for valid input
while Choice.upper() not in ["ROCK", "PAPER", "SCISSORS"]:
	Choice = input("\nEnter your choice: ")
	Choice = Choice.upper()

#Start game
game(opponent(), Choice)


#make scoreboards work, just keeps displaying 0
#Number of rounds
#Infinite rounds

#Could add tournament/2nd player
