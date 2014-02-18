import card
import re

class read_cards:
   cards = list()
   #p = re.compile('[ \t]*(type|color|quantity|colorless|blue|black|green|white|red|converted mana cost|sub type|card text|flavor text|power|toughness|expansion|rarity|card number|artist|multiverse id)[ \t]*=[ \t]*(.+)', re.IGNORECASE)
   p = re.compile("([\W\w]+)=[ \t]*(.+)", re.IGNORECASE)
   plus = re.compile('(\+)')
   minus = re.compile('(\-)')
   ################################
   def __init__(self, file_name):
      self.file_name = file_name

      f = file(file_name,'r')
      line = f.readline().strip()
      while line:

         Type                = None
         color               = None
         colorless           = None
         blue_mana           = None
         black_mana          = None
         green_mana          = None
         white_mana          = None
         red_mana            = None
         converted_mana      = None
         sub_type            = None
         card_text           = None
         flavor_text         = None
         power               = None
         toughness           = None
         expansion           = None
         rarity              = None
         card_number         = None
         artist              = None
         multiverseid        = None
         card_name           = None

         if self.plus.findall(line):
            line = f.readline().strip()
            card_name = line
            while line and line != '+' and line != '-':
               y = self.p.findall(line)
               if not y:
                  line = f.readline().strip()
                  continue
               elif y[0][0].strip() == 'type':
                  Type = y[0][1]
               elif y[0][0].strip() == 'sub type':
                  sub_type = y[0][1]
               elif y[0][0].strip() == 'colorless':
                  colorless = y[0][1]
               elif y[0][0].strip() == 'white':
                  white_mana = y[0][1]
               elif y[0][0].strip() == 'blue':
                  blue_mana = y[0][1]
               elif y[0][0].strip() == 'black':
                  black_mana = y[0][1]
               elif y[0][0].strip() == 'red':
                  red_mana = y[0][1]
               elif y[0][0].strip() == 'green':
                  green_mana = y[0][1]
               elif y[0][0].strip() == 'converted mana cost':
                  converted_mana = y[0][1]
               elif y[0][0].strip() == 'card text':
                  card_text = y[0][1]
               elif y[0][0].strip() == 'flavor text':
                  flavor_text = y[0][1]
               elif y[0][0].strip() == 'power':
                  power = y[0][1]
               elif y[0][0].strip() == 'toughness':
                  toughness = y[0][1]
               elif y[0][0].strip() == 'expansion':
                  expansion = y[0][1]
               elif y[0][0].strip() == 'rarity':
                  rarity = y[0][1]
               elif y[0][0].strip() == 'card number':
                  card_number = y[0][1]
               elif y[0][0].strip() == 'artist':
                  artist = y[0][1]
               elif y[0][0].strip() == 'multiverse id':
                  multiverseid = y[0][1]
               line = f.readline().strip()
         elif self.minus.findall(line):
            break

#         print Type
#         print sub_type
#         print colorless
#         print white_mana
#         print blue_mana
#         print black_mana
#         print red_mana
#         print green_mana
#         print converted_mana
#         print card_text
#         print flavor_text
#         print power
#         print toughness
#         print expansion
#         print rarity
#         print card_number
#         print artist
#         print multiverseid
#         print '++++++++++++++++++++'

         this_card = card.card(card_name)
         this_card.setcost(colorless, white_mana, blue_mana,\
                           black_mana, red_mana, green_mana, converted_mana)
         this_card.settype(Type, sub_type)
         this_card.settext(card_text, flavor_text)

         self.cards.append(this_card)
      f.flush()
      f.close()
      
   def getcards(self):
      return self.cards
