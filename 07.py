# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:12:00 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(10):
    mc.setBlock(x,y-1,z+i,1)
    
for i in range(10):
    mc.setBlocks(x+i,y-1,z+i,x+i,y-1,z+i+3,1)
    
mc.setBlocks(x+2,y+2,z+2,x,y,z,1)
mc.setBlocks(x,y-5,z,x,y+1,z,17)
