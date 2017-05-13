#!/usr/bin/python
# -*- coding: utf-8 -*-

# define colors and color utilities for plots
import numpy as np
import matplotlib.pyplot as plt

fte_colors = ["#30a2da","#fc4f30","#fab52f","#32a273","#8b8b8b","#32a273","#9c75c7"]
fte_colors_dark = ["#1c5f80","#a6341f","#8c6b22","#29361d","#333333","#2b654a","#6a3d9a"]
fte_colors_light = ["#96d0ec","#feb4a6","#f3d9a1","#aac494","#c7c7c7","#80d87b","#cfbce4"]
bg_colors = ["#50ade5","#bf1b2c","#512268"]
bg_colors_wt = [fte_colors_light[0],fte_colors_light[1],fte_colors_light[6]]
bg_colors_mut = [fte_colors[0],fte_colors[1],fte_colors_dark[6]]
t_colors = [plt.cm.viridis_r(x) for x in np.linspace(0, 1, 6)]