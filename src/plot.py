# -*- coding: utf-8 -*-
hatches = []

import colors, utils

import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib import lines,ticker
from matplotlib.patches import Polygon
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import numpy as np

def boxplot_custom(bp, ax, colors=colors, hatches=hatches):
    for i in range(len(bp['boxes'])):
        box = bp['boxes'][i]
        box.set_linewidth(0)
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
            boxCoords = zip(boxX,boxY)
            boxPolygon = Polygon(boxCoords, 
                                 facecolor = colors[i % len(colors)], 
                                 linewidth=0, 
                                 hatch = hatches[i % len(hatches)])
            ax.add_patch(boxPolygon)

    for i in range(0, len(bp['boxes'])):
        bp['boxes'][i].set_color(colors[i])
        #bp['boxes'][i].set_hatch('/')

        # we have two whiskers!
        bp['whiskers'][i*2].set(color=colors[i], 
                                linewidth=1.5,
                                linestyle='-')
        bp['whiskers'][i*2 + 1].set(color=colors[i], 
                                linewidth=1.5,
                                linestyle='-')
        # top and bottom fliers
        bp['fliers'][i].set(markerfacecolor=colors[i],
                            marker='o', alpha=0.75, markersize=3,
                            markeredgecolor='none')
        bp['medians'][i].set_color('black')
        bp['medians'][i].set_linewidth(2)
        # and 4 caps to remove
        for c in bp['caps']:
            c.set_linewidth(0)

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.tick_params(axis='y', length=0)

    ax.grid(axis='y', color="0.9", linestyle='-', linewidth=1)
    ax.set_axisbelow(True)
    
    
from matplotlib.collections import PatchCollection


def heatmap_spores(S, ax, title, xlabel, ylabel, xticklabels, yticklabels, fold=False, cmap='RdBu', radius=0.25):
    '''
    
    '''
    
    dict_mat = {u'MATa':{'x':[-radius]*len(S.loc[u'MATa']), 'y':np.arange(0.5,len(S.loc[u'MATa']))},
                u'MATα':{'x':np.arange(0.5,len(S.loc[u'MATα'])), 'y':[-radius]*len(S[u'MATα'])}}
    
    for mating in dict_mat.iterkeys():
        data = map(list, zip(*[dict_mat[mating]['x'], dict_mat[mating]['y']]))
        circles = [plt.Circle([x, y], radius) for (x, y) in data]
        col = PatchCollection(circles, edgecolor='black', lw=0.75)

        s = S.ix[mating].values
        
        # shift colormap
        orig_cmap = cmap
        mid = (1 - np.ma.max(S)/(np.ma.max(S) + abs(np.ma.min(S))))
                    
        shifted_cmap = utils.shift_colormap(orig_cmap, midpoint=mid, name='shifted')
        shifted_cmap.set_bad('w')
        
        col.set(array=s, cmap=shifted_cmap)
        col.set_clip_on(False)

        ax.add_collection(col)
        
    return dict_mat


def heatmap_hybrids(M, ax, title, xlabel, ylabel, xticklabels, yticklabels, fold=False, cmap='RdBu', pad=0.25, legend_title=''):
    '''
    '''
    
    if fold:
        #
        X = M.values
        Y = M.values.T
        # calculate the element-wise average of the two matrices
        Z = np.add(X, Y) / 2.
        Z = np.tril(Z) # get the lower triangle of the matrix
        Z = np.ma.masked_array(Z, Z == 0) # mask the upper triangle
    else:
        Z = M.values

    # Shift colormap
    orig_cmap = cmap
    mid=(1 - np.ma.max(Z)/(np.ma.max(Z) + abs(np.ma.min(Z))))

    shifted_cmap = utils.shift_colormap(orig_cmap, midpoint=mid, name='shifted')
    shifted_cmap.set_bad('w') # default value is 'k'

    im = ax.pcolor(Z, edgecolors='lightgrey', linewidths=0.5, cmap=shifted_cmap)
    
    # Place the major ticks at the middle of each cell
    ax.set_xticks(np.arange(Z.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(Z.shape[0]) + 0.5, minor=False)

    # set tick labels
    ax.set_xticklabels(xticklabels, minor=False, rotation=90)
    ax.set_yticklabels(yticklabels, minor=False)
    
    # set title and x/y labels
    ax.set_title(title, fontsize=6, y=1.15)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    # Remove last blank column
    ax.set_xlim( (0, Z.shape[1]) )
    ax.set_ylim( (0, Z.shape[0]) )
    
    # Turn off all the ticks
    for t in ax.xaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False
    for t in ax.yaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False
        
    # Proper orientation (origin at the top left instead of bottom left)
    ax.invert_yaxis()

    # add colorbar
    cax = inset_axes(ax, width='3%', height='50%', loc=3,
                     bbox_to_anchor=(1.05, 0., 1, 1),
                     bbox_transform=ax.transAxes,
                     borderpad=0)
    cbar = plt.colorbar(im, cax=cax)
    cbar.ax.set_title(legend_title, horizontalalignment='left', fontsize=6)
    cbar.ax.tick_params(labelsize=4)
    cbar.locator = ticker.MaxNLocator(nbins = 3)
    cbar.ax.yaxis.set_major_locator(ticker.AutoLocator())

    
def set_custom_labels(index, pos):
    """
    
    """
    start = dict((m[pos], ii) for ii,m in enumerate(index.values))
    end = dict((m[pos], len(index)-ii-1) for ii,m in enumerate(index[::-1].values))
    labels = {key: (start[key] + end.get(key, 0))/2. for key in end.keys()}
    
    return start, end, labels


def add_inner_title(ax, title, loc, size=None, **kwargs):
    from matplotlib.offsetbox import AnchoredText
    from matplotlib.patheffects import withStroke
    if size is None:
        size = dict(size=plt.rcParams['legend.fontsize'])
    at = AnchoredText(title, loc=loc, prop=size,
                      pad=0., borderpad=0.5,
                      frameon=False, **kwargs)
    ax.add_artist(at)
    at.txt._text.set_path_effects([withStroke(foreground="w", linewidth=3)])
    return at
    

from matplotlib.transforms import Bbox, TransformedBbox, \
    blended_transform_factory

from mpl_toolkits.axes_grid1.inset_locator import BboxPatch, BboxConnector,\
    BboxConnectorPatch


def connect_bbox(bbox1, bbox2,
                 loc1a, loc2a, loc1b, loc2b,
                 prop_lines, prop_patches=None):
    if prop_patches is None:
        prop_patches = prop_lines.copy()
        prop_patches["alpha"] = prop_patches.get("alpha", 1)*0.2

    c1 = BboxConnector(bbox1, bbox2, loc1=loc1a, loc2=loc2a, **prop_lines)
    c1.set_clip_on(False)
    c2 = BboxConnector(bbox1, bbox2, loc1=loc1b, loc2=loc2b, **prop_lines)
    c2.set_clip_on(False)

    bbox_patch1 = BboxPatch(bbox1, **prop_patches)
    bbox_patch2 = BboxPatch(bbox2, **prop_patches)

    p = BboxConnectorPatch(bbox1, bbox2,
                           # loc1a=3, loc2a=2, loc1b=4, loc2b=1,
                           loc1a=loc1a, loc2a=loc2a, loc1b=loc1b, loc2b=loc2b,
                           **prop_patches)
    p.set_clip_on(False)

    return c1, c2, bbox_patch1, bbox_patch2, p


def zoom_effect(ax1, ax2, xmin, xmax, **kwargs):
    """
    ax1 : the main axes
    ax1 : the zoomed axes
    (xmin,xmax) : the limits of the colored area in both plot axes.

    connect ax1 & ax2. The x-range of (xmin, xmax) in both axes will
    be marked.  The keywords parameters will be used to create
    patches.

    """

    trans1 = blended_transform_factory(ax1.transData, ax1.transAxes)
    trans2 = blended_transform_factory(ax2.transData, ax2.transAxes)

    bbox = Bbox.from_extents(xmin, 0, xmax, 1)

    mybbox1 = TransformedBbox(bbox, trans1)
    mybbox2 = TransformedBbox(bbox, trans2)

    prop_patches = kwargs.copy()
    prop_patches["ec"] = "none"
    prop_patches["alpha"] = 0.2

    c1, c2, bbox_patch1, bbox_patch2, p = \
        connect_bbox(mybbox1, mybbox2,
                     loc1a=3, loc2a=2, loc1b=4, loc2b=1,
                     prop_lines=kwargs, prop_patches=prop_patches)

    ax1.add_patch(bbox_patch1)
#     ax2.add_patch(bbox_patch2)
    ax2.add_patch(c1)
    ax2.add_patch(c2)
    ax2.add_patch(p)

    return c1, c2, bbox_patch1, bbox_patch2, p
