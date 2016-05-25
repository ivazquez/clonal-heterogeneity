 #!/usr/bin/python
 # -*- coding: utf-8 -*-
 
""" 
Variance component analysis 
"""

from collections import defaultdict

import numpy as np
import pandas as pd

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
    
def run_anova(factor_data, formula, anova_type=3):
    lm = ols(formula, factor_data).fit()
    anova = anova_lm(lm, type=anova_type)
    return lm, anova

def fraction_of_explainable_variance(factor, anova):
    factors = [ each for each in anova.index if each != 'Residual' ]
    num = anova.ix[factor]['sum_sq']
    denom = anova.ix[factors]['sum_sq'].sum()
    return num/denom

def variance_explained(factor, anova):    
    return anova.ix[factor]['sum_sq']/anova['sum_sq'].sum()
    
def variance_vectors(factor_data, formula, var_func=variance_explained):
    results = defaultdict(list)
    lm, anova = run_anova(factor_data, formula)
    factors = [each for each in anova.index if each != 'Residual']
    for factor in anova.index:
        results[('var_explained',factor)].append(var_func(factor, anova))
        results[('var_total',factor)].append(fraction_of_explainable_variance(factor, anova))
        results[('df',factor)].append(anova.ix[factor]['df'])
        results[('sum_sq',factor)].append(anova.ix[factor]['sum_sq'])
        results[('mean_sq',factor)].append(anova.ix[factor]['mean_sq'])
        results[('f_stat',factor)].append(anova.ix[factor]['F'])
        results[('p_var',factor)].append(anova.ix[factor]['PR(>F)'])
    return pd.DataFrame(results)
