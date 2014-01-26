import termcolor as tc
import mana
import creature

class card:
   permanent = True
   quantity = 1
   color = "none"
   card_name = ""
   card_text = ""
   flavor_text = ""
   expansion = ""
   rarity = "common"
   card_number = 0
   artist = ""
   watermark = ""
   multiverseid = 0
   tapped = False
   can_untap = True
   can_tap = True
   converted_mana_cost = 0
   colorless_mana = 0
   white_mana = 0
   green_mana = 0
   blue_mana = 0
   red_mana = 0
   black_mana = 0

   # Cost
   cost = mana.Mana()

   def tap(self):
      if can_tap:
         self.tapped = True

   def untap(self):
      if can_untap:
         self.tapped = False

   def attack():
      pass

   def block():
      pass

############################################

   def print_card(self, action):
      match = False
      action = action.lower()
      if action == self.card_name.lower():
         match = True
         print ''
         if self.color == "white":
            print tc.colored(self.card_name,'grey','on_white')
         elif self.color == "green":
            print tc.colored(self.card_name,'white','on_green')
         elif self.color == "blue":
            print tc.colored(self.card_name,'white','on_blue')
         elif self.color == "black":
            print tc.colored(self.card_name,'white','on_grey')
         elif self.color == "red":
            print tc.colored(self.card_name,'white','on_red')
         else:
            print self.card_name

         print "cost\t",
         if self.colorless_mana > 0:
            print "%s" % self.colorless_mana,
         if self.white_mana > 0:
            print "%s" % tc.colored(self.white_mana, 'grey','on_white'), 
         if self.green_mana > 0:
            print "%s" % tc.colored(self.green_mana, 'white','on_green'),
         if self.black_mana > 0:
            print "%s" % tc.colored(self.black_mana, 'white','on_grey'),
         if self.red_mana > 0:
            print "%s" % tc.colored(self.red_mana, 'white','on_red'),
         if self.blue_mana > 0:
            print "%s" % tc.colored(self.blue_mana, 'white','on_blue'),
         print ''
         print ''
         print self.card_text
         print ''
         print self.flavor_text
         if isinstance(self, creature.Creature):
            print ''
            print "%d/%d" % (self.power, self.toughness)
         print ''

      return match
