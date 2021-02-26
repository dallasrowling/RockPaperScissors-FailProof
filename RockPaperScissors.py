""" Welcome to Rock / Paper / Scissors """
import random
  
""" PS means player selection """
ps_scissors = { 1: ["paper", "Your opponent chooses paper, you have won!","win"], 2: ["scissors", "Your opponent chooses scissors as well, Draw!","draw"], 3: ["rock", "Your opponent chooses rock, you have lost!","lose"] }

ps_paper = { 1: ["paper", "Your opponent chooses paper as well, Draw!","draw"], 2: ["scissors", "Your opponent chooses scissors, you have lost!","lose"], 3: ["rock", "Your opponent chooses rock, you have won!","win"] }

ps_rock = { 1: ["paper", "Your opponent chooses paper, you have lost!","lose"], 2: ["scissors", "Your opponent chooses scissors, you have won!","win"], 3: ["rock", "Your opponent chooses rock as well, Draw!","draw"] }

startGame = False
while startGame == False:
  """ Scoring System """
  the_round = 1
  players_score = 0
  computers_score = 0     
  number_of_games = input("\033[1mHow many rounds would you like to play?\n(Must be more than 1 and an odd number)\033[0m\n")
  try:
    val = int(number_of_games)
    if (val % 2) == 0 or (val == 1):
      print("\nThe number of games must be an odd number and not 1 in order to determine a winner.\n")
    elif val >= 51:
       print("\nPlease select at most 49 games! You can always play another game after :)\n")
    else:
      startGame = True    
  except ValueError:
    print("\nYou are only allowed to insert numbers.\n")  

  while startGame == True and int(number_of_games) != 0: 
    def track_score(value):
      global players_score
      global computers_score 
      global the_round
      if value[cs_random][2] == 'win':
        players_score += 1
      elif value[cs_random][2] == 'lose': 
        computers_score += 1  
      the_round += 1  

    print(f"\nRound {the_round}: ({number_of_games} remaining) [Scoreboard: {players_score} : {computers_score}]")
    players_choice = input("\033[1mWhat would you like to pick?\033[0m: (Choices: rock, paper, scissors)\n")
    cs_random = random.randint(1,3)
    """ Get results """
    if players_choice == 'scissors':
      print(ps_scissors[cs_random][1])
      number_of_games = int(number_of_games) - 1
      track_score(ps_scissors)
    elif players_choice == 'rock':
      print(ps_rock[cs_random][1])
      number_of_games = int(number_of_games) - 1
      track_score(ps_rock)    
    elif players_choice == 'paper':
      print(ps_paper[cs_random][1])
      number_of_games = int(number_of_games) - 1
      track_score(ps_paper)
    else:
      print('You are only allowed to input: "rock", "paper" or "scissors"')
  else:
    if (number_of_games == 0):
      if players_score > computers_score:
        print("\n\033[1mCongratuations! You won the game :)\033[0m")
      elif computers_score > players_score:
        print("\n\033[1mYour opponent outscored you, you have lost this game!\033[0m")
      else:
        print("\n\033[1mThe match has ended in a draw!\033[0m")
      print(f'\033[0mThe final score was {players_score} (\x1B[3myou\x1B[23m) - {computers_score} (\x1B[3mopponent\x1B[23m)\033[0m')
      startGame = False
      print("\nPlay again:")
    