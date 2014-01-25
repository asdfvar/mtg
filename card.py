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

def print_card(action):
   action = action.lower()
   if action == "steeple roc":
      crd = creature.Steeple_roc()
   elif action == "daring skyjek":
      crd = creature.Daring_skyjek()
   elif action == "vulpine goliath":
      crd = creature.Vulpine_goliath()
   else:
      return

   print ''
   print crd.card_name
   print "cost\t",
   if crd.colorless_mana > 0:
      print "%s" % crd.colorless_mana,
   if crd.white_mana > 0:
      print "%s" % tc.colored(crd.white_mana, 'grey','on_white'), 
   if crd.green_mana > 0:
      print "%s" % tc.colored(crd.green_mana, 'white','on_green'),
   if crd.black_mana > 0:
      print "%s" % tc.colored(crd.black_mana, 'white','on_grey'),
   if crd.red_mana > 0:
      print "%s" % tc.colored(crd.red_mana, 'white','on_red'),
   if crd.blue_mana > 0:
      print "%s" % tc.colored(crd.blue_mana, 'white','on_blue'),
   print ''
   print crd.card_text
   print ''
   print crd.flavor_text
   if isinstance(crd, creature.Creature):
      print ''
      print "%d/%d" % (crd.power, crd.toughness)
   print ''
