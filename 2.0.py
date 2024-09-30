#importing library
import random

#Creating array for bot
Choices = ["ROCK", "PAPER", "SCISSORS"]

#Creating scores
BotScore = 0
PlayerScore = 0

#Creating Other variables
GameOptions = ""
Choice = "START"
Games = 0


#Creating bot
def opponent():
  ChoiceOpp = random.randint(0, 2)

  print(Choices[ChoiceOpp])
  return Choices[ChoiceOpp]


#Deciding game winner
def game(ChoiceOpp, Choice, BotScore, PlayerScore):
  if ChoiceOpp == Choice:
    print("\nDraw, No player gets a point")
  elif ChoiceOpp == "ROCK" and Choice == "PAPER" or ChoiceOpp == "SCISSORS" and Choice == "ROCK" or ChoiceOpp == "PAPER" and Choice == "SCISSORS":
    PlayerScore = PlayerScore + 1
    print("\nYou Win")
    return PlayerScore 
  else:
    BotScore = BotScore + 1
    print("\nYou Lose")
    return BotScore



#Starting statements

#Set number of games
while GameOptions.upper() != "NO" or GameOptions.upper() != "YES":
  GameOptions = input(
      "\nWould you like to play a set number of rounds?: \nYes \nNo \n\nType here: "
  )
  print(GameOptions.upper())
  if GameOptions.upper() == "YES":
    Games = int(input("\nHow many rounds would you like to play?: "))
    if Games < 0:
      break
    else:
      for i in range(0, Games - 1):
        print("Round", i + 1)
        Choice = input("Pick between Rock, Paper, and Scissors\n")

        #Checking for valid input
        while Choice.upper() not in ["ROCK", "PAPER", "SCISSORS"]:
          Choice = input("\nEnter your choice: ")
          Choice = Choice.upper()

        #Start game
        game(opponent(), Choice, BotScore, PlayerScore)
        print("Player has ", PlayerScore, "Wins", "Bot has", BotScore, "Wins")
        if i == Games - 1:
          if PlayerScore > BotScore:
            print("Player Wins")
          if BotScore > PlayerScore:
            print("Bot Wins")
          else:
            print("Draw")

#INFINITE ROUNDS
  else:
    print("Infinite rounds activated")
    Continue = True
    Round = 0
    while Continue == True:
      Round = Round + 1
      print("Round", Round)
      Choice = input("Pick between Rock, Paper, and Scissors\n")

      #Checking for valid input
      while Choice.upper() not in ["ROCK", "PAPER", "SCISSORS"]:
        Choice = input("\nEnter your choice: ")
        Choice = Choice.upper()
        
      #Start game
      game(opponent(), Choice, BotScore, PlayerScore)
      print("Player has", PlayerScore, "Wins", "Bot has", BotScore, "Wins")
      
      #continue game
      Continue = input(
          "\nWould you like to continue?: \nYes \nNo \n\nType here: ")
      if Continue.upper() == "NO":
        Continue = False
        print("\nPlayer has", PlayerScore, "Wins", "Bot has", BotScore, "Wins")

        if PlayerScore > BotScore:
          print("Player Wins")
        if BotScore > PlayerScore:
          print("Bot Wins")
        else:
          print("Draw")
        break
      else:
        Continue = True

#make scoreboards work, just keeps displaying 0
#Number of rounds
#Infinite rounds

