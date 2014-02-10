#!/usr/bin/python
import requests
import re

class Page_defined():
   defined = False
   counter = 0
   def setFalse(self):
      self.defined = False
      self.counter+=1
      if self.counter % 20 == 0:
         print "%d undefined pages thus far"\
               % self.counter
   def setTrue(self):
      self.defined = True
      self.counter=0
   def isTrue(self):
      return self.defined

page_defined = Page_defined()

class Stats:
   def settodef(self):
      self.multiverse_id = None
      self.colorless = None
      self.red = None
      self.green = None
      self.blue = None
      self.black = None
      self.white = None
      self.converted_mana_cost = None
      self.types = None
      self.subtype = None

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

for k in range(373645,373660):
   page_defined.setFalse()
   req = session.get(base_name + str(k))
   cont = req.content.split('\n')
   BUF.settodef()

   BUF.multiverse_id = k
   for i,line in enumerate(cont):
      if card_name.findall(line):
         BUF.card_name = cont[i+2].strip()[0:-6]
         page_defined.setTrue()
      elif mana_cost.findall(line):
         mc = cont[i+2].strip()
         tmp = colorless.findall(mc)
         if tmp:
            BUF.colorless = int(tmp[0][5:-1])
         BUF.red = len(red.findall(mc))
         BUF.green = len(green.findall(mc))
         BUF.blue = len(blue.findall(mc))
         BUF.black = len(black.findall(mc))
         BUF.white = len(white.findall(mc))
      elif converted_mana_cost.findall(line):
         BUF.converted_mana_cost = int(num.findall(cont[i+2].strip())[0])
      elif types.findall(line):
         BUF.types = cont[i+2].strip()[0:-6]
         tmp = parts.findall(cont[i+2].strip()[0:-6])
         if tmp and len(tmp[0])>1:
            BUF.types = tmp[0][0].strip()
            BUF.subtype = tmp[0][1].strip()
         else:
            BUF.types = part.findall(cont[i+2].strip()[0:-6])[0]
            BUF.subtype = ""

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
