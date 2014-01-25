# The phases of gameplay are:
#
# BEGINNING PHASE
#   Untap step
#   Upkeep step
#   Draw step
# MAIN PHASE
# COMBAT PHASE
#   Beginning of combat step
#   Declare attackers step
#   Declare blockers step
#   Combat damage step
#   End of combat step
# MAIN PHASE
# ENDING PHASE
#   End step
#   Cleanup step

import sys
import player
import creature
import land
import card

stack = []
num_players = 2

if num_players < 2:
   print "There must be at least 2 players"
   sys.exit()

plain = land.Plain()
forrest = land.Forrest()

steeple_roc = creature.Steeple_roc()
daring_skyjek = creature.Daring_skyjek()
vulpine_goliath = creature.Vulpine_goliath()


player1 = player.Player([steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath]) 

player2 = player.Player([steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, steeple_roc, daring_skyjek, plain, plain, plain, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, forrest, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath, vulpine_goliath]) 

players = [player1, player2]
stack = []
end_game = False
move = 1
first_player_move = True


def main_phase(player, players):
   action = ''
   while action != "done":
      action = raw_input("Main phase: ")
   
      if action == "hand":
         player.print_hand()
      elif action == "exit":
         sys.exit()
      else: # print card info
         card.print_card(action)
   

while not(end_game):
   for player in players:

     ## BEGINNING PHASE
     # Untap step
      for play in player.in_play:
         play.untap()

     # Upkeep step
      player.mana_pool.remove_all_mana()

     # Draw step
      if not(first_player_move):
          player.draw()
          if player.lose:
             end_game = True

     ## MAIN PHASE
      # ask user what to do
      # also supports game status
      main_phase(player, players)
      
     ## COMBAT PHASE
      
     # Beginning of combat step
      
     # Declare attackers step
      
     # Declare blockers step
      
     # Combat damage step
      
     # End of combat step
      
     ## MAIN PHASE
      
     ## ENDING PHASE
      first_player_move = False
      move += 1
     # End step
      
     # Cleanup step
      # remove all creature damage
      for plyr in players:
         plyr.remove_creature_damage()

# Determine the winners and losers
for ii in range(len(players)):
   if not(players[ii].win) and not(players[ii].lose):
      players[ii].wins()

   if players[ii].win:
      print "player %d wins" % (ii+1)
   elif players[ii].lose:
      print "player %d loses" % (ii+1)
