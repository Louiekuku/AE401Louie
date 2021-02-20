# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:10:47 2021

@author: louie
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

try:
    a = int(input('enter your block:'))
    mc.setBlock(x,y,z,a)


except:
    print('plz enter numbers')
    
    
name = input('enter your name:')
message = input('enter your messege:')
mc.postToChat(' <'+ name + '> ' + message)