 #!/usr/bin/python
 # -*- coding: utf-8 -*-
 
""" 
Gaussian mixture model
"""

# Load external dependencies
from setup import *
# Load internal dependencies
from sklearn.mixture import GaussianMixture

def gmm_fit(X, N):
    """
    Fit models with N range components
    """
    models = [None for i in range(len(N))]
    
    for i in range(len(N)):
        models[i] = GaussianMixture(N[i], n_init=100).fit(X)
        
    return models

def gmm_plot(ax, X, M_best, label=None):
    """
    Learn the best-fit GMM models
    The fit() method uses Expectation-Maximization to find 
    the best mixture of Gaussians for the data

    Plot the results in three panels:
    1) data + best-fit mixture
    2) AIC and BIC vs number of components
    3) probability that a point came from each component
    """

    # Plot data + best-fit mixture
    x = np.linspace(X.min()-.2, X.max()+.2, 1000)
    logprob, responsibilities = M_best.score_samples(np.array([x]).T)
    pdf = np.exp(logprob)
    pdf_individual = responsibilities * pdf[:, np.newaxis]

    ax.hist(X, 30, normed=True, histtype='stepfilled', alpha=0.5)
    ax.plot(x, pdf, '-k', label=label)
    ax.plot(x, pdf_individual, '--k', label=label)
    # ax.set_xlabel('$x$')
    # ax.set_ylabel('$p(x)$')
    
    # print M_best.n_components, M_best.means_.ravel()
    
def gmm_components(AIC, BIC, N):
    """
    Plot AIC and BIC
    """
    ax = plt.gca()
    ax.plot(N, AIC, '-k', label='AIC')
    ax.plot(N, BIC, '--k', label='BIC')
    ax.set_xlabel('No. components')
    ax.set_ylabel('Information criterion')
    ax.legend(loc=2)

def gmm_posterior(ax, X, M_best):
    """
    Plot posterior probabilities for each component
    """
    ax = plt.gca()

    x = np.linspace(X.min()-.2, X.max()+.2, 1000)
    p = M_best.predict_proba(np.array([x]).T)
    p = p.cumsum(1).T

    ax.fill_between(x, 0, p[0], color='gray', alpha=0.3)
#     ax.fill_between(x, p[0], p[1], color='gray', alpha=0.5)
#     ax.fill_between(x, p[1], 1, color='gray', alpha=0.7)
    ax.set_xlim(X.min()-.2, X.max()+.2)
    ax.set_ylim(0, 1)
    ax.set_xlabel('$\lambda$')
    ax.set_ylabel(r'$p(j|\lambda)$')