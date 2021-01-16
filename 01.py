# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 10:39:28 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#print(mc.player.getTilePos())

x = 0 
y = 1
z = 0

mc.player.setTilePos(x,y,z)