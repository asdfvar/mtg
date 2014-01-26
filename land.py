import termcolor as tc
import card

class Land(card.card):
   permanent = True
   quantitiy = float("inf")
   def tap(self, player, players):
      pass


   #################
   # Generic Lands #
   #################

class Forrest(Land):
   card_name = "Forrest"
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.green += 1
      self.tapped = True

##################################

class Mountain(Land):
   card_name = "Mountain"
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.red += 1
      self.tapped = True

##################################

class Swamp(Land):
   card_name = "Swamp"
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.black += 1
      self.tapped = True

##################################

class Plain(Land):
   card_name = "Plain"
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.white += 1
      self.tapped = True

##################################

class Island(Land):
   card_name = "Island"
   def __init__(self):
      pass
   def tap(self, player, players):
      player.mana_pool.blue += 1
      self.tapped = True

##################################
