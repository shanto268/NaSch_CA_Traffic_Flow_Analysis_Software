# -*- coding: utf-8 -*-
"""
Created on Thu May 30 18:33:09 2019

@author: Owner
"""
import scipy.stats
from PIL import Image
'''
background = Image.open("New-model-3lane-dedicated.png")
overlay = Image.open("New-model-3lane-no-dedicated.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("nemodelw.png","PNG")
'''
scipy.stats.norm(30, 5).pdf(1)