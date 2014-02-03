import re

p = re.compile('[ \t]*(card_name|type|color|quantity|blue_mana|black_mana|green_mana|white_mana|red_mana|converted_mana_cost|sub_type|card_text|flavor_text|power|toughness|expansion|rarity|card_number|artist|multiverseid)[ \t]*=[ \t]*(.+)', re.IGNORECASE)
plus = re.compile('(\+)')
minus = re.compile('(\-)')

f = open('deck','r')
line = f.readline()
while line:
   if plus.findall(line):
      line = f.readline()
      while not plus.findall(line) and line:
         y = p.findall(line)
         if not y:
            break
         elif y[0][0] == 'card_name':
            card_name = y[0][1]
         elif y[0][0] == 'type':
            Type = y[0][1]
         elif y[0][0] == 'color':
            color = y[0][1]
         elif y[0][0] == 'quantity':
            quantity = y[0][1]
         elif y[0][0] == 'blue_mana':
            blue_mana = y[0][1]
         elif y[0][0] == 'black_mana':
            black_mana = y[0][1]
         elif y[0][0] == 'green_mana':
            green_mana = y[0][1]
         elif y[0][0] == 'white_mana':
            white_mana = y[0][1]
         elif y[0][0] == 'red_mana':
            red_mana = y[0][1]
         elif y[0][0] == 'converted_mana_cost':
            converted_mana_cost = y[0][1]
         elif y[0][0] == 'sub_type':
            sub_type = y[0][1]
         elif y[0][0] == 'card_text':
            card_text = y[0][1]
         elif y[0][0] == 'flavor_text':
            flavor_text = y[0][1]
         elif y[0][0] == 'power':
            power = y[0][1]
         elif y[0][0] == 'toughness':
            toughness = y[0][1]
         elif y[0][0] == 'expansion':
            expansion = y[0][1]
         elif y[0][0] == 'rarity':
            rarity = y[0][1]
         elif y[0][0] == 'card_number':
            card_number = y[0][1]
         elif y[0][0] == 'artist':
            artist = y[0][1]
         elif y[0][0] == 'multiverseid':
            multiverseid = y[0][1]
         line = f.readline()
   elif minus.findall(line):
      break
   line = f.readline()
