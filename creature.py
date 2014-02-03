import termcolor as tc
import card
import player

class Creature(card.card):
   card_name = ''
   Type = 'creature'
   sub_type = ''
   permanent = True
   summining_sickness = True

   power = 0
   toughness = 0

   damage = 0

   # Abilities
   vigilance = False
   haste = False
   Trample = False
   flying = False
   first_strike = False

   def __init__(self, card_name):
      self.card_name = card_name

   def remove_damage(self):
      self.damage = 0

################################
##       Creature cards       ##
################################

# WHITE

  ##############
  # Steeple Roc
  ##############

class Steeple_roc(Creature):
   Type = 'bird'
   card_name = "Steeple Roc"
   color = "white"
   card_text = "Flying, first strike"
   flavor_text = "\"Sometimes it forgets to loosen its grip before taking flight. I lost my roof that way.\" \n-Ecaban, Boros scout"
   
   # Cost
   converted_mana_cost = 5
   colorless_mana = 4
   white_mana = 1
   
   power = 3
   toughness = 1
   
   # Abilities
   flying = True
   first_strike = True
   
   # Misc
   expansion = "Dragon's Maze"
   card_number = 8
   multiverseid = 368992
   artist = "David Palumbo"

   ################
   # Daring Skyjek
   ################

class Daring_skyjek(Creature):
   complete = True
   Type = 'human knight'
   card_name = "Daring Skyjek"
   color = "white"
   card_text = "Battalion - Whenever Daring Skyjek and at least two other creatures attack, Daring Skyjek gains flying until end of turn."
   flavor_text = "\"The hard part isn't landing in the saddle. The hard part is leaping before you see it.\""
   watermark = "Boros"

   # Cost
   converted_mana_cost = 2
   colorless_mana = 1
   white_mana = 1
   
   power = 3
   toughness = 1
   
   # Misc
   expansion = "Gatecrash"
   card_number = 9
   multiverseid = 366251
   artist = "Jason Chan"

   def attack(self, this_player, other_players):
      if self.tapped or self.summining_sickness:
         print "this creature cannot attack now"
         return
      
      self.tapped = True
      if len(this_player.attackers) >= 3:
         self.flying = True

   def end_turn(self):
      self.flying = False

  ##################
  # Vulpine Goliath
  ##################

class Vulpine_goliath(Creature):
   Type = 'fox'
   card_name = "Vulpine Goliath"
   color = "green"
   card_text = "Trample"
   flavor_text = "\"With a diet of hydras, giants, and massive serpents, anything would get that big.\"\n-Corisande, Setessan hunter"

   # Cost
   converted_mana_cost = 6
   colorless_mana = 4
   green_mana = 2

   # Misc
   expansion = "Theros"
   card_number = 183
   multiverseid = 373655
   artist = "Adam Paquette"
