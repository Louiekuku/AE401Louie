# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:03:33 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import choice

mineral = [14,15,16,56,73,129]

r = choice(mineral)

myID = mc.getPlayerEntityIde('King_Louie1231')
x,y,z = mc.entity.getTilePos(myID)
mc.setBlock(x,y,z,r)

list2d = [[12,41,14],[35,73,86]]

x,y,z = mc.player.getTilePos()
startX = x

for list1d in list2d:
    
    for i in list1d:
        mc.setBlock(x,y,z,i)
        
        x = x + 1
        
    x = startX
    z = z+1
    
x,y,z = mc.player.getTilePos()
    
try:
    blockType = int(input('enter your blockID'))
    mc.setBlock(x,y,z,blockType)
        
except:
    print('enter numbers!!!')