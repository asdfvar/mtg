class Mana:
   def __init__(self):
      pass
   colorless = 0
   white = 0
   black = 0
   green = 0
   blue = 0
   red = 0

   def add_white(self, n):
      self.white += n

   def add_black(self, n):
      self.black += n

   def add_green(self, n):
      self.green += n

   def add_blue(self, n):
      self.blue += n

   def add_red(self, n):
      self.red += n

   def add_colorless(self, n):
      self.colorless += n

   def remove_white(self, n):
      self.white -= n

   def remove_black(self, n):
      self.black -= n

   def remove_green(self, n):
      self.green -= n

   def remove_blue(self, n):
      self.blue -= n

   def remove_red(self, n):
      self.red -= n

   def remove_colorless(self, n):
      self.colorless -= n

   def remove_all_mana(self):
      self.colorless = 0
      self.white     = 0
      self.black     = 0
      self.green     = 0
      self.blue      = 0
      self.red       = 0
