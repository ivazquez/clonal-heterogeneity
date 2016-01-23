#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define colors and color utilities for plots

from matplotlib.colors import colorConverter, LinearSegmentedColormap, cnames
import brewer2mpl
# import colorbrewer

COLOR_MAP = {
    "red":"#e41a1c",
    "blue":"#377eb8",
    "green":"#4daf4a",
    "purple":"#984ea3",
    "orange":"#ff7f00",
    "yellow":"#ebbc57",
    "brown":"#a65628",
    "pink": "#f781bf", 
    "grey": "#999999",
    "white": "#ffffff",
    "black": "#000000",
}

bmap = brewer2mpl.get_map('Set2', 'qualitative', 8)
colors = bmap.mpl_colors
hatches = [' ', ' ', ' ', ' ', ' ']

reds = brewer2mpl.get_map('Reds', 'Sequential', 9).mpl_colors
greens = brewer2mpl.get_map('Greens', 'Sequential', 9).mpl_colors
blues = color = brewer2mpl.get_map('Blues', 'Sequential', 9).mpl_colors
color = brewer2mpl.get_map('Paired', 'qualitative', 12).mpl_colors
pastel1 = brewer2mpl.get_map('Pastel1', 'qualitative', 9)
set1 = brewer2mpl.get_map('Set1', 'qualitative', 9)
pastel2 = brewer2mpl.get_map('Pastel2', 'qualitative', 8)
set2 = brewer2mpl.get_map('Set2', 'qualitative', 8)
dark2 = brewer2mpl.get_map('Dark2', 'qualitative', 8)
bmap = brewer2mpl.get_map('Paired', 'qualitative', 12)
colors = bmap.mpl_colors

my_colors = [(62, 62, 61), (217, 77, 77), (235, 165, 56),(75, 179, 210),(140, 173, 109)]#, (75, 179, 210),(140, 173, 109),
my_colors = [(c[0]/256.,c[1]/256.,c[2]/256.) for c in my_colors]

bmh_colors=["#348ABD","#A60628","#7A68A6","#467821","#CF4457","#188487","#E24A33"]
fte_colors=["#30a2da","#fc4f30","#e5ae38","#6d904f","#8b8b8b","#32a273"]
fte_colors_dark=["#1c5f80","#a6341f","#8c6b22","#29361d","#333333","#2b654a"]
fte_colors_light=["#96d0ec","#feb4a6","#f3d9a1","#aac494","#c7c7c7","#80d87b"]
mr_colors=["#243b52","#328b87","#80d07f"]
bg_colors=["#50ade5","#bf1b2c","#512268"]

# def is_pal(name):
#     return colorbrewer.__dict__.has_key(name)
#
# def get_pal(name, n=None):
#     ns = colorbrewer.__dict__[name].keys()
#     if n > max(ns) or not n:
#         n_index = max(ns)
#     elif n < min(ns):
#         n_index = min(ns)
#     else:
#         n_index = n
#
#     pal = colorbrewer.__dict__[name][n_index][:n]
#     for i in range(len(pal)):
#         pal[i] = [x/255.0 for x in pal[i]]
#
#     return pal
#
# DEFAULT_COLORS = get_pal("Set1")
#
# def parse_colors(colors):
#     if type("") == type(colors):
#         colors = [x.strip() for x in colors.split(",")]
#
#     parsed = []
#     for c in colors:
#         if type("") == type(c):
#             # Named color
#             if COLOR_MAP.has_key(c):
#                 parsed.append(COLOR_MAP[c])
#             elif cnames.has_key(c):
#                 parsed.append(cnames[c])
#             elif is_pal(c):
#                 # c is a Colorbrewer palette name
#                 parsed += get_pal(c)
#             elif len(c.split(":")) == 2:
#                 p,n = c.split(":")
#                 if is_pal(p):
#                     parsed += get_pal(p, int(n))
#                 else:
#                     raise ValueError("%s is not a valid colorbrewer name!" % p)
#             # Hex code?
#             else:
#                 if c.startswith("#"):
#                     parsed.append(c)
#                 else:
#                     try:
#                         int(c, 16)
#                         parsed.append("#" + c)
#                     except:
#                         raise ValueError("Unknown color definition %s" % c)
#         else:
#             # c is not a strint, assume it's already a valid color
#             parsed.append(c)
#     return parsed
#
# def create_colormap(col1, col2):
#     c1 = colorConverter.to_rgb(col1)
#     c2 = colorConverter.to_rgb(col2)
#
#     cdict = {
#         'red': ((0.,c1[0], c1[0]),(1.,c2[0], c2[0])),
#         'green': ((0.,c1[1], c1[1]),(1.,c2[1], c2[1])),
#         'blue': ((0.,c1[2], c1[2]),(1.,c2[2], c2[2]))
#     }
#     return LinearSegmentedColormap('custom', cdict, 256)
#
