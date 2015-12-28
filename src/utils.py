#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter,NullLocator
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import pandas as pd

def save_fig(path, ext='png', close=True, verbose=True):
    """Save a figure from pyplot.
    Parameters
    ----------
    path : string
        The path (and filename, without the extension) to save the
        figure to.
    ext : string (default='png')
        The file extension. This must be supported by the active
        matplotlib backend (see matplotlib.backends module).  Most
        backends support 'png', 'pdf', 'ps', 'eps', and 'svg'.
    close : boolean (default=True)
        Whether to close the figure after saving.  If you want to save
        the figure multiple times (e.g., to multiple formats), you
        should NOT close it in between saves or you will have to
        re-plot it.
    verbose : boolean (default=True)
        Whether to print information about when and where the image
        has been saved.
    """
    
    # Extract the directory and filename from the given path
    directory = os.path.split(path)[0]
    filename = "%s.%s" % (os.path.split(path)[1], ext)
    if directory == '':
        directory = '.'

    # If the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # The final path to save to
    savepath = os.path.join(directory, filename)

    if verbose:
        print("Saving figure to '%s'..." % savepath),

    # Actually save the figure
    plt.savefig(savepath)
    
    # Close it
    if close:
        plt.close()

    if verbose:
        print("Done")
        
def load_data(fn):
    '''Load the data for the plots
    
    Input
    -----
      fn : filename 
    '''
    import cPickle as pickle
    with open(fn, 'rb') as f:
        return pickle.load(f)
        
def save_data(data, fn):
    '''Store data to file for the plots
    
    Input
    -----
      data : pandas dataframe
      fn : filename 
    '''
    import cPickle as pickle
    with open(fn, 'wb') as f:
        pickle.dump(data, f, protocol=-1)

def create_grid_figure(nrows, ncolumns, plotwidth=2.0, plotheight=2.0, pad=0.1, padleft=0.1, padright=0.1, padtop=0.1, padbottom=0.1, clean=True):
    '''
    Function to...

    Input
    -----
      nrows : 
      ncols : 
      plotwidth : 
      plotheight : 
      pad : 
      padleft : 
      padright : 
      padtop : 
      padbottom : 
      clean : 
    '''
    wsize = padleft + (ncolumns * plotwidth) + (pad * (ncolumns - 1)) + padright
    hsize = padtop + (nrows * plotheight) + (pad * (nrows - 1)) + padbottom
    fig = plt.figure(figsize=(wsize, hsize))
    wpadfraction = pad / wsize
    hpadfraction = pad / hsize
    wplotsize = plotwidth / wsize
    hplotsize = plotheight / hsize 
    axes = {}
    # Create all the subplots
    for row in range(nrows):
        axes[row] = {}
        for col in range(ncolumns):
            axes[row][col] = plt.subplot(nrows, ncolumns, row * ncolumns + col + 1)
            
            # No labels, ticks, etc.
            if clean:
                for ax in [axes[row][col].xaxis, axes[row][col].yaxis]:
                    ax.set_major_formatter(NullFormatter())
                    ax.set_major_locator(NullLocator())
    
    # Resize all the subplots
    for row in range(nrows):
        for col in range(ncolumns):
            x0 = (padleft / wsize ) + (wplotsize + wpadfraction) * col
            x1 = wplotsize
            y0 = (padbottom / hsize) + (nrows - row - 1) * (hplotsize + hpadfraction) 
            y1 = hplotsize
            coords = [x0, y0, x1, y1]
            axes[row][col].set_position(coords)

            for s in axes[row][col].spines.values():
                s.set_linewidth(0.8)

    return fig, axes


# Noticeable points
count = 0
def highlight(ax, x, y, reason):
    global count
    #if index and index > 0:
    #    x,y = (ava['seconds_elapsed'][index],
    #           smooth(ava['successful_transactionssecond'])[index])
    #    plot([x], [y], 'ko')
    ax.annotate('%d TPS\n(%s)' % (y,reason), xy=(x,y),
                xytext=(20, -(count+4.7)*22), textcoords='axes points',
                arrowprops=dict(arrowstyle="-",
                connectionstyle="angle,angleA=0,angleB=80,rad=10"),
                horizontalalignment='left',
                verticalalignment='bottom',
                fontsize=8)


def hide_axes(ax):
    '''
    Function to...

    Input
    -----
      ax : 
    '''
    for x in [ax.xaxis, ax.yaxis]:
        x.set_major_formatter(NullFormatter())
        x.set_major_locator(NullLocator())
    for loc,spine in ax.spines.iteritems():
        spine.set_color('none')
        
        
def simple_axes(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
        
            
def annotate_group(name, yspan, ax=None):
    '''
    Annotates a span of the y-axis
    http://stackoverflow.com/questions/3918028/how-do-i-plot-multiple-x-or-y-axes-in-matplotlib 
    '''
    def annotate(ax, name, left, right, x, pad):
        arrow = ax.annotate(name,
                xy=(left, x), xycoords='data',
                xytext=(right, x-pad), textcoords='data',
                annotation_clip=False, verticalalignment='top',
                horizontalalignment='center', linespacing=2.0#,
                # arrowprops=dict(arrowstyle='-', shrinkA=0, shrinkB=0,
             #            connectionstyle='angle,angleB=90,angleA=0,rad=5')
                )
        return arrow
    if ax is None:
        ax = plt.gca()
    xmin = ax.get_xlim()[0]
    xpad = 0.01 * np.ptp(ax.get_xlim())
    ycenter = np.mean(yspan)
    left_arrow = annotate(ax, name, yspan[0], ycenter, xmin, xpad)
    right_arrow = annotate(ax, name, yspan[1], ycenter, xmin, xpad)
    return left_arrow, right_arrow
        
        
def force_aspect(ax,aspect=1):
    '''
    
    http://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
    '''
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)


def shift_colormap(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    '''
    Function to offset the "center" of a colormap. Useful for
    data with a negative min and positive max and you want the
    middle of the colormap's dynamic range to be at zero

    Input
    -----
      cmap : The matplotlib colormap to be altered
      start : Offset from lowest point in the colormap's range.
          Defaults to 0.0 (no lower ofset). Should be between
          0.0 and `midpoint`.
      midpoint : The new center of the colormap. Defaults to 
          0.5 (no shift). Should be between 0.0 and 1.0. In
          general, this should be  1 - vmax/(vmax + abs(vmin))
          For example if your data range from -15.0 to +5.0 and
          you want the center of the colormap at 0.0, `midpoint`
          should be set to  1 - 5/(5 + 15)) or 0.75
      stop : Offset from highets point in the colormap's range.
          Defaults to 1.0 (no upper ofset). Should be between
          `midpoint` and 1.0.
    '''
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }

    # regular index to compute the colors
    reg_index = np.linspace(start, stop, 257)

    # shifted index to match the data
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False), 
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])

    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)

        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))

    newcmap = LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap=newcmap)

    return newcmap

def discrete_colormap(N, base_cmap=None):
    """Create an N-bin discrete colormap from the specified input map"""

    # Note that if base_cmap is a string or None, you can simply do
    #    return plt.cm.get_cmap(base_cmap, N)
    # The following works for string, None, or a colormap instance:

    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)

def percentile(data):
    median = np.zeros(data.shape[1])
    perc_25 = np.zeros(data.shape[1])
    perc_75 = np.zeros(data.shape[1])
    for i in range(0, len(median)):
        median[i] = np.median(data[:, i])
        perc_25[i] = np.percentile(data[:, i], 25)
        perc_75[i] = np.percentile(data[:, i], 75)
    return median, perc_25, perc_75


def stars(p):
    '''
    Function to...

    Input
    -----
      p : p-value
    '''
    if p < 0.0001:
        return "****"
    elif (p < 0.001):
        return "***"
    elif (p < 0.01):
        return "**"
    elif (p < 0.05):
        return "*"
    else:
        return "n.s."
        
#Define digit mapping
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

def int_to_roman(n):
    """convert integer to Roman numeral"""
    if not (0 < n < 5000):
        raise OutOfRangeError, "number out of range (must be 1..4999)"
    if int(n) != n:
        raise NotIntegerError, "decimals can not be converted"

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

#Define pattern to detect valid Roman numerals
romanNumeralPattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """ ,re.VERBOSE)

def roman_to_int(s):
    """convert Roman numeral to integer"""
    if not s:
        raise InvalidRomanNumeralError, 'Input can not be blank'
    if not romanNumeralPattern.search(s):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
    
    
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
    
sgd_length = pd.read_csv('~/reference/SGD_2010.lengths', names=['chr_arabic','chrs','chr_length'], index_col=False, sep=' ')
sgd_length = sgd_length[~(sgd_length['chr_arabic'].isin([17,18]))]
sgd_length['chr_start'] = ((pd.rolling_sum((sgd_length['chr_length']), 2) - sgd_length['chr_length']).fillna(0)).cumsum(axis=0)
sgd_length['chr_end'] = (sgd_length['chr_length'] + 1).cumsum(axis=0)
sgd_length = sgd_length.drop('chr_length', axis=1)

def chr_to_gw(df):
    df = df.merge(sgd_length, how='left', on='chr_arabic')
    if 'start' and 'end' in df:
        df['pos_start'] = df.start + df.chr_start
        df['pos_end'] = df.end + df.chr_start
    if 'site' in df:
        df['pos'] = df.site + df.chr_start
        
    df['chr_roman'] = df['chr_arabic'].apply(int_to_roman)
    
    df = df.drop(['chr_start','chr_end','chrs'], axis=1)
    
    return df
