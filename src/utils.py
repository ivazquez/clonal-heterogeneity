#!/usr/bin/python
# -*- coding: utf-8 -*-

# Load external dependencies
from setup import *
# Load internal dependencies
import config, utils

def load_data(fn):
    """
	Load the data for the plots
    
    Input
    -----
      fn : filename 
    """
    import cPickle as pickle
    with open(fn, 'rb') as f:
        return pickle.load(f)


def save_data(data, fn):
    """
	Store data to file for the plots
    
    Input
    -----
      data : pandas dataframe
      fn : filename 
    """
    import cPickle as pickle
    with open(fn, 'wb') as f:
        pickle.dump(data, f, protocol=-1)


def merge_two_dicts(x, y):
    """
	Given two dicts, merge them into a new dict as a shallow copy.
    """
    z = x.copy()
    z.update(y)
    return z
	
	
def combine_columns(df, c1, c2, mirror=True):
    from itertools import combinations
	
    df.sort_values([c1,c2], inplace=True)
    comb = list(combinations(df[c1].unique(),2))
    
    genotype=[]
    for index, row in df.iterrows():
        if mirror:
            if (row[c1], row[c2]) in comb:
                g = (row[c1],row[c2])
            else:
                g = (row[c2],row[c1])
        else:
            g = (row[c1],row[c2])
        genotype.append(g)
            
    return genotype

    
def simple_axes(ax):
    """
	Show left and bottom axes in a plot

    Input
    -----
      ax : matplotlib axis
    """
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()


def shift_colormap(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    """
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
    """
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

    newcmap = mpl.colors.LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap=newcmap)

    return newcmap


def discrete_colormap(N, base_cmap=None):
    """
	Create an N-bin discrete colormap from the specified input map
    
    Input
    -----
      N : number of bins
      cmap : The matplotlib colormap to be altered
    """

    # Note that if base_cmap is a string or None, you can simply do
    #    return plt.cm.get_cmap(base_cmap, N)
    # The following works for string, None, or a colormap instance:

    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)


def percentile(data):
    """
	Calculate the median and top/bottom percentiles
    
    Input
    -----
      data : pandas series or dataframe
    """
    median = np.zeros(data.shape[1])
    perc_25 = np.zeros(data.shape[1])
    perc_75 = np.zeros(data.shape[1])
    for i in range(0, len(median)):
        median[i] = np.median(data[:, i])
        perc_25[i] = np.percentile(data[:, i], 25)
        perc_75[i] = np.percentile(data[:, i], 75)
    return median, perc_25, perc_75


def stars(p):
    """
	Convert p-values to star notation

    Input
    -----
      p : p-value
    """
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
roman_numeral = (('M',  1000),
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
    """
	Convert integer to roman numeral
	"""
    if not (0 < n < 5000):
        raise(OutOfRangeError, "number out of range (must be 1..4999)")
    if int(n) != n:
        raise(NotIntegerError, "decimals can not be converted")

    result = ""
    for numeral, integer in roman_numeral:
        while n >= integer:
            result += numeral
            n -= integer
    return result

# Define pattern to detect valid Roman numerals
roman_numeral_pattern = re.compile("""
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
    """
	Convert roman numeral to integer
	"""
    if not s:
        raise(InvalidRomanNumeralError, 'Input can not be blank')
    if not roman_numeral_pattern.search(s):
        raise(InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s)

    result = 0
    index = 0
    for numeral, integer in roman_numeral:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result

def hex_to_rgb(value):
    """
	Convert hex code to rgb
	"""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    """
    Convert rgb to hex code
	"""
    return '#%02x%02x%02x' % rgb

def chr_coords():
	# Load config file with chromosome lengths
    df = pd.DataFrame(config.chrom_len.items(), columns=['chr_arabic', 'chr_length'])
    df = df[~(df['chr_arabic'].isin([17,18]))]
    df['chr_roman'] = df['chr_arabic'].apply(utils.int_to_roman)
	# Calculate start/end coordinates
    df['chr_start'] = ((df['chr_length'].rolling(window=2,center=False).sum() - df['chr_length']).fillna(0)).cumsum(axis=0).astype(int)
    df['chr_end'] = (df['chr_length']).cumsum(axis=0)
    return df

def chr_to_gw(df, chr_coords):
    df = df.merge(chr_coords, how='left', on='chr_arabic')
    if 'start' and 'end' in df:
        df['pos_start'] = df.start + df.chr_start
        df['pos_end'] = df.end + df.chr_start
    if 'pos' in df:
        df['pos_cum'] = df.pos + df.chr_start
        
    df['chr_roman'] = df['chr_arabic'].apply(int_to_roman)
    
    df = df.drop(['chr_start','chr_end'], axis=1)
    
    return df
	
def est_cum_pos(position, aggregation='chrom', column='pos', offset=0, chrom_len=None):
    """
	Compute the cumulative position of each variant given the position and the chromosome
    Also return the starting cumulativeposition of each chromosome

    Input
    -----
      position:   pandas DataFrame of basepair positions (key='pos') and chromosome values (key='chrom')
                  The DataFrame will be updated with field 'pos_cum'
      chrom_len:  vector with predefined chromosome length
      offset:     offset between chromosomes for cumulative position (default 0 bp)
    
    Output
    -----
      chrom_pos:  numpy.array of starting cumulative positions for each chromosome
      position:   augmented position object where cumulative positions are defined
    """
    RV = position.copy()
    chromvals =  sp.unique(position[aggregation]) # sp.unique is always sorted
    chrom_pos_cum= sp.zeros_like(chromvals) # get the starting position of each Chrom
    pos_cum= sp.zeros_like(position.shape[0])
    if not column+'_cum' in position:
        RV[column+'_cum']= sp.zeros_like(position[column]) # get the cum_pos of each variant.
    pos_cum=RV[column+'_cum'].values
    maxpos_cum=0
    for i,mychrom in enumerate(chromvals):
        chrom_pos_cum[i] = maxpos_cum
        i_chr=position[aggregation]==mychrom
        if chrom_len is None:
            maxpos = position[column][i_chr].max()+offset
        else:
            maxpos = chrom_len[mychrom]+offset
        pos_cum[i_chr.values]=maxpos_cum+position.loc[i_chr,column]
        maxpos_cum+=maxpos      
    
    return RV, chrom_pos_cum