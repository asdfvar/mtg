#!/usr/bin/python
# the player class has all the attributes for the player. When stored in a list, this can express multiple players

'''
W - white
U - blue
B - black
R - red
G - green
Z - multicolor
X - split cards
A - artifact
L - land

C - common
U - uncommon
R - rare
M - mythic rare
L - land
T - token
S - special
'''


import re
import cmd
import sys

import player
import creature
import land

import mtg_game

play_game = True

if play_game:
   mtg_game
