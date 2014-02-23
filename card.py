# class defined for each individual card

import termcolor as tc

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
   power = None
   toughness = None
   
   seeFlavor = False
   seeExpansion = True
   seeRarity = False
   seeType = True
   seeNumber = False

########################

   def __init__(self, card_name):
      self.card_name = card_name

########################

   def setcost(self, colorless, white_mana, blue_mana,\
               black_mana, red_mana, green_mana, converted_mana_cost):
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
   
   def settype(self, Type, sub_type):
      if Type: self.Type = Type
      if sub_type: self.sub_type = sub_type
   
   def settext(self, card_text, flavor_text):
      if card_text: self.card_text = card_text
      if flavor_text: self.flavor_text = flavor_text

   def setPT(self, power, toughness):
      self.power = power
      self.toughness = toughness

   def setexpansion(self, expansion):
      self.expansion = expansion

   def setrarity(self, rarity):
      self.rarity = rarity

   def setNumber(self, number):
      if number: self.card_number = int(number)

   def setartist(self, artist):
      self.artist = artist

########################

   def tap(self):
      if can_tap:
         self.tapped = True

########################

   def untap(self):
      if can_untap:
         self.tapped = False

########################

   def addFlavor(self):
      self.seeFlavor = True
   
   def addExpansion(self):
      self.seeExpansion = True

   def addRarity(self):
      self.seeRarity = True

   def addType(self):
      self.seeType = True

   def addNumber(self):
      self.card_number = True
      
########################

   def rmFlavor(self):
      self.seeFlavor = False
   
   def rmExpansion(self):
      self.seeExpansion = False

   def rmRarity(self):
      self.seeRarity = False

   def rmType(self):
      self.seeType = False

   def rmNumber(self):
      self.card_number = False

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
      print ''
      if self.card_text: print self.card_text
      if self.flavor_text and self.seeFlavor:
         print self.flavor_text
      if self.seeType:
         if self.sub_type: print "%s \xe2\x80\x94 %s" % (self.Type, self.sub_type)
         else: print self.Type
      if self.expansion and self.seeExpansion:
         print "Expansion: %s" % self.expansion
      if self.seeRarity:
         print "Rarity: %s" % self.rarity
      if self.power and self.toughness: print "%s/%s" % (self.power, self.toughness)
      if self.seeNumber: print "card number = %d" % self.card_number
      print ''
