#!/usr/bin/python
import requests
import re
import os

class Page_defined:
   defined = False
   counter = 0
   def setFalse(self, multiverse_id):
      self.defined = False
      self.counter+=1
      if self.counter % 10 == 0:
         print "multiverse id %d with %d undefined pages thus far"\
               % (multiverse_id, self.counter)
   def setTrue(self):
      self.defined = True
      self.counter=0
   def isTrue(self):
      return self.defined

page_defined = Page_defined()

class Stats:
   card_name           = None
   multiverse_id       = None
   colorless           = None
   red                 = None
   green               = None
   blue                = None
   black               = None
   white               = None
   converted_mana_cost = None
   types               = None
   subtype             = None
   card_text           = None
   flavor_text         = None
   power               = None
   toughness           = None
   expansion           = None
   rarity              = None
   card_number         = None
   artist              = None
   def set2null(self):
      self.multiverse_id       = None
      self.colorless           = None
      self.red                 = None
      self.green               = None
      self.blue                = None
      self.black               = None
      self.white               = None
      self.converted_mana_cost = None
      self.types               = None
      self.subtype             = None
      self.card_text           = None
      self.flavor_text         = None
      self.power               = None
      self.toughness           = None
      self.expansion           = None
      self.rarity              = None
      self.card_number         = None
      self.artist              = None
   def write2File(self, file_name):
      # write to file
      f = file(file_name,'a')
      f.write('+\n')
      if self.card_name:     f.write("%s\n" % self.card_name)
      if self.multiverse_id: f.write("multiverse id = %d\n" % self.multiverse_id)
      if self.colorless:     f.write("colorless = %d\n" % self.colorless)
      if self.red:           f.write("red = %d\n" % self.red)
      if self.green:         f.write("green = %d\n" % self.green)
      if self.blue:          f.write("blue = %d\n" % self.blue)
      if self.black:         f.write("black = %d\n" % self.black)
      if self.white:         f.write("white = %d\n" % self.white)
      if self.converted_mana_cost: f.write("converted mana cost = %d\n" %\
                                            self.converted_mana_cost)
      if self.types:         f.write("type = %s\n" % self.types)
      if self.subtype:       f.write("sub type = %s\n" % self.subtype)
      if self.card_text:     f.write("card text = %s\n" % self.card_text)
      if self.flavor_text:   f.write("flavor text = %s\n" % self.flavor_text)
      if self.power:         f.write("power = %s\n" % self.power)
      if self.toughness:     f.write("toughness = %s\n" % self.toughness)
      if self.expansion:     f.write("expansion = %s\n" % self.expansion)
      if self.rarity:        f.write("rarity = %s\n" % self.rarity)
      if self.card_number:   f.write("card number = %s\n" % self.card_number)
      if self.artist:        f.write("artist = %s\n" % self.artist)
      f.flush()
      f.close()
      
BUF = Stats()

session = requests.session()
base_name = "http://gatherer.wizards.com/pages/Card/Details.aspx?multiverseid="

card_name = re.compile('[ \t](Card Name:)\<\/div\>')
mana_cost = re.compile('[ \t](  Mana Cost:)\<\/div\>')
converted_mana_cost = re.compile('[ \t](Converted Mana Cost:)\<\/div\>')
colorless = re.compile('(alt="[0-9]{1,2}")')
red       = re.compile('(alt="Red")')
green     = re.compile('(alt="Green")')
blue      = re.compile('(alt="Blue")')
black     = re.compile('(alt="Black")')
white     = re.compile('(alt="White")')
num       = re.compile('[0-9]{1,2}')
types     = re.compile('Types:')
parts     = re.compile("([\w\s]+)\xe2\x80\x94([\w\s]+)")
part      = re.compile("([\w\s]+)")
card_text = re.compile("(Card Text:)")
text_part = re.compile("<[^>]*>(.*?)<[^>]*>")
flavor_text = re.compile("(Flavor Text:)")
flavor_part = re.compile("</?i>(.*?)</?i>[^\r]")
not_r     = re.compile("[^\r]+")
pow_tof   = re.compile("P/T:")
PTparts   = re.compile("\d{1,2}|\*\s/\s\d{1,2}|\*")
Expansion = re.compile("Expansion:")
exp_part  = re.compile(">(.*?)</a>")
rarity    = re.compile("Rarity:")
card_number = re.compile("Card Number:")
number_part = re.compile("\d{1,4}")
artist    = re.compile("Artist:")


for multiverse_id in range(320000, 340000):
   page_defined.setFalse(multiverse_id)
   req = session.get(base_name + str(multiverse_id))
   cont = req.content.split('\n')
   BUF.set2null()

   BUF.multiverse_id = multiverse_id
   for i,line in enumerate(cont):
   
      # Card name
      if card_name.findall(line):
         try:
            BUF.card_name = cont[i+2].strip()[0:-6]
            page_defined.setTrue()
         except Exception:
            continue
            
      # Mana cost
      elif mana_cost.findall(line):
         try:
            mc = cont[i+2].strip()
            tmp = colorless.findall(mc)
            if tmp:
               BUF.colorless = int(tmp[0][5:-1])
            BUF.red = len(red.findall(mc))
            BUF.green = len(green.findall(mc))
            BUF.blue = len(blue.findall(mc))
            BUF.black = len(black.findall(mc))
            BUF.white = len(white.findall(mc))
         except Exception:
            continue
         
      # Converted mana cost
      elif converted_mana_cost.findall(line):
         try:
            BUF.converted_mana_cost = int(num.findall(cont[i+2].strip())[0])
         except Exception:
            continue
         
      # Card type
      elif types.findall(line):
         try:
            BUF.types = cont[i+2].strip()[0:-6]
            tmp = parts.findall(cont[i+2].strip()[0:-6])
            if tmp and len(tmp[0])>1:
               BUF.types = tmp[0][0].strip()
               BUF.subtype = tmp[0][1].strip()
            else:
               BUF.types = part.findall(cont[i+2].strip()[0:-6])[0]
         except Exception:
            continue
            
      # Card text
      elif card_text.findall(line):
         try:
            tmp = text_part.findall(cont[i+2].strip())
            BUF.card_text = ""
            for string in tmp:
               if string:
                  BUF.card_text += string + ' '
            BUF.card_text = BUF.card_text[0:-1]
         except Exception:
            continue
      
      # Flavor text
      elif flavor_text.findall(line):
         try:
            tmp = flavor_part.findall(cont[i+2].strip())
            BUF.flavor_text = ""
            for string in tmp:
               BUF.flavor_text += not_r.findall(string)[0] + ' '
            BUF.flavor_text = BUF.flavor_text[0:-1]
         except Exception:
            continue
      
      # Power / toughness
      elif pow_tof.findall(line):
         try:
            tmp = PTparts.findall(cont[i+2].strip())
            BUF.power = tmp[0]
            BUF.toughness = tmp[1]
         except Exception:
            continue
      
      # Expansion
      elif Expansion.findall(line):
         try:
            BUF.expansion = exp_part.findall(cont[i+4].strip())[0]
         except Exception:
            continue
      
      # Rarity
      elif rarity.findall(line):
         try:
            BUF.rarity = text_part.findall(cont[i+2].strip())[0]
         except Exception:
            continue
      
      # Card number
      elif card_number.findall(line):
         try:
            BUF.card_number = number_part.findall(cont[i+2].strip())[0]
         except Exception:
            continue
      
      # Artist
      elif artist.findall(line):
         try:
            BUF.artist = text_part.findall(cont[i+2].strip())[0]
         except Exception:
            continue
      
   # write out to file and std
   if page_defined.isTrue():
      print "\n",
      if BUF.card_name:           print BUF.card_name
      if BUF.multiverse_id:       print "multiverse_id = %d" % BUF.multiverse_id
      if BUF.colorless:           print "colorless = %d" % BUF.colorless
      if BUF.red:                 print "red = %d" % BUF.red
      if BUF.green:               print "green = %d" % BUF.green
      if BUF.blue:                print "blue = %d" % BUF.blue
      if BUF.black:               print "black = %d" % BUF.black
      if BUF.white:               print "white = %d" % BUF.white
      if BUF.converted_mana_cost: print "converted mana cost = %d" % BUF.converted_mana_cost
      if BUF.types:               print "type = %s" % BUF.types
      if BUF.subtype:             print "sub type = %s" % BUF.subtype
      if BUF.card_text:           print "card text = %s" % BUF.card_text
      if BUF.flavor_text:         print "flavor text = %s" % BUF.flavor_text
      if BUF.power:               print "power = %s" % BUF.power
      if BUF.toughness:           print "toughness = %s" % BUF.toughness
      if BUF.expansion:           print "expansion = %s" % BUF.expansion
      if BUF.rarity:              print "rarity = %s" % BUF.rarity
      if BUF.card_number:         print "card number = %s" % BUF.card_number
      if BUF.artist:              print "artist = %s" % BUF.artist

      # write to file
      File = os.environ["HOME"] + "/Desktop/database"
      BUF.write2File(File)
