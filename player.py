import termcolor as tc
import random
import mana
import creature

class Devotion:
   def __init__(self):
      pass
   white = 0
   blue = 0
   green = 0
   black = 0
   red = 0

###########################

class Player:
   mana_pool = mana.Mana()
   devotion = Devotion()
   life = 20
   play_land = False
   win = False
   lose = False
   
   def __init__(self, library = []):
      self.library =   []
      self.hand      = []
      self.graveyard = []
      self.exiled    = []
      self.in_play   = []

      random.shuffle(library)
      for ii in range(7):
         self.hand.append(library.pop(0))
      self.library = library
   
   def draw(self, cards = 1):
      # Player draws [1] cards from
      # their library
      if len(self.library) < cards: # Lose
         self.lose = True
      else:
         for ii in range(cards):
            self.hand.append(self.library.pop(0))

   def print_hand(self):
      print ''
      for crd in self.hand:
         if crd.color == "white":
            print tc.colored(crd.card_name,'grey','on_white')
         elif crd.color == "green":
            print tc.colored(crd.card_name,'white','on_green')
         elif crd.color == "blue":
            print tc.colored(crd.card_name,'white','on_blue')
         elif crd.color == "black":
            print tc.colored(crd.card_name,'white','on_grey')
         elif crd.color == "red":
            print tc.colored(crd.card_name,'white','on_red')
         else:
            print crd.card_name
      print ''

   def print_card(self, action):
      for crd in self.hand:
         if crd.print_card(action):
            break

   def remove_creature_damage(self):
      for crtr in self.in_play:
         if isinstance(crtr, creature.Creature):
            crtr.remove_damage()

   def wins(self):
      self.win = True
