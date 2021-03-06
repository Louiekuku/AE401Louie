# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        if block == 1:
            mc.setBlock(x,y,z,41)
        
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,0,"1","2","3","4")

import random
import time

i = 1
while i < 20:
    pos = mc.player.getpos()
    i = i + 1
    x = pos.x + random.uniform(-20,20)
    y = pos.y + random.uniform(3,0) 
    z = pos.z + random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,93)
    time.sleep(0,1)