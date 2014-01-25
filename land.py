import termcolor as tc
import card

class land(card.card):
   permanent = True
   quantitiy = float("inf")
   def tap(self, player, players):
      pass


   #################
   # Generic Lands #
   #################

class Forrest(land):
   card_name = tc.colored("Forrest",'white','on_green')
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.green += 1
      self.tapped = True

##################################

class Mountain(land):
   card_name = tc.colored("Mountain",'white','on_red')
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.red += 1
      self.tapped = True

##################################

class Swamp(land):
   card_name = tc.colored("Swamp",'white','on_grey')
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.black += 1
      self.tapped = True

##################################

class Plain(land):
   card_name = tc.colored("Plain",'grey','on_white')
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.white += 1
      self.tapped = True

##################################

class Island(land):
   card_name = tc.colored("Island",'white','on_blue')
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.blue += 1
      self.tapped = True

##################################
