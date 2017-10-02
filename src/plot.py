#!/usr/bin/python
# -*- coding: utf-8 -*-

# Load external dependencies
from setup import *
# Load internal dependencies
import config, utils

def histogram_binned_data(ax, data, bins=50):
    """
    """
    nx, xbins = np.histogram(data, bins=bins, normed=True)

    nx_frac = nx/float(len(nx)) # Each bin divided by total number of objects
    width = xbins[1] - xbins[0] # Width of each bin
    x = np.ravel(zip(xbins[:-1], xbins[:-1]+width))
    y = np.ravel(zip(nx_frac,nx_frac))
    
    return x, y


def boxplot_custom(bp, ax, colors, hatches):
    """
    Custom boxplot style
    """
    for i in range(len(bp['boxes'])):
        box = bp['boxes'][i]
        box.set_linewidth(0)
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
            boxCoords = zip(boxX,boxY)
            boxPolygon = patches.Polygon(
                boxCoords, 
                facecolor = colors[i % len(colors)], 
                linewidth=0, 
                hatch = hatches[i % len(hatches)],
                zorder=4
            )
            ax.add_patch(boxPolygon)

    for i in range(0, len(bp['boxes'])):
        # Boxes
        bp['boxes'][i].set(color=colors[i])
        # Whiskers
        bp['whiskers'][i*2].set(color=colors[i], 
                                linewidth=1.5,
                                linestyle='-',
                                zorder=4)
        bp['whiskers'][i*2 + 1].set(color=colors[i], 
                                linewidth=1.5,
                                linestyle='-',
                                zorder=4)
        # Top and bottom fliers
        bp['fliers'][i].set(markerfacecolor=colors[i],
                            marker='o', alpha=0.75, markersize=3,
                            markeredgecolor='none', zorder=4)
        bp['medians'][i].set(color='black',
                             linewidth=2,
                             zorder=5)
        # 4 caps to remove
        for c in bp['caps']:
            c.set_linewidth(0)

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.tick_params(axis='y', length=0)
    

def heatmap(x, y, z, ax, title, xlabel, ylabel, xticklabels, yticklabels, cmap='RdBu', hatch='', vmin=0.0, vmax=1.0, show=False, speed='slow', zorder=1):
    """
    Inspired by:
    - http://stackoverflow.com/a/16124677/395857 
    - http://stackoverflow.com/a/25074150/395857
    """
    # Plot the heatmap
    if speed=='slow':
        c = ax.pcolor(x, y, z, linewidths=1, cmap=cmap, hatch=hatch, vmin=vmin, vmax=vmax, rasterized=True, zorder=zorder)
    
        # Place the major ticks at the middle of each cell
        ax.set_xticks(np.arange(z.shape[1]) + 0.5, minor=False)
        ax.set_yticks(np.arange(z.shape[0]) + 0.5, minor=False)

        # Set tick labels
        ax.set_xticklabels(xticklabels, minor=False, rotation=90)
        ax.set_yticklabels(yticklabels, minor=False)
    else:
        c = ax.pcolormesh(x, y, z, linewidths=1, cmap=cmap, hatch=hatch, vmin=vmin, vmax=vmax, rasterized=True, zorder=zorder)

    # Set title and x/y labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Remove last blank column
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))

    # Turn off all the ticks
    for t in ax.xaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False
    for t in ax.yaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False

    # Proper orientation (origin at the top left instead of bottom left)
    ax.invert_yaxis()
    
    return c
    
    
def heatmap_spores(S, ax, title, xlabel, ylabel, xticklabels, yticklabels, fold=False, cmap='RdBu', vmin=0.0, vmax=1.0, radius=0.25):
    """
    
    """
    dict_mat = {u'MATa':{'x':[-radius]*len(S.loc[u'MATa']), 'y':np.arange(0.5,len(S.loc[u'MATa']))},
                u'MATα':{'x':np.arange(0.5,len(S.loc[u'MATα'])), 'y':[-radius]*len(S[u'MATα'])}}
    
    for mating in dict_mat.iterkeys():
        data = map(list, zip(*[dict_mat[mating]['x'], dict_mat[mating]['y']]))
        circles = [plt.Circle([x, y], radius) for (x, y) in data]
        # col = patch_collections(circles, edgecolor='black', lw=0.75)

        s = S.ix[mating].values
        
        # col.set(array=s, cmap=cmap)
        # col.set_clim([vmin, vmax])
        # col.set_clip_on(False)
        #
        # ax.add_collection(col)
        
    return dict_mat


def heatmap_hybrids(H, ax, title, xlabel, ylabel, xticklabels, yticklabels, fold=False, cmap='RdBu', vmin=0.0, vmax=1.0, pad=0.25, legend_title=''):
    """
    
    """
    from matplotlib.ticker import FormatStrFormatter
    
    if fold:
        # Get the matrix M and its transpose
        X = H.values
        Y = H.values.T
        # Calculate the element-wise average of the two matrices
        Z = np.add(X, Y) / 2.
        Z = np.tril(Z) # Get the lower triangle of the matrix
        Z = np.ma.masked_array(Z, Z == 0) # Mask the upper triangle
    else:
        Z = H.values
    
    #
    Z = np.ma.array(Z, mask=np.isnan(Z))
    cmap.set_bad('0.1',1.)

    im = ax.pcolor(Z, edgecolors='lightgrey', linewidths=0.5, cmap=cmap, vmin=vmin, vmax=vmax, rasterized=True)
    
    # Place the major ticks at the middle of each cell
    ax.set_xticks(np.arange(Z.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(Z.shape[0]) + 0.5, minor=False)

    # Set tick labels
    ax.set_xticklabels(xticklabels, minor=False, rotation=90)
    ax.set_yticklabels(yticklabels, minor=False)

    # Set title and x/y labels
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
    
    # Set equal aspect ratio
    ax.set_aspect('equal')

    # Add colorbar
    cax = inset_axes(ax, width='4%', height='30%', loc=3,
                     bbox_to_anchor=(1.05, 0., 1, 1),
                     bbox_transform=ax.transAxes,
                     borderpad=0)
    cbar = plt.colorbar(im, cax=cax, ticks=[vmin, 0, vmax], format='%.1f')
    cbar.ax.set_title(legend_title, horizontalalignment='center', fontsize=6)
    cbar.ax.tick_params(labelsize=5)
    cbar.locator = ticker.MaxNLocator(nbins=3)
    cbar.outline.set_visible(False)
	
def gw_frequency(data, ax=None, **kwargs):
    """
    
    """
    # Line plots
    data.plot(
        ax=ax, kind='line',
        legend=False, rasterized=True, zorder=2, **kwargs
    )
    # Draw chromosome shades
    chr_coords = utils.chr_coords()
    for chrom, g in chr_coords.groupby('chr_arabic'):
        ax.axvspan(g.chr_start.squeeze(), g.chr_end.squeeze(),
                   color=('0.95' if chrom % 2 == 1 else 'w'), lw=0, zorder=0, rasterized=True) 
    # Axes limits
    ax.set_ylim(0, 1)
    # Axis tick properties
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
    ax.yaxis.set_minor_locator(ticker.MaxNLocator(nbins=20))
    ax.yaxis.set_ticks_position('left')
    # Axis tick parameters
    ax.tick_params(axis='x', which='major', size=0, labelsize=6)
    ax.tick_params(axis='y', which='major', size=2, labelsize=6)
    ax.tick_params(axis='both', which='minor', size=1, labelsize=4)
    # Grid
    ax.yaxis.grid(lw=0.6, ls='-', color='0.9', which='major', zorder=1)
    # Turn off the x-axis ticks
    for tick in ax.xaxis.get_major_ticks():
        tick.tick1On = False
        tick.tick2On = False

def chr_frequency(data, ax=None, **kwargs):
    """
    
    """
    # Line plots
    data.plot(
        ax=ax, kind='line',
        legend=False, rasterized=True, zorder=2, **kwargs
    )
    # Axes limits
    ax.set_ylim(0, 1)
    # Axis tick properties
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
    ax.yaxis.set_minor_locator(ticker.MaxNLocator(nbins=20))
    ax.yaxis.set_ticks_position('left')
    # Axis tick parameters
    ax.tick_params(axis='x', which='major', size=0, labelsize=6)
    ax.tick_params(axis='y', which='major', size=2, labelsize=6)
    ax.tick_params(axis='both', which='minor', size=1, labelsize=4)
    # Grid
    ax.yaxis.grid(lw=0.6, ls='-', color='0.9', which='major', zorder=1)
    # Turn off the x-axis ticks
    for tick in ax.xaxis.get_major_ticks():
        tick.tick1On = False
        tick.tick2On = False
    
def histogram_frequency(data, ax=None, **kwargs):
    """
    
    """
    # Histogram plots
    for time in data:
        x, y = histogram_binned_data(ax, data[time], bins=50)
        ax.plot(x, y, color=config.time['color'][time], lw=0.5, rasterized=True, zorder=1)
        ax.fill_between(x, 0, y, label=time, facecolor=config.time['color'][time], zorder=1, **kwargs)
    # Axes limits
    ax.set_xlim(0, 1)
    ax.set_ylim(bottom=0)
    # Axis tick properties
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=2))
    ax.xaxis.set_minor_locator(ticker.MaxNLocator(nbins=4))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=3, prune='upper'))
    ax.yaxis.set_ticks_position('right')
    # Axis tick parameters
    ax.tick_params(axis='both', which='major', size=2, labelsize=6)
    ax.tick_params(axis='both', which='minor', size=1, labelsize=4)
    # Grid
    ax.xaxis.grid(lw=0.6, ls='-', color='0.9', which='minor', zorder=0)

def loh_length(data, ax=None, **kwargs):
    """
    
    """
    data.plot(ax=ax, logy=True, style='.', marker='o', ms=3, mec='none', legend=False, **kwargs)

    utils.simple_axes(ax)
    # Axes limits
    ax.set_xlim(0,1.1E3)
    ax.set_ylim(1E-5,1E-0)
    # Axes labels
    ax.set_xlabel('Homozygosity segment length (kb)')
    ax.set_ylabel('Frequency')
    # Legend
    ax.legend(frameon=False, loc='upper right', 
              borderaxespad=0., prop={'size':5},
              handlelength=0.75)

def loh_fluctuation(data, ax=None, **kwargs):
    """
    
    """
    data.plot(ax=ax, kind='bar', edgecolor='k', legend=False,
              error_kw=dict(ecolor='0.1', lw=.75, capsize=.75, capthick=.75), 
              **kwargs)

    utils.simple_axes(ax)
    
    # Set tick labels
    ax.set_xticklabels(data.index.get_level_values('environment'), minor=False, rotation=0)
    
    # Set axes labels
    ax.set_xlabel('Environment')
    ax.set_ylabel(r'Locus-specific LOH rate (gen$^{-1}$)')
    
    # Set log scale
    ax.set_yscale('log')
    
    # Draw legend
    ax.legend(frameon=False, loc='upper right', 
              borderaxespad=0., prop={'size':5},
              handlelength=0.75)
              
def filter_multiindex(data, names=None):
    """
    Filter multiindex by level 'type'
    """
    indexer = [slice(None)]*len(data.index.names)
    indexer[data.index.names.index('type')] = names
    return data.loc[tuple(indexer),:].dropna(axis=1, how='all')
    
### Consensus genotype ###
def consensus_genotype(data, ax=None):
    """
    Plot the consensus genotype across multiple clones
    """
    if len(data) > 0:
        x = data.columns.get_level_values('pos_cum').values
        y = np.arange(len(data.index))
                    
        # Make a color map of fixed colors
        cmap = mpl.colors.ListedColormap([config.background['color']['NA/NA'],
                                          config.background['color']['WA/NA'],
                                          config.background['color']['WA/WA']])
        bounds = [0,1,2]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
            
        heatmap(np.r_[x, x.max()+1], np.r_[y, y.max()+1], data,
                ax, '', '', '', [], [], cmap=cmap, vmin=0, vmax=2)

### SNV/indel mutations ###
def snv_indel_genotype(data, ax=None):
    """
    Plot genotype of SNVs/indels
    """
    if len(data) > 0:
        
        for ii,(k,g) in enumerate(data.groupby(level='clone')):
            g = g.dropna(axis=1)
            x = g.columns.get_level_values('pos_cum').values
            y = [ii+.5]*len(x)
            colors = [config.genotype['color'][int(gt)] for gt in g.values.flatten()]
            ax.scatter(x, y, facecolors=colors, edgecolors='k', s=8, rasterized=False, zorder=3)

### Copy number ###
def copy_number(data, ax=None):
    """
    Plot copy number aberrations
    """
    if len(data.columns) > 0:
        
        print(data)
        
        x = data.columns.get_level_values('pos_cum').values
        y = np.arange(len(data.index.get_level_values('clone')))
                    
        cmap = mpl.colors.ListedColormap(['none','w','none'])
        bounds = [1,2,3]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
            
        for cn, hatch in zip([1, 3], ['xx','--']):
            heatmap(np.r_[x, x.max()+1], np.r_[y, y.max()+1], np.ma.masked_array(data, data!=cn),
                    ax, '', '', '', [], [], cmap=cmap, hatch=hatch, vmin=1, vmax=3, zorder=2)

### LOH ###
def loh_genotype(data, ax=None):
    """
    Plot genotype changes due to LOH
    """
    if len(data) > 0:

        x = data.columns.get_level_values('pos_cum').values
        y = np.arange(len(data.index.get_level_values('clone')))
                
        # Make a color map of fixed colors
        cmap = mpl.colors.ListedColormap(['k','w','k'])
        bounds = [-1,0,1]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
            
        heatmap(np.r_[x, x.max()+1], np.r_[y, y.max()+1], data,
                ax, '', '', '', [], [], cmap=cmap, vmin=-1, vmax=1, zorder=1)

def annotate_genotype(data, ax=None):
    """
    Annotate mutation genotype
    """
    labels = data.columns.get_level_values('gene')
    loc = zip(data.columns.get_level_values('pos_cum'), [-.25]*data.shape[1])
        
    for l, xy in zip(labels, loc):
        trans = ax.get_xaxis_transform() # x in data units, y in axes fraction
        ax.annotate(l, xy=xy, xytext=(0, 4), textcoords='offset points',
                    arrowprops=dict(arrowstyle='wedge,tail_width=0.7', color='black'),
                    fontsize=5, style=('italic' if l!='non-coding' else 'normal'),
                    weight=('bold' if l in ['RNR2','RNR4','FPR1','TOR1'] else 'normal'),
                    annotation_clip=False, va='bottom', ha='center')

def genome_instability(data, ax=None, title=None):
    """
    
    """
    idx = 0
    
    # Plot tracks
    for ii, (s, group) in enumerate(data.groupby(level='set')):
        
        # Consensus genotypes
        consensus_data = filter_multiindex(group, names=['consensus'])
        nrows = consensus_data.index.get_level_values('clone').nunique()
        
        ax1 = plt.subplot(ax[idx:idx+nrows])
        consensus_genotype(consensus_data, ax1)
        
        if ax1.is_first_row():
            # Set axis label
            labels = ['Consensus']
            ax1.set_yticks(np.arange(len(labels)) + 0.5, minor=True)
            ax1.set_yticklabels(labels, fontweight='bold', va='center', minor=True)
            ax1.set_title(title, fontsize=6, y=2, weight='bold')
            # Annotate variants
            annotation = filter_multiindex(data, names=['snv_indel'])
            annotate_genotype(annotation, ax1)
        
        idx += nrows
        
        # De novo genotypes
        de_novo_data = filter_multiindex(group, names=['snv_indel','copy_number','loh'])
        labels = de_novo_data.index.get_level_values('clone').unique()
        nrows = len(labels)
        
        ax2 = plt.subplot(ax[idx:idx+nrows], sharex=ax1)
        # SNV/indel
        snv_indel_data = filter_multiindex(group, names=['snv_indel'])
        snv_indel_genotype(snv_indel_data, ax2)
        # Copy number
        copy_number_data = filter_multiindex(group, names=['copy_number'])
        copy_number(copy_number_data, ax2)
        # LOH
        loh_data = filter_multiindex(group, names=['loh'])
        loh_genotype(loh_data, ax2)

        # Annotate clonal lineages
        ax2.set_yticks(np.arange(len(labels)) + 0.5)
        ax2.set_yticklabels('C' + labels, fontweight='bold', va='center')
        [ax2.axhline(g, lw=0.5, ls="-", color="lightgray") for g in np.arange(len(labels))]
        lineage = group.index.get_level_values('lineage').unique()[0]
        ax2.tick_params(axis='y', colors=config.lineages[lineage]['fill'], width=5, which='both')
        
        # Show chromosome boundaries
        chrom_boundaries(ax2)
        
        idx += nrows

    # Set axis label
    ax2.set_xlabel('Chromosome')
    

def scatter_plot(x, y, ax=None, **kwargs):
    """
    
    """
    ax.plot(x, y, linestyle='', rasterized=False, **kwargs)#, label=config.population['long_label'][t])
    
    from matplotlib.ticker import MaxNLocator
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=5, prune='upper'))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=5, prune='upper'))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

def histogram_x(X, ax=None, time=None):
    """
    
    """
    import gmm
                
    # Fit the Gaussian mixture model
    N = np.arange(1, 4)
    models = gmm.gmm_fit(X, N)

    # Compute the AIC and the BIC
    AIC = [m.aic(X) for m in models]
    BIC = [m.bic(X) for m in models]
    M_best = models[np.argmin(BIC)]
    
    # Plot data
    bins = 34
    xbins, y = histogram_binned_data(ax, X, bins=bins)
                        
    ax.fill_between(xbins, 0, y, label=config.population['long_label'][time], 
                    alpha=0.5, facecolor=config.population['color'][time])
            
    xbins = np.linspace(ax.get_xlim()[0], ax.get_xlim()[1], 1000)
    logprob = M_best.score_samples(np.array([xbins]).T)
    pdf = np.exp(logprob)
            
    ax.plot(xbins, pdf / bins, '-', 
            color=config.population['color'][time], lw=1)

    # Mean of the distribution
    for p in abs(M_best.means_.ravel()):
        ax.axvline(x=p, ls='--', lw=1.5, color=config.population['color'][time], zorder=1)
        pos = ax.get_ylim()[0] * 0.75 + ax.get_ylim()[1] * 0.25
        trans = ax.get_xaxis_transform() # x in data units, y in axes fraction
        ax.annotate(np.around(p, 2),
                    xy=(p, 0.85), xycoords=trans, fontsize=6,
                    color='k', va='center',
                    ha=('right' if time=='ancestral' else 'left'),
                    xytext=((-5 if time=='ancestral' else 5),0), textcoords='offset points',
                    path_effects=[path_effects.withStroke(linewidth=0.5, foreground="w")])

    ax.set_xticks([])
    ax.set_xticklabels([])
    
    ax.set_yticks(ax.get_yticks()[1:])
    
    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=2))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

def histogram_y(Y, ax=None, time=None):
    """
    
    """
    import gmm
                
    # Fit the Gaussian mixture model
    N = np.arange(1, 4)
    models = gmm.gmm_fit(Y, N)

    # Compute the AIC and the BIC
    AIC = [m.aic(Y) for m in models]
    BIC = [m.bic(Y) for m in models]
    M_best = models[np.argmin(BIC)]
            
    # Plot data
    bins = 34
    ybins, x = histogram_binned_data(ax, Y, bins=bins)
    
    ax.fill_betweenx(ybins, 0, x, label=config.population['long_label'][time], 
                     alpha=0.5, facecolor=config.population['color'][time])
            
    ybins = np.linspace(ax.get_ylim()[0], ax.get_ylim()[1], 1000)
    logprob = M_best.score_samples(np.array([ybins]).T)
    pdf = np.exp(logprob)
            
    ax.plot(pdf / bins, ybins, '-', 
            color=config.population['color'][time], lw=1)

    # Mean of the distribution
    for p in abs(M_best.means_.ravel()):
        ax.axhline(y=p, ls='--', lw=1.5, color=config.population['color'][time], zorder=1)
        pos = ax.get_xlim()[0] * 0.75 + ax.get_xlim()[1] * 0.25
        trans = ax.get_yaxis_transform() # x in data units, y in axes fraction
        ax.annotate(np.around(p, 2),
                    xy=(0.85, p), xycoords=trans, fontsize=6,
                    color='k', ha='center',
                    va=('bottom' if time=='ancestral' else 'top'),
                    xytext=(0,(-10 if time=='ancestral' else 10)), textcoords='offset points',
                    path_effects=[path_effects.withStroke(linewidth=0.5, foreground="w")])

    ax.set_yticks([])
    ax.set_yticklabels([])
    
    ax.set_xticks(ax.get_xticks()[1:])
    
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=2))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
def lollipops(data, ax=None):
    """
    
    """
    data = data.agg([np.mean, np.median, np.std, 'count'])
    
    if len(data)>0:
        x_data = np.array(data)
        y_data = np.repeat([0.2*(ax.get_ylim()[1]-ax.get_ylim()[0])], len(x_data))
        arr = zip(x_data, y_data)
        
        markerline, stemlines, baseline = ax.stem(x_data, y_data)
                
        plt.setp(markerline, 'color', config.population['color'][time], 
                 markersize = 2.75, markeredgewidth=.75, markeredgecolor='k', zorder=3)
        plt.setp(stemlines, linewidth=.75, color=config.population['color'][time],
                 path_effects=[path_effects.withStroke(linewidth=1.25, foreground='k')], zorder=2)  
        plt.setp(baseline, 'color', 'none', zorder=1)
                    
#         for idx, label in data.iterrows():
#             ax.annotate(label.name[1],
#                         xy = (label, 0.2), xycoords=('data','axes fraction'), 
#                         xytext = (0, 8), textcoords = 'offset points', 
#                         ha = 'center', va = 'top',
#                         fontsize = 6, style = 'italic',
#                         path_effects=[path_effects.withStroke(linewidth=0.5, foreground="w")])

import seaborn as sns

def scatter_rank_correlation(data, ax=None, environment=None):
    """
    Scatter plot - Rank correlation
    """
    if ax is None:
        ax = plt.gca()
    # Define colour palettes
    colors = [config.population['color'].get(e, 'k') for e in data.columns]
    # # Scatter plot
    # sns.stripplot(ax=ax, data=data[data['environment']=='YNB'],
    #               x="population", y="value", hue="group", marker='o', size=7,#marker='marker',
    #               palette=colors, clip_on=False)
    #
    # sns.stripplot(ax=ax, data=data[data['environment']==environment],
    #               x="population", y="value", hue="group", marker='^', size=7,
    #               palette=colors, clip_on=False)

    # # Remove default legend
    # ax.legend_.remove()
    # Mean expectation
    ax.axvline(x=0.0, c='lightgray', ls='--', lw=2)
    # Axes limits
    ax.set_xlim((-1,1))
    
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=5))
    
    ax.tick_params(axis='x-axis', which='major', size=2, labelsize=6)
    ax.tick_params(axis='y-axis', which='major', size=0, labelsize=7)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)


def chrom_boundaries(ax=None):
    """
    Show chromosome boundaries
    """
    # Set labels
    chr_coords = utils.chr_coords()
    ticks = chr_coords.chr_start + (chr_coords.chr_end - chr_coords.chr_start)/2.
    labels = chr_coords.chr_roman
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels)
    # Show grid
    start = chr_coords.chr_start
    grid=[x+1. for x in list(set(start))]
    [ax.axvline(g, lw=0.5, ls="-", color="gray") for g in grid]

def set_custom_labels(index, pos):
    """
    Custom labels for nested axes.
    index : 
    pos : 
    """
    start = dict((m[pos], ii) for ii,m in enumerate(index.values))
    end = dict((m[pos], len(index)-ii-1) for ii,m in enumerate(index[::-1].values))
    labels = dict((key, (start[key] + end.get(key, 0))/2.) for key in end.keys())
    
    return start, end, labels

def connect_bbox(bbox1, bbox2,
                 loc1a, loc2a, loc1b, loc2b,
                 prop_lines, prop_connector=None, prop_patches=None):
    """
    
    """
    from mpl_toolkits.axes_grid1.inset_locator import BboxPatch, BboxConnector, BboxConnectorPatch
    
    if prop_connector is None:
        prop_connector = prop_lines.copy()
        prop_connector["alpha"] = prop_connector.get("alpha", 1)*0.2
        
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
                           loc1a=loc1a, loc2a=loc2a, loc1b=loc1b, loc2b=loc2b,
                           **prop_connector)
    p.set_fill(True)       
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
    from matplotlib.transforms import Bbox, TransformedBbox, blended_transform_factory

    trans1 = blended_transform_factory(ax1.transData, ax1.transAxes)
    trans2 = blended_transform_factory(ax2.transData, ax2.transAxes)

    bbox = Bbox.from_extents(xmin, 0, xmax, 1)

    mybbox1 = TransformedBbox(bbox, trans1)
    mybbox2 = TransformedBbox(bbox, trans2)
    
    prop_connector = kwargs.copy()
    prop_connector["edgecolor"] = "none"
    prop_connector["facecolor"] = "gray"
    prop_connector["alpha"] = 0.4
    
    prop_patches = kwargs.copy()
    prop_patches["edgecolor"] = "none"
    prop_patches["facecolor"] = "gray"
    prop_patches["alpha"] = 0.4
    
    c1, c2, bbox_patch1, bbox_patch2, p = \
    connect_bbox(mybbox1, mybbox2,
    loc1a=3, loc2a=2, loc1b=4, loc2b=1,
    prop_lines=kwargs, prop_connector=prop_connector, prop_patches=prop_patches)

    ax1.add_patch(bbox_patch1)
    # ax2.add_patch(bbox_patch2)
    ax2.add_patch(c1)
    ax2.add_patch(c2)
    ax2.add_patch(p)

    return c1, c2, bbox_patch1, bbox_patch2, p

def get_text_positions(x_data, y_data, txt_width, txt_height):
    """
    
    """
    a = zip(y_data, x_data)
    text_positions = y_data.copy()
    for index, (y, x) in enumerate(a):
        local_text_positions = [i for i in a if i[0] > (y - txt_height) 
                            and (abs(i[1] - x) < txt_width * 2) and i != (y,x)]
        if local_text_positions:
            sorted_ltp = sorted(local_text_positions)
            if abs(sorted_ltp[0][0] - y) < txt_height: #True == collision
                differ = np.diff(sorted_ltp, axis=0)
                a[index] = (sorted_ltp[-1][0] + txt_height, a[index][1])
                text_positions[index] = sorted_ltp[-1][0] + txt_height
                for k, (j, m) in enumerate(differ):
                    #j is the vertical distance between words
                    if j > txt_height * 2: #if True then room to fit a word in
                        a[index] = (sorted_ltp[k][0] + txt_height, a[index][1])
                        text_positions[index] = sorted_ltp[k][0] + txt_height
                        break
    return text_positions

def text_plotter(x_data, y_data, text_positions, axis,txt_width,txt_height):
    """
    
    """
    for x,y,t in zip(x_data, y_data, text_positions):
        axis.text(x - txt_width, 1.01*t, '%d'%int(y),rotation=0, color='blue')
        if y != t:
            axis.arrow(x, t,0,y-t, color='red',alpha=0.3, width=txt_width*0.1, 
                       head_width=txt_width, head_length=txt_height*0.5, 
                       zorder=0,length_includes_head=True)

def annotate_custom(ax, s, xy_arr=[], *args, **kwargs):
    """
    
    """
    ans = []
    an = ax.annotate(s, xy_arr[0], *args, **kwargs)
    ans.append(an)
    d = {}
    try:
        d['xycoords'] = kwargs['xycoords']
    except KeyError:
        pass
    try:
        d['arrowprops'] = kwargs['arrowprops']
    except KeyError:
        pass
    for xy in xy_arr[1:]:
        an = ax.annotate(s, xy, alpha=0.0, xytext=(0,0), textcoords=an, **d)
        ans.append(an)
    return ans

def colorbar_index(ncolors, cmap):
    """
    
    """
    cmap = colormap_discretize(cmap, ncolors)
    mappable = plt.cm.ScalarMappable(cmap=cmap)
    mappable.set_array([])
    mappable.set_clim(-0.5, ncolors+0.5)
    return mappable
    
def colormap_discretize(cmap, N):
    """
    Return a discrete colormap from the continuous colormap cmap.
        cmap: colormap instance, eg. cm.jet. 
        N: number of colors.
    Example
        x = resize(arange(100), (5,100))
        djet = cmap_discretize(cm.jet, 5)
        imshow(x, cmap=djet)
    """
    import matplotlib.colors as mcolors

    if type(cmap) == str:
        cmap = plt.get_cmap(cmap)
    colors_i = np.concatenate((np.linspace(0, 1., N), (0.,0.,0.,0.)))
    colors_rgba = cmap(colors_i)
    indices = np.linspace(0, 1., N+1)
    cdict = {}
    for ki,key in enumerate(('red','green','blue')):
        cdict[key] = [ (indices[i], colors_rgba[i-1,ki], colors_rgba[i,ki])
                       for i in xrange(N+1) ]
    # Return colormap object
    return mcolors.LinearSegmentedColormap(cmap.name + "_%d"%N, cdict, 1024)

def save_figure(filename, formats=['pdf','png','svg'], **kwargs):
    """
    Save matplotlib figure in multiple formats (pdf, png, svg).
        formats: list of formats.
        kwargs: arguments to plt.savefig (e.g. dpi).
    """
    if 'pdf' in formats:
        plt.savefig(filename+'.pdf', bbox_inches='tight', **kwargs)
    if 'png' in formats:
        plt.savefig(filename+'.png', bbox_inches='tight', **kwargs)
    if 'svg' in formats:
        plt.savefig(filename+'.svg', bbox_inches='tight', **kwargs)
