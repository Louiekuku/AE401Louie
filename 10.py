# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:00:57 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

x,y,z = mc.player.getTilePos()

for i in range(20) :
    r = random.randrange(1,5)
    
    if r == 1:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x = x + 4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x = x - 4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z = z + 4
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z == z - 4
        
while True:
    mc.executeCommand('time add 50')
    time.sleep(0.5)