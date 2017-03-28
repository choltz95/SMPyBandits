# -*- coding: utf-8 -*-
""" Arms : contains different types of bandit arms:
Uniform, Bernoulli, Poisson, Gaussian, Exponential.

Also contain makeMeans, a small function to generate uniformly spacen means of arms.
"""

__author__ = "Lilian Besson"
__version__ = "0.6"

from random import shuffle
from copy import copy
import numpy as np

if __name__ != "__main__":
    from .Uniform import Uniform
    from .Bernoulli import Bernoulli
    from .Binomial import Binomial
    from .Poisson import Poisson, UnboundedPoisson
    from .Gaussian import Gaussian, UnboundedGaussian
    from .Exponential import Exponential, ExponentialFromMean, UnboundedExponential
    from .Gamma import Gamma, GammaFromMean, UnboundedGamma


def makeMeans(nbArms=3, delta=0.1, lower=0., amplitude=1.):
    """Return a list of means of arms, well spacen:

    - in [lower, lower + amplitude],
    - sorted in increasing order,
    - starting from lower + amplitude * delta, up to lower + amplitude * (1 - delta),
    - and there is nbArms arms.

    >>> makeMeans(2, 0.1)
    array([ 0.1,  0.9])
    >>> makeMeans(3, 0.1)
    array([ 0.1,  0.5,  0.9])
    >>> makeMeans(9, 1 / (1. + 9))
    array([ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
    """
    assert nbArms >= 1, "Error: nbArms has to be >= 1."
    assert 0 < delta < 1, "Error: delta has to be in (0, 1)."
    # return list(lower + amplitude * np.linspace(delta, 1 - delta, nbArms))
    return lower + amplitude * np.linspace(delta, 1 - delta, nbArms)


def randomMeans(nbArms=3, mingap=0.05, lower=0., amplitude=1., sorted=True):
    """Return a list of means of arms, randomly sampled uniformly in [lower, lower + amplitude], with a min gap >= mingap.

    - All means will be different, except if mingap = None, with a min gap > 0.

    >>> import numpy as np; np.random.seed(1234)  # reproducible results
    >>> randomMeans(nbArms=3, mingap=0.05)  # doctest: +ELLIPSIS
    array([ 0.191...,  0.437...,  0.622...])
    >>> randomMeans(nbArms=3, mingap=0.1)  # doctest: +ELLIPSIS
    array([ 0.276...,  0.801...,  0.958...])

    - Means are sorted, except if sorted=False.

    >>> randomMeans(nbArms=5, mingap=0.1, sorted=True)  # doctest: +ELLIPSIS
    array([ 0.006...,  0.229...,  0.416...,  0.535...,  0.899...])
    >>> randomMeans(nbArms=5, mingap=0.1, sorted=False)  # doctest: +ELLIPSIS
    array([ 0.419...,  0.932...,  0.072...,  0.755...,  0.650...])
    """
    mus = np.sort(np.random.rand(nbArms))
    if mingap is not None and mingap > 0:
        while np.min(np.diff(mus)) <= mingap:  # Ensure a min gap > mingap
            mus = np.sort(np.random.rand(nbArms))
    if not sorted:
        np.random.shuffle(mus)
    return lower + (amplitude * mus)


def shuffled(mylist):
    """Returns a shuffled version of the input 1D list. sorted() exists instead of list.sort(), but shuffled() does not exist instead of random.shuffle()...

    >>> from random import seed; seed(1234)  # reproducible results
    >>> mylist = [ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9]
    >>> shuffled(mylist)
    [0.9, 0.4, 0.3, 0.6, 0.5, 0.7, 0.1, 0.2, 0.8]
    >>> shuffled(mylist)
    [0.4, 0.3, 0.7, 0.5, 0.8, 0.1, 0.9, 0.6, 0.2]
    >>> shuffled(mylist)
    [0.4, 0.6, 0.9, 0.5, 0.7, 0.2, 0.1, 0.3, 0.8]
    >>> shuffled(mylist)
    [0.8, 0.7, 0.3, 0.1, 0.9, 0.5, 0.6, 0.2, 0.4]
    """
    copiedlist = copy(mylist)
    shuffle(copiedlist)
    return copiedlist


# --- Debugging

if __name__ == "__main__":
    # Code for debugging purposes.
    from doctest import testmod
    print("\nTesting automatically all the docstring written in each functions of this module :")
    testmod(verbose=True)
