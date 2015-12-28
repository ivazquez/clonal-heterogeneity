""" 
Module for 
Mixture model.
ANOVA and variance explained analysis. 
"""

from collections import defaultdict

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from sklearn.mixture import GMM

def gmm_fit(X, N):
    # fit models with N range components
    models = [None for i in range(len(N))]
    
    for i in range(len(N)):
        models[i] = GMM(N[i]).fit(X)
        
    return models

def gmm_plot(X, M_best, label=None):
    #------------------------------------------------------------
    # Learn the best-fit GMM models
    #  Here we'll use GMM in the standard way: the fit() method
    #  uses an Expectation-Maximization approach to find the best
    #  mixture of Gaussians for the data

    ax = plt.gca()

    #------------------------------------------------------------
    # Plot the results
    #  We'll use three panels:
    #   1) data + best-fit mixture
    #   2) AIC and BIC vs number of components
    #   3) probability that a point came from each component

    # plot data + best-fit mixture
    x = np.linspace(X.min()-.2, X.max()+.2, 1000)
    logprob, responsibilities = M_best.score_samples(np.array([x]).T)
    pdf = np.exp(logprob)
    pdf_individual = responsibilities * pdf[:, np.newaxis]

    ax.hist(X, 30, normed=True, histtype='stepfilled', alpha=0.5)
    ax.plot(x, pdf, '-k', label=label)
    ax.plot(x, pdf_individual, '--k', label=label)
    ax.text(0.04, 0.96, "Best-fit mixture",
        ha='left', va='top', transform=ax.transAxes)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$p(x)$')
    
    print M_best.n_components, M_best.means_.ravel()

    
def gmm_components(AIC, BIC, N):
    # plot AIC and BIC
    ax = plt.gca()
    ax.plot(N, AIC, '-k', label='AIC')
    ax.plot(N, BIC, '--k', label='BIC')
    ax.set_xlabel('No. components')
    ax.set_ylabel('Information criterion')
#     ax.legend(loc=2)


def gmm_posterior(X, M_best):
    # plot posterior probabilities for each component
    ax = plt.gca()

    x = np.linspace(X.min()-.2, X.max()+.2, 1000)
    p = M_best.predict_proba(np.array([x]).T)
#     p = p[:, (1, 0, 2)]  # rearrange order so the plot looks better
    p = p.cumsum(1).T

    ax.fill_between(x, 0, p[0], color='gray', alpha=0.3)
#     ax.fill_between(x, p[0], p[1], color='gray', alpha=0.5)
#     ax.fill_between(x, p[1], 1, color='gray', alpha=0.7)
    ax.set_xlim(X.min()-.2, X.max()+.2)
    ax.set_ylim(0, 1)
    ax.set_xlabel('$x$')
    ax.set_ylabel(r'$p({\rm class}|x)$')

#     ax.text(-5, 0.3, 'class 1', rotation='vertical')
#     ax.text(0, 0.5, 'class 2', rotation='vertical')
#     ax.text(3, 0.3, 'class 3', rotation='vertical')

#     plt.show()


from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

def run_anova(formula, df):
    lm = ols(formula, df).fit()
    anova = anova_lm(lm, type=3)
    return lm, anova

def fraction_of_explainable_variance(factor, anova):
    factors = [ each for each in anova.index if each != 'Residual' ]
    num = anova.ix[factor]['sum_sq']
    denom = anova.ix[factors]['sum_sq'].sum()
    return num/denom

def variance_explained(factor, anova):
    
    return anova.ix[factor]['sum_sq']/anova['sum_sq'].sum()

def mean_vectors(factor_data, formula, var_func=variance_explained):
    results = defaultdict(list)
#     for ii, (col, series) in enumerate(activity.iteritems()):
#         factor_data['doubling_time'] = series.astype(float)
    lm, anova = run_anova(formula, factor_data)
    factors = [each for each in anova.index if each != 'Residual']
    for factor in factors:
        results[factor].append(var_func(factor, anova))
#         results[factor].append(fraction_of_explainable_variance(factor, anova))
#         results['P({})'.format(factor)].append(anova.ix[factor]['PR(>F)'])
    return lm#pd.DataFrame(results)

def variance_vectors(factor_data, formula, var_func=variance_explained):
    results = defaultdict(list)
#     for ii, (col, series) in enumerate(activity.iteritems()):
#         factor_data['doubling_time'] = series.astype(float)
    lm, anova = run_anova(formula, factor_data)
    factors = [each for each in anova.index if each != 'Residual']
    for factor in factors:
        results[factor].append(var_func(factor, anova))
#         results[factor].append(fraction_of_explainable_variance(factor, anova))
#         results['P({})'.format(factor)].append(anova.ix[factor]['PR(>F)'])
    return pd.DataFrame(results)