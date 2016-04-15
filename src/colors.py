#!/usr/bin/python
# -*- coding: utf-8 -*-

# define colors and color utilities for plots
from matplotlib.colors import colorConverter, LinearSegmentedColormap, cnames
import brewer2mpl

hatches = [' ', ' ', ' ', ' ', ' ']

my_colors = [(62, 62, 61), (217, 77, 77), (235, 165, 56),(75, 179, 210),(140, 173, 109)]#, (75, 179, 210),(140, 173, 109),
my_colors = [(c[0]/256.,c[1]/256.,c[2]/256.) for c in my_colors]

bmh_colors=["#348abd","#a60628","#7a68a6","#467821","#cf4457","#188487","#e24A33"]
fte_colors=["#30a2da","#fc4f30","#e5ae38","#6d904f","#8b8b8b","#32a273"]
fte_colors_dark=["#1c5f80","#a6341f","#8c6b22","#29361d","#333333","#2b654a"]
fte_colors_light=["#96d0ec","#feb4a6","#f3d9a1","#aac494","#c7c7c7","#80d87b"]
mr_colors=["#243b52","#328b87","#80d07f"]
bg_colors=["#50ade5","#bf1b2c","#512268"]
t_colors=["#80d07f","#60b487","#328b87","#245d5c","#243b52","#242e3e"]
