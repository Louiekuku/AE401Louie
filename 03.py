# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:15:18 2021

@author: louie
"""
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(5)
x,y,z = mc.player.getTilePos()

mc.setBlock(x,y,z,202)
mc.setBlock(x,y+1,z,202)
mc.setBlock(x,y+2,z,202)
mc.setBlock(x,y+3,z,202)
mc.setBlock(x,y+4,z,202)
mc.setBlock(x,y+5,z,202)
mc.setBlock(x,y+6,z,202)
mc.setBlock(x,y+7,z,202)
mc.setBlock(x,y+8,z,202)
mc.setBlock(x,y+9,z,202)
mc.setBlock(x,y+10,z,202)


mc.setBlock(x+1,y,z,202)
mc.setBlock(x-1,y,z,202)
mc.setBlock(x,y,z+1,202)
mc.setBlock(x,y,z-1,202)
mc.setBlock(x+1,y,z+1,202)
mc.setBlock(x-1,y,z-1,202)
mc.setBlock(x+1,y,z-1,202)
mc.setBlock(x-1,y,z+1,202)


mc.setBlocks(x+50, y+50, z+50, x-50, y-50, z-50, 0)