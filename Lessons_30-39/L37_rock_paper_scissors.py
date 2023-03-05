# This is a game where a user will type Rock Paper or Scissors and play against a Computer choosing an option at random
import random

# Tallies to be displayed after each round
player_score = 0
computer_score = 0
games_played = 0

# While-loop to continue game running until Player opts out
while True:
  choices = ['rock', 'paper', 'scissors']
  computer_move = random.choice(choices).capitalize()  #  computer's choice is chosen at random
  player_move = ''

  # Will keep asking for a valid input until matches one of the choices
  while player_move.lower() not in choices:
    player_move = input("Rock, Paper or Scissors?: ").capitalize()

  print("Player: ", player_move)
  print("Computer: ", computer_move) 

  # Declare a Tie when choices are the same
  if player_move == computer_move:
    print("It's a Tie! Play again!")

  # Results when player choose Rock
  elif player_move == 'Rock':
    if computer_move == 'Paper':
      print("Player loses! :(")
      computer_score += 1
    elif computer_move == 'Scissors':
      print('Player wins! :)')  
      player_score += 1

  # Results when player chooses Paper
  elif player_move == 'Paper':
    if computer_move == 'Scissors':
      print("Player loses! :(")
      computer_score += 1
    elif computer_move == 'Rock':
      print('Player wins! :)')  
      player_score += 1

  # Results when player choose Scissors
  elif player_move == 'Scissors':
    if computer_move == 'Rock':
      print("Player loses! :(")
      computer_score += 1
    elif computer_move == 'Paper':
      print('Player wins! :)')  
      player_score += 1
  
  # Add count to total games played once round is over
  games_played += 1

  # Display info on games scored for each Player and Computer
  print('Player: {} - Computer {}'.format(str(player_score), str(computer_score)))
  print() 

  # Awaits response from Player for another round, break out of While-loop if not
  another_round = input("Play another game? (yes/no): ").lower()
  if another_round != 'yes':
    break
  print()

# Displays total games played and final score
print('Games Played: '+ str(games_played))
print('Final Score: Player: {} - Computer {}'.format(str(player_score), str(computer_score)))