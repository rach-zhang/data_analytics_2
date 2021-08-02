def result(winner, winning_weapon, losing_weapon):
  print("Congratulations, " + winner + "! " + winning_weapon.title() + " beats " + losing_weapon + "!")

another_round = 'Yes'
while another_round.title() == "Yes":
  
  player_1_weapon = input("Player 1: What is your weapon?")
  player_2_weapon = input("Player 2: What is your weapon?")

  if (player_1_weapon.lower() == 'rock' and player_2_weapon.lower() == 'scissors') or \
  (player_1_weapon.lower() == 'scissors' and player_2_weapon.lower() == 'paper') or \
  (player_1_weapon.lower() == 'paper' and player_2_weapon.lower() == 'rock'):
    result("Player 1", player_1_weapon, player_2_weapon)
  elif player_1_weapon.lower() == player_2_weapon.lower():
    print ("Draw.")
  else:
    result("Player 2", player_2_weapon, player_1_weapon)

  another_round = input("Want to play again? (Yes/No)")
  if another_round.title() == "No":
    print("Oh, okay. Some other time, then. I'll miss you!")


