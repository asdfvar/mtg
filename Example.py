#!/usr/bin/python
import cards

dbase = cards.cards()

dbase.get_from_database("database")

dbase.rmExpansion()
#dbase.rmRepeats()

#dbase.findname("Black Lotus")
#dbase.findname("Yawgmoth Demon")
