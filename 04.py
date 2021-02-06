# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:07:15 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
width = 10
height = 6
length = 5

mc.setBlocks(x,y,z,x+width,y+height,z+length,5)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,0)

while True:
    x,y,z = mc.player.getTilePos()
    
    a = mc.getBlock(x+1,y-1,z)
    b = mc.getBlock(x-1,y-1,z)
    c = mc.getBlock(x,y-1,z+1)
    d = mc.getBlock(x,y-1,z-1)
    
    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,416)
        
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x+1,y,z+1,x-1,y,z-1,47)

x,y,z = mc.player.getTilePos()
a = 0
while a < 8:
    mc.setBlocks(x+30,y-1,z,x-30,y-10,z,19)
    z = z + 5
    a = a + 1