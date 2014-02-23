#########################################################################
# Wrapper interface for the card class to handle cases for multiple cards
#
#########################################################################

import read_cards

class cards:
   allcards = []
   
   def get_from_database(self, database_file):
      self.allcards = read_cards.read_cards("database").getcards()
   
   def findname(self, name):
      for crd in self.allcards:
         if crd.card_name == name:
            crd.print_card()
   
########################

   def addFlavor(self):
      for crd in self.allcards:
         crd.addFlavor()
   
   def addExpansion(self):
      for crd in self.allcards:
         crd.addExpansion()

   def addRarity(self):
      for crd in self.allcards:
         crd.addRarity()

   def addType(self):
      for crd in self.allcards:
         crd.addType()

   def addNumber(self):
      for crd in self.allcards:
         crd.addNumber()
      
########################

   def rmFlavor(self):
      for crd in self.allcards:
         crd.rmFlavor()
   
   def rmExpansion(self):
      for crd in self.allcards:
         crd.rmExpansion()

   def rmRarity(self):
      for crd in self.allcards:
         crd.rmRarity()

   def rmType(self):
      for crd in self.allcards:
         crd.rmType()

   def rmNumber(self):
      for crd in self.allcards:
         crd.rmNumber()

########################
