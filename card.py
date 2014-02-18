import termcolor as tc
#import creature

class card:
   card_name = None
   Type = None
   sub_type = None
   complete = False
   permanent = True
   quantity = 0
   color = list()
   card_text = None
   flavor_text = None
   expansion = None
   rarity = 'C'
   card_number = 0
   artist = None
   watermark = None
   multiverseid = 0
   tapped = False
   can_untap = True
   can_tap = True
   converted_mana_cost = None
   colorless = None
   white_mana = None
   green_mana = None
   blue_mana = None
   red_mana = None
   black_mana = None

########################

   def __init__(self, card_name):
      self.card_name = card_name

########################

   def setcost(self, colorless, white_mana, blue_mana, black_mana, red_mana, green_mana, converted_mana_cost):
      if white_mana:
         self.white_mana = white_mana
         self.color.append('W')
      if blue_mana:
         self.blue_mana = blue_mana
         self.color.append('U')
      if black_mana:
         self.black_mana = black_mana
         self.color.append('B')
      if red_mana:
         self.red_mana = red_mana
         self.color.append('R')
      if green_mana:
         self.green_mana = green_mana
         self.color.append('G')
      if colorless:
         self.colorless = colorless
   
########################

   def settype(self, Type, sub_type):
      if Type: self.Type = Type
      if sub_type: self.sub_type = sub_type

########################
      
   def settext(self, card_text, flavor_text):
      if card_text: self.card_text = card_text
      if flavor_text: self.flavor_text = flavor_text

########################

   def tap(self):
      if can_tap:
         self.tapped = True

########################

   def untap(self):
      if can_untap:
         self.tapped = False

########################

   def attack():
      pass

########################

   def block():
      pass

########################

   def print_card(self):
      print self.card_name
      print "cost\t",
      if self.colorless:
         print "%s" % self.colorless,
      if self.white_mana:
         print "%s" % tc.colored(self.white_mana, 'grey','on_white'),
      if self.blue_mana:
         print "%s" % tc.colored(self.blue_mana, 'white','on_blue'),
      if self.green_mana:
         print "%s" % tc.colored(self.green_mana, 'white','on_green'),
      if self.black_mana:
         print "%s" % tc.colored(self.black_mana, 'white','on_grey'),
      if self.red_mana:
         print "%s" % tc.colored(self.red_mana, 'white','on_red'),
      print self.card_text
      print self.flavor_text
#         if isinstance(self, creature.Creature):
#            print ''
#            print "%d/%d" % (self.power, self.toughness)
      print ''
