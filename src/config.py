 #!/usr/bin/python
 # -*- coding: utf-8 -*-
 
import colors
import numpy as np
import matplotlib.patheffects as PathEffects

# population attributes
sp_bg = {
    'position': {
        'HU': 
        {'parents': 0, 'ancestral': 1, 'evolved': 2},
        'RM':
        {'parents': 0, 'ancestral': 1, 'evolved': 2}
    }
}

# background attributes
sp_cl = {
    'position': {
        'HU': 
        {'WA': 0, 'NA': 1, 'WAxNA': 2},
        'RM':
        {'WA': 0, 'NA': 1, 'WAxNA': 2},
    },
    'color': {
        'HU':
        {'WA': colors.fte_colors[0], 'NA': colors.fte_colors[1], 'WAxNA': colors.fte_colors[2]},
        'RM':
        {'WA': colors.fte_colors[0], 'NA': colors.fte_colors[1], 'WAxNA': colors.fte_colors[2]},
    }
}

# gene attributes
sp_gn = {
    'position': {
        'HU': 
        {'RNR2': 0, 'RNR4': 1},
        'RM':
        {'no driver': 0, 'FPR1': 1, 'TOR1': 2},
    }
}

# genotype attributes
sp_gt_long = {
    'position': {
        'HU': 
        {'': 0, 'RNR2': 1, 'RNR2*': 2, 'RNR4': 3, 'RNR4*': 4},
        'RM': 
        {'': 0, 'no driver': 1, 'FPR1*': 2, 'TOR1': 3, 'TOR1*': 4}
    },
    'color': {
        'HU': 
        { '': colors.fte_colors[0], 'RNR2': colors.fte_colors[1], 'RNR2*': colors.fte_colors[2], 'RNR4': colors.fte_colors[1], 'RNR4*': colors.fte_colors[2]},
        'RM': 
        {'': colors.fte_colors[0], 'no driver': colors.fte_colors[1], 'FPR1*': colors.fte_colors[2], 'TOR1': colors.fte_colors[1], 'TOR1*': colors.fte_colors[2]}
    }
}

# genotype attributes
sp_gt_short = {
'position':
 {'HU': 
  {'+': 0, '-': 1},
  'RM': 
  {'+': 0, '-': 1}
  },
'color':
  {'HU': 
  {'+': colors.fte_colors_dark[5], '-': colors.fte_colors_light[5]},
  'RM': 
  {'+': colors.fte_colors_dark[5], '-': colors.fte_colors_light[5]}
  }
}

# collection attributes
hy_bg = {
'position':
{'HU': 
 {('parents','parents'): 0, ('ancestral','ancestral'): 1, 
  ('ancestral','evolved'): 2, ('evolved','evolved'): 3},
'RM':
 {('parents','parents'): 0, ('ancestral','ancestral'): 1, 
  ('ancestral','evolved'): 2, ('evolved','evolved'): 3}
 }
}

# background attributes
hy_cl = {
'position':
{'HU': 
 {('WA','WA'): 0, ('NA','NA'): 1, ('WAxNA','WAxNA'): 2},
'RM':
 {('WA','WA'): 0, ('NA','NA'): 1, ('WAxNA','WAxNA'): 2},
 },
'color':
{'HU':
 {('WA','WA'): colors.fte_colors[0], ('NA','NA'): colors.fte_colors[1], ('WAxNA','WAxNA'): colors.fte_colors[2]},
'RM':
 {('WA','WA'): colors.fte_colors[0], ('NA','NA'): colors.fte_colors[1], ('WAxNA','WAxNA'): colors.fte_colors[2]},
}
}

# gene attributes
hy_gn = {
'position':
{'HU': 
 {('','RNR2'): 0, ('','RNR4'): 1,
  ('RNR2','RNR2'): 0, ('RNR4','RNR4'): 1, ('RNR2','RNR4'): 2},
'RM':
 {('','no driver'): 0, ('','FPR1'): 1, ('','TOR1'): 2,
  ('no driver','no driver'): 0, ('FPR1','FPR1'): 1, ('TOR1','TOR1'): 2, 
  ('FPR1','TOR1'): 3, ('FPR1','no driver'): 4, ('TOR1','no driver'): 5},
 }
}

# genotype attributes
hy_gt_long = {
'position':
{'HU': 
 {('',''): 0,
  ('','RNR2'): 1, ('','RNR2*'): 2, ('','RNR4'): 3, ('','RNR4*'): 4,
  ('RNR2','RNR2'): 5, ('RNR2','RNR2*'): 6, ('RNR2*','RNR2*'): 7, 
  ('RNR4','RNR4'): 8, ('RNR4','RNR4*'): 9, ('RNR4*','RNR4*'): 10, 
  ('RNR2','RNR4'): 11, ('RNR2*','RNR4'): 12, ('RNR2','RNR4*'): 13, ('RNR2*','RNR4*'): 14},
'RM':
 {('',''): 0,
  ('','FPR1'): 1, ('','FPR1*'): 2, ('','TOR1'): 3, ('','TOR1*'): 4,
  ('no driver','no driver'): 5, ('FPR1','FPR1'): 6, ('FPR1*','FPR1*'): 7,
  ('TOR1','TOR1'): 8, ('TOR1','TOR1*'): 9, ('TOR1*','TOR1*'): 10,
  ('FPR1','TOR1'): 11, ('FPR1*','TOR1'): 12, ('FPR1','TOR1*'): 13, ('FPR1*','TOR1*'): 14},
 },
'color':
{'HU':
 {('',''): colors.fte_colors[0],
  ('','RNR2'): colors.fte_colors[1], ('','RNR2*'): colors.fte_colors[2], ('','RNR4'): colors.fte_colors[1], ('','RNR4*'): colors.fte_colors[2],
  ('RNR2','RNR2'): colors.fte_colors[1], ('RNR2','RNR2*'): colors.fte_colors[2], ('RNR2*','RNR2*'): colors.fte_colors[3],
  ('RNR4','RNR4'): colors.fte_colors[1], ('RNR4','RNR4*'): colors.fte_colors[2], ('RNR4*','RNR4*'): colors.fte_colors[3],
  ('RNR2','RNR4'): colors.fte_colors[1], ('RNR2*','RNR4'): colors.fte_colors[2], ('RNR2','RNR4*'): colors.fte_colors[2], ('RNR2*','RNR4*'): colors.fte_colors[3]},
'RM':
 {('',''): colors.fte_colors[0],
  ('','FPR1'): colors.fte_colors[1], ('','FPR1*'): colors.fte_colors[2], ('','TOR1'): colors.fte_colors[1], ('','TOR1*'): colors.fte_colors[2],
  ('no driver','no driver'): colors.fte_colors[1], ('FPR1','FPR1'): colors.fte_colors[1], ('FPR1*','FPR1*'): colors.fte_colors[3],
  ('TOR1','TOR1'): colors.fte_colors[1], ('TOR1','TOR1*'): colors.fte_colors[2], ('TOR1*','TOR1*'): colors.fte_colors[3],
  ('FPR1','TOR1'): colors.fte_colors[1], ('FPR1*','TOR1'): colors.fte_colors[2], ('FPR1','TOR1*'): colors.fte_colors[2], ('FPR1*','TOR1*'): colors.fte_colors[3]},
}
}

# genotype attributes
hy_gt_short = {
'position':
{'HU': 
{('+','+'): 0, ('+','-'): 1, ('-','+'): 2, ('-','-'): 3},
'RM':
{('+','+'): 0, ('+','-'): 1, ('-','+'): 2, ('-','-'): 3}, 
},
'color':
{'HU':
{('+','+'): colors.fte_colors_dark[5], ('+','-'): colors.fte_colors[5], ('-','+'): colors.fte_colors[5], ('-','-'): colors.fte_colors_light[5]},
'RM':
{('+','+'): colors.fte_colors_dark[5], ('+','-'): colors.fte_colors[5], ('-','+'): colors.fte_colors[5], ('-','-'): colors.fte_colors_light[5]},
}
}

# factor attributes
factors = {
    'color': {
        'time': colors.fte_colors[2],
        'background\n(genotype)': colors.fte_colors[0],
        'de novo\n(gene identity)': colors.fte_colors_dark[1], 
        'de novo\n(genotype)': colors.fte_colors[1],
        'auxotrophy': colors.fte_colors[5],
        'measurement\nerror': colors.fte_colors[3],
        'tetrad': colors.fte_colors[4],
        'spore': colors.fte_colors[4]
        },
    'hatch': {
        'spores': " ", 
        'hybrids': "/"
        },
    'position': {
        'time': 0, 
        'de novo\n(gene identity)': 1, 
        'de novo\n(genotype)': 2,
        'auxotrophy': 3,
        'background\n(genotype)': 4,
        'tetrad': 4,
        'spore': 5     
    }
}

# gene attributes
gene = {
    'position':{
        'RNR2':0, 'RNR4':1, 'no driver':0, 'FPR1':1, 'TOR1':2   
    }
}

# genotype attributes
genotype = {
    'position':{
        '+':0,
        '-':1
    },
    'color':{
        0:'w',
        1:'lightgray',
        2:'k'
    }
}

# population attributes
population = {
    'position':{
        'parents': 0, 'ancestral': 1, 'evolved': 2
    },
    'facecolor':{
        'parents': colors.fte_colors[0], 
        'ancestral': colors.fte_colors[0],
        'evolved': colors.fte_colors[1]
    },
    'color':{
        'parents': colors.fte_colors[0], 
        'ancestral': colors.fte_colors[0],
        'evolved': colors.fte_colors[1]   
    },
    'long_label':{
        'parents': 'parents', 
        'ancestral': r'ancestral ($t=0$)',
        'evolved': r'evolved ($t=32$)'  
    },
    'short_label':{
        'parents': 'par.', 
        'ancestral': 'anc.',
        'evolved': 'evolved'  
    },
    'alpha':{
        'parents': 0.5, 
        'ancestral': 0.5,
        'evolved': 0.5  
    },
    'pad':{
        'parents': 0.11, 
        'ancestral': 0.11, 
        'evolved':0.11
    }
}

# background attributes
background = {
    'position':{
        'WA':0, 
        'NA':1,
        'WAxNA':2,
        'WA/WA':3, 
        'NA/NA':4,
        'WA/NA':5
    },
    'color':{
        'WA':colors.bg_colors[0],
        'NA':colors.bg_colors[1],
        'WAxNA':colors.bg_colors[2],
        'WA/WA':colors.bg_colors[0],
        'NA/NA':colors.bg_colors[1],
        'WA/NA':colors.bg_colors[2]
    },
    'marker':{
        'WA':'o', 
        'NA':'o', 
        'WA/WA':'D', 
        'NA/NA':'D', 
        'WA/NA':'D'
    }
}

labels = {
    'gene':'de_novo_gene',
    'genotype_short':'de_novo_genotype'
}

# selection attributes
selection = {
    'color': {
        'HU':colors.fte_colors_light[5],
        'RM':colors.fte_colors[5],
        'YPD':colors.fte_colors_dark[5]
        # 'HU':colors.mr_colors[2],
        # 'RM':colors.mr_colors[1],
        # 'YPD':'k'
    },
    'linewidth': {
        'HU':0.75,'RM':0.75,'YPD':0.75
    },
    'style': {
        'HU':'-','RM':'-','YPD':'-' 
    },
    'long_label': {
        u'HU': u'Hydroxyurea (YPD+HU 10 mg/ml)', 
        u'RM': u'Rapamycin (YPD+RM 0.025 μg/ml)',
        u'YPD': u'Control (YNB)',
        'COM':'Control', 
        'null': u'Control'
    },
    'short_label': {
        'HU':'Hydroxyurea',
        'RM':'Rapamycin',
        'YPD':'Control',
        'COM':'Control', 
        'null': u'Control'
    }
}

# environment attributes
environment = {
    'color': {
        'HU':colors.mr_colors[2],
        'RM':colors.mr_colors[1],
        'YNB':'k'
    },
    'linewidth': {
        'HU':0.75,'RM':0.75,'YNB':0.75
    },
    'style': {
        'HU':'-','RM':'-','YNB':'-' 
    },
    'long_label': {
        u'HU': u'Hydroxyurea (YNB+HU 10 mg/ml)', 
        u'RM': u'Rapamycin (YNB+RM 0.025 μg/ml)',
        u'YNB': u'Control (YNB)',
        'COM':'Control', 
        'null': u'Control'
    },
    'short_label': {
        'HU':'Hydroxyurea',
        'RM':'Rapamycin',
        'YNB':'Control',
        'COM':'Control', 
        'null': u'Control'
    }
}

# lineage attributes
lineages = {
    'subclone A': {'fill':colors.fte_colors[0], 'line':colors.fte_colors[0]},
    'subclone B': {'fill':colors.fte_colors[1], 'line':colors.fte_colors[1]},
    'subclone C': {'fill':colors.fte_colors[2], 'line':colors.fte_colors[2]},
    'subclone D': {'fill':colors.fte_colors[3], 'line':colors.fte_colors[3]},
    'bulk': {'fill':colors.fte_colors[4], 'line':colors.fte_colors[4]},
    '': {'fill':colors.fte_colors[4], 'line':colors.fte_colors[4]},
}

# mutation type attributes
mutation_type = {
    'driver' : {
        'linestyle':'-',
        'linewidth':1.5,
        'path_effects':[PathEffects.withStroke(linewidth=2, foreground="k")],
        'zorder':2
    },
    'passenger': {
        'linestyle':'--',
        'dashes':(3,2),
        'linewidth':1.5,
        'path_effects':[PathEffects.withStroke(linewidth=2, foreground="k")],
        'zorder':1,
    }
}

# mutation consequence attributes
consequence_short = {
    'non-synonymous' : {
        'marker':'o',
        'markersize':2,
        'markeredgecolor':'none',
        'zorder':2
    },
    'synonymous': {
        'marker':'s',
        'markersize':1.5,
        'markeredgecolor':'none',
        'zorder':1
    }
}

# time attributes
time = {
    'color': {
        0:colors.t_colors[0],
        2:colors.t_colors[1],
        4:colors.t_colors[2],
        8:colors.t_colors[3],
        16:colors.t_colors[4],
        32:colors.t_colors[5]
    },
    'linewidth': {
        0:0.75,2:0.75,4:0.75,8:0.75,16:0.75,32:0.75
    },
    'style': {
        0:'-',2:'-',4:'-',8:'-',16:'-',32:'-'  
    }
}

# background attributes for genetic constructs
construct_background = {
    'color': {
        'wt': {'WA':colors.bg_colors_wt[0], 'NA':colors.bg_colors_wt[1], 'WA/WA':colors.bg_colors_wt[0], 'NA/NA':colors.bg_colors_wt[1], 'WA/NA':colors.bg_colors_wt[2]},
        'mut': {'WA':colors.bg_colors_mut[0], 'NA':colors.bg_colors_mut[1], 'WA/WA':colors.bg_colors_mut[0], 'NA/NA':colors.bg_colors_mut[1], 'WA/NA':colors.bg_colors_mut[2]}
    },
    'position': {
        'WA':0, 'NA':1, 'WA/WA':2, 'NA/NA':3, 'WA/NA':4
    }
}

# genotype attributes for genetic constructs
construct_genotype = {
'HU': {u'RNR2':{u'WT':0, u'rnr2Δ':1, u'rnr2Δ/RNR2':2, u'rnr2::RNR2*':3,
                u'rnr2Δ WA/RNR2 NA':4, u'RNR2 WA/rnr2Δ NA':5,
                u'RNR2*/rnr2Δ':6, u'rnr2*Δ/RNR2':7}, 
       u'RNR4':{u'WT':0, u'rnr4Δ':1, u'rnr4Δ/RNR4':2,
                u'rnr4Δ WA/RNR4 NA':3, u'RNR4 WA/rnr4Δ NA':4, u'rnr4::RNR4*':5}},
'RM': {u'CTF8':{u'WT':0, u'ctf8Δ':1,
                u'ctf8Δ WA/CTF8 NA':2, u'CTF8 WA/ctf8Δ NA':3}, 
       u'DEP1':{u'WT':0, u'dep1Δ':1,
                u'dep1Δ WA/DEP1 NA':2, u'DEP1 WA/dep1Δ NA':3},
       u'FPR1':{u'WT':0, u'fpr1Δ':1, u'fpr1Δ/FPR1':2,
                u'fpr1Δ WA/FPR1 NA':3, u'FPR1 WA/fpr1Δ NA':4, u'fpr1::FPR1*':5},
       u'INP54':{u'WT':0, u'inp54Δ':1,
                 u'inp54Δ WA/INP54 NA':2, u'INP54 WA/inp54Δ NA':3}, 
       u'KOG1':{u'WT':0, u'kog1Δ WA/KOG1 NA':1, u'KOG1 WA/kog1Δ NA':2},
       u'TOR1':{u'WT':0, u'tor1Δ':1, u'tor1Δ/TOR1':2, 
                u'tor1Δ WA/TOR1 NA':3, u'TOR1 WA/tor1Δ NA':4, 
                u'TOR1*/tor1Δ':5, u'tor1*Δ/TOR1':6},
       u'YNR066C':{u'WT':0, u'ynr066cΔ':1,
                   u'ynr066cΔ WA/YNR066C NA':2, u'YNR066C WA/ynr066cΔ NA':3}}
}

# statistical tests for genetic constructs
construct_tests = {
    u'CTF8':{
        (u'WA', u'ctf8Δ'): (u'WA', u'WT'),
        (u'NA', u'ctf8Δ'): (u'NA', u'WT'),
        (u'WA/NA', u'ctf8Δ'): (u'WA/NA', u'WT'),
        (u'WA/NA', u'CTF8 WA/ctf8Δ NA'): (u'WA/NA', u'ctf8Δ WA/CTF8 NA')
    },
    u'DEP1':{
        (u'WA', u'dep1Δ'): (u'WA', u'WT'),
        (u'NA', u'dep1Δ'): (u'NA', u'WT'),
        (u'WA/NA', u'dep1Δ'): (u'WA/NA', u'WT'),
        (u'WA/NA', u'DEP1 WA/dep1Δ NA'): (u'WA/NA', u'dep1Δ WA/DEP1 NA')
    },
    u'FPR1':{
        (u'WA', u'fpr1Δ'): (u'WA', u'WT'),
        (u'NA', u'fpr1Δ'): (u'NA', u'WT'),
        (u'WA/WA', u'fpr1Δ/FPR1'): (u'WA/WA', u'WT'),
        (u'NA/NA', u'fpr1Δ/FPR1'): (u'NA/NA', u'WT'),
        (u'WA/NA', u'fpr1Δ'): (u'WA/NA', u'WT'),
        (u'WA/NA', u'FPR1 WA/fpr1Δ NA'): (u'WA/NA', u'fpr1Δ WA/FPR1 NA')
    },
    u'INP54':{
        (u'WA', u'inp54Δ'): (u'WA', u'WT'),
        (u'NA', u'inp54Δ'): (u'NA', u'WT'),
        (u'WA/NA', u'inp54Δ'): (u'WA/NA', u'WT'),
        (u'WA/NA', u'INP54 WA/inp54Δ NA'): (u'WA/NA', u'inp54Δ WA/INP54 NA')
    },
    u'KOG1':{
        (u'WA/NA', u'KOG1 WA/kog1Δ NA'): (u'WA/NA', u'kog1Δ WA/KOG1 NA')
    },
    u'RNR2':{
        (u'WA', u'rnr2Δ'): (u'WA', u'WT'),
        (u'NA', u'rnr2Δ'): (u'NA', u'WT'),
        (u'WA/WA', u'rnr2Δ/RNR2'): (u'WA/WA', u'WT'),
        (u'NA/NA', u'rnr2Δ/RNR2'): (u'NA/NA', u'WT'),
        (u'WA/NA', u'rnr2*Δ/RNR2'): (u'WA/NA', u'RNR2*/rnr2Δ'),
        (u'WA/NA', u'RNR2 WA/rnr2Δ NA'): (u'WA/NA', u'rnr2Δ WA/RNR2 NA')
    },
    u'RNR4':{
        (u'WA', u'rnr4Δ'): (u'WA', u'WT'),
        (u'NA', u'rnr4Δ'): (u'NA', u'WT'),
        (u'WA/WA', u'rnr4Δ/RNR4'): (u'WA/WA', u'WT'),
        (u'NA/NA', u'rnr4Δ/RNR4'): (u'NA/NA', u'WT'),
        (u'NA/NA', u'rnr4::RNR4*'): (u'NA/NA', u'WT'),
        (u'WA/NA', u'RNR4 WA/rnr4Δ NA'): (u'WA/NA', u'rnr4Δ WA/RNR4 NA')
    },
    u'TOR1':{
        (u'WA', u'tor1Δ'): (u'WA', u'WT'),
        (u'NA', u'tor1Δ'): (u'NA', u'WT'),
        (u'WA/WA', u'tor1Δ/TOR1'): (u'WA/WA', u'WT'),
        (u'NA/NA', u'tor1Δ/TOR1'): (u'NA/NA', u'WT'),
        (u'WA/NA', u'tor1*Δ/TOR1'): (u'WA/NA', u'TOR1*/tor1Δ'),
        (u'WA/NA', u'TOR1 WA/tor1Δ NA'): (u'WA/NA', u'tor1Δ WA/TOR1 NA')
    },
    u'YNR066C':{
        (u'WA', u'ynr066cΔ'): (u'WA', u'WT'),
        (u'NA', u'ynr066cΔ'): (u'NA', u'WT'),
        (u'WA/NA', u'ynr066cΔ'): (u'WA/NA', u'WT'),
        (u'WA/NA', u'YNR066C WA/ynr066cΔ NA'): (u'WA/NA', u'ynr066cΔ WA/YNR066C NA')
    }
}