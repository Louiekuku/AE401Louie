# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:08:55 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def buildPyramid(x,y,z):
    base = 50
    height = (base//2) + 1
    
    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        x2 = x + base - i
        z2 = z + base - i
        mc.setBlocks(x1,y1,z1,x2,y,z2,24)
        
x,y,z = mc.player.getTilePos()
buildPyramid(x,y,z)

line1 = []
line2 = []
line3 = []

for i in range(1,4):
    line1.append(1*i)
    
for i in range(1,4):
    line2.append(2*1)
    
for i in range(1,4):
    line3.append(3*i)
    
x,y,z = mc.player.getPos()

mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))