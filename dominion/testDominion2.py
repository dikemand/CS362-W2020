# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:08:30 2020

@author: Daemon Dikeman
"""
import Dominion
from collections import defaultdict
import testUtility

#Get player names
player_names = testUtility.NameStart()

#number of curses and victory cards
nlist = testUtility.CVStart(player_names)
nV = nlist[0]
nC = nlist[1]

#Define box
box = testUtility.BoxStart(nC)

#Define Supply Order
supply_order = testUtility.SupplyOrderStart()

#Pick 10 cards from box to be in the supply.
supply = testUtility.ShuffleStart(box)

#The supply always has these cards
supply = testUtility.SupplyBaseStart(supply, player_names, nC, nV)

#initialize the trash
trash = testUtility.TrashStart()

#Costruct the Player objects
players = testUtility.PlayerStart(player_names)


#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
