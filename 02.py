# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 10:12:02 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = -4
y = 71
z = 265

mc.player.setTilePos(x,y,z)
time.sleep(3)
y = y+1
mc.player.setTilePos(x,y,z)
time.sleep(3)
y = y+1
mc.player.setTilePos(x,y,z)

t=0

while True:
    t = t + 1
    mc.postToChat(str(t) + 'times')
    
    
while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("x:" + str(x) + "y:" + str(y) + "z:" + str(z))
