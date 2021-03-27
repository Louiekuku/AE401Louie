# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:00:31 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
x,y,z = mc.player.getTilePos()
for i in range(5):
    for j in range(5):
        for k in range(5):
            plantTree(x + i*5, y + i*j, z + i*k)
    
    
    