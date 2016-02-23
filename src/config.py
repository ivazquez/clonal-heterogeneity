 #!/usr/bin/python
 # -*- coding: utf-8 -*-
 
import colors
import matplotlib.patheffects as PathEffects

# population attributes
sp_bg_dict = {
    'position': {
        'HU': 
        {'parents': 0, 'ancestral': 1, 'evolved': 2},
        'RM':
        {'parents': 0, 'ancestral': 1, 'evolved': 2}
    }
}

# background attributes
sp_cl_dict = {
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
sp_gn_dict = {
    'position': {
        'HU': 
        {'RNR2': 0, 'RNR4': 1},
        'RM':
        {'no driver': 0, 'FPR1': 1, 'TOR1': 2},
    }
}

# genotype attributes
sp_gt_long_dict = {
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
sp_gt_short_dict = {
'position':
 {'HU': 
  {'+': 0, '-': 1},
  'RM': 
  {'+': 0, '-': 1}
  },
'color':
  {'HU': 
  {'+': colors.fte_colors[1], '-': colors.fte_colors[5]},
  'RM': 
  {'+': colors.fte_colors[1], '-': colors.fte_colors[5]}
  }
}

# collection attributes
hy_bg_dict = {
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
hy_cl_dict = {
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
hy_gn_dict = {
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
hy_gt_long_dict = {
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
hy_gt_short_dict = {
'position':
{'HU': 
 {('+','+'): 0, ('+','-'): 1, ('-','+'): 2, ('-','-'): 3},
'RM':
 {('+','+'): 0, ('+','-'): 1, ('-','+'): 2, ('-','-'): 3},
 },
'color':
{'HU':
 {('+','+'): colors.fte_colors[1], ('+','-'): colors.fte_colors[0], ('-','+'): colors.fte_colors[0], ('-','-'): colors.fte_colors[5]},
'RM':
 {('+','+'): colors.fte_colors[1], ('+','-'): colors.fte_colors[0], ('-','+'): colors.fte_colors[0], ('-','-'): colors.fte_colors[5]},
}
}

# factor attributes
factor_dict = {
    'color': {
        'time': colors.fte_colors[0],
        'background\n(genotype)': colors.fte_colors_dark[0],
        'de novo\n(gene identity)': colors.fte_colors[1], 
        'de novo\n(genotype)': colors.fte_colors_dark[1],
        'auxotrophy': colors.fte_colors[5],
        'tetrad': colors.fte_colors[4],
        'spore': colors.fte_colors[4]
#         'background': "#348ABD", 
#         'de_novo_gene': "#A60628", 
#         'de_novo_genotype': "#7A68A6",
#         'auxotrophy': "#467821",
#         'tetrad': "#CF4457",
#         'spore': "#188487"
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
dict_gene = {
    'position':{
        'RNR2':0, 'RNR4':1, 'no driver':0, 'FPR1':1, 'TOR1':2   
    }
}

# genotype attributes
dict_genotype = {
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
dict_population = {
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
dict_background = {
    'position':{
        'WA':0, 
        'NA':1,
        'WAxNA':2,
        'WA/WA':3, 
        'NA/NA':4,
        'WA/NA':5
    },
    'color':{
        # 'WA':colors.bg_colors[0],
        # 'NA':colors.bg_colors[1],
        # 'WAxNA':colors.bg_colors[2],
        # 'WA/WA':colors.bg_colors[0],
        # 'NA/NA':colors.bg_colors[1],
        # 'WA/NA':colors.bg_colors[2]
        'WA':colors.fte_colors[0], 
        'NA':colors.fte_colors[1], 
        'WAxNA':colors.fte_colors[2],
        'WA/WA':colors.fte_colors[0],
        'NA/NA':colors.fte_colors[1],
        'WA/NA':colors.fte_colors[2]
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

# environment attributes
dict_environment = {
    'color': {
        'HU':colors.mr_colors[2],
        'RM':colors.mr_colors[1],
        'YPD':'k'
    },
    'linewidth': {
        'HU':0.75,'RM':0.75,'YPD':0.75
    },
    'style': {
        'HU':'-','RM':'-','YPD':'-' 
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
        'YPD':'Control',
        'YNB':'Control',
        'COM':'Control', 
        'null': u'Control'
    }
}

# lineage attributes
dict_lineages = {
    'subclone A': {'fill':colors.fte_colors[0], 'line':colors.fte_colors[0]},
    'subclone B': {'fill':colors.fte_colors[1], 'line':colors.fte_colors[1]},
    'subclone C': {'fill':colors.fte_colors[2], 'line':colors.fte_colors[2]},
    'subclone D': {'fill':colors.fte_colors[3], 'line':colors.fte_colors[3]},
    'bulk': {'fill':colors.fte_colors[4], 'line':colors.fte_colors[4]},
    '': {'fill':colors.fte_colors[4], 'line':colors.fte_colors[4]},
}

# mutation type attributes
dict_mutation_type = {
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
dict_consequence_short = {
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
dict_time = {
    'color': {
        0:colors.blues[1],
        2:colors.blues[1],
        4:colors.blues[2],
        8:colors.blues[3],
        16:colors.blues[0],
        32:colors.blues[4]
    },
    'linewidth': {
        0:0.75,2:0.75,4:0.75,8:0.75,16:0.75,32:0.75
    },
    'style': {
        0:'-',2:'-',4:'-',8:'-',16:'-',32:'-'  
    }
}

# attributes for genetic constructs
dict_constructs = {
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