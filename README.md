# Bandit algorithms and the aggregated bandit
This repository contains the code of [my](http://perso.crans.org/besson/) numerical environment, written in [Python](https://www.python.org/), in order to perform numerical simulations on *single*-player and *multi*-players [Multi-Armed Bandits (MAB)](https://en.wikipedia.org/wiki/Multi-armed_bandit) algorithms.

[![PyPI implementation](https://img.shields.io/pypi/implementation/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/AlgoBandits/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)

[I (Lilian Besson)](http://perso.crans.org/besson/) have [starting my PhD](http://perso.crans.org/besson/phd/) in October 2016, and this is a part of my **on going** research.

----

## 1st contribution: The [**policy aggregation algorithm**](Aggr.md)
I designed and added the [`Aggr`](Policies/Aggr.py) policy, in order to test its validity and performance.

It is a "simple" **voting algorithm to combine multiple bandit algorithms into one**.
Basically, it behaves like a simple MAB bandit just based on empirical means (even simpler than UCB), where *arms* are the child algorithms `A_1 .. A_N`, each running in "parallel".

**For more details**, refer to this file: [`Aggr.md`](Aggr.md).

----

## 2nd contribution: [**Multi-players simulation environment**](MultiPlayers.md)
> I have started the multi-player part, it will take time to be finished.

There is another point of view: instead of comparing different single-player policies on the same problem, we can make them play against each other, in a multi-player setting.
The basic difference is about **collisions** : at each time `t`, if two or more user chose to sense the same channel, there is a *collision*. Collisions can be handled in different way from the base station point of view, and from each player point of view.

**For more details**, refer to this file: [`MultiPlayers.md`](MultiPlayers.md).

----

## Remarks
- Everything here is done in an imperative, object oriented style. I will document the API of the Arms and Policy classes.
- The code is [clean](logs/main_pylint_log.txt), valid for both [Python 2](logs/main_pylint_log.txt) and [Python 3](logs/main_pylint3_log.txt).
- Some piece of code come from the [pymaBandits](http://mloss.org/software/view/415/) project, but most of them were refactored. Thanks to the initial project!
- [G.Varoquaux](http://gael-varoquaux.info/)'s [joblib](https://pythonhosted.org/joblib/) is used for the [`Evaluator`](Environment/Evaluator.py) class, so the simulations can easily be parallelized. (Put `n_jobs = -1` or `PARALLEL = True` in the config file to use all your CPU cores, as it is by default).

### Warning
- This work is still in **its early stage of development**! It's [active research](https://github.com/Naereen/AlgoBandits/graphs/contributors).
- This aggregated bandit algorithm has NO THEORETICAL warranties what so ever - *yet*.

### UML diagrams
For more details, see [these UML diagrams](uml_diagrams/):

- Packages: organization of the different files:
[![UML Diagram - Packages of AlgoBandits.git](uml_diagrams/packages_AlgoBandits.png)](uml_diagrams/packages_AlgoBandits.svg)
- Classes: inheritance diagrams of the different classes:
[![UML Diagram - Classes of AlgoBandits.git](uml_diagrams/classes_AlgoBandits.png)](uml_diagrams/classes_AlgoBandits.svg)

----

## :boom: [TODO](TODO.md)
> See this file [`TODO.md`](TODO.md), and [the issues](https://github.com/Naereen/AlgoBandits/issues).

----

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/AlgoBandits.svg)](https://github.com/Naereen/AlgoBandits/blob/master/LICENSE)
[MIT Licensed](https://lbesson.mit-license.org/) (file [LICENSE](LICENSE)).

© 2012 [Olivier Cappé](http://perso.telecom-paristech.fr/%7Ecappe/), [Aurélien Garivier](https://www.math.univ-toulouse.fr/%7Eagarivie/), [Émilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/) and for the initial [pymaBandits v1.0](http://mloss.org/software/view/415/) project, and © 2016 [Lilian Besson](https://GitHub.com/Naereen) for the rest.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/AlgoBandits/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/AlgoBandits/README.md?pixel)](https://GitHub.com/Naereen/AlgoBandits/)

![PyPI implementation](https://img.shields.io/pypi/implementation/ansicolortags.svg)
![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
