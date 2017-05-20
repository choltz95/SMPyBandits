# -*- coding: utf-8 -*-
""" PoliciesMultiPlayers : contains various collision-avoidance protocol for the multi-players setting.

- :class:`Selfish`: a multi-player policy where every player is selfish, they do not try to handle the collisions.

- :class:`CentralizedNotFair`: a multi-player policy which uses a centralize intelligence to affect users to a FIXED arm.
- :class:`CentralizedFair`: a multi-player policy which uses a centralize intelligence to affect users an offset, each one take an orthogonal arm based on (offset + t) % nbArms.

- :class:`CentralizedMultiplePlay` and :class:`CentralizedIMP`: multi-player policies that use centralized but non-omniscient learning to select K = nbPlayers arms at each time step.

- :class:`OracleNotFair`: a multi-player policy with full knowledge and centralized intelligence to affect users to a FIXED arm, among the best arms.
- :class:`OracleFair`: a multi-player policy which uses a centralized intelligence to affect users an offset, each one take an orthogonal arm based on (offset + t) % nbBestArms, among the best arms.

- :class:`rhoRand`, :class:`ALOHA`: implementation of generic collision avoidance algorithms, relying on a single-player bandit policy (eg. :class:`UCB`, :class:`Thompson` etc). And variants, :class:`rhoRandRand`, :class:`rhoRandSticky`, :class:`rhoRandRotating`, :class:`rhoRandEst`, :class:`rhoRandLearn`, :class:`rhoRandALOHA`,


All policies have the same interface, as described in :class:`BaseMPPolicy` for decentralized policies,
and :class:`BaseCentralizedPolicy` for centralized policies,
in order to use them in any experiment with the following approach:

>>> my_policy_MP = Policy_MP(nbPlayers, nbArms, *args, lower=0, amplitude=1, **kwargs)
>>> children = my_policy_MP.children             # get a list of usable single-player policies
>>> for one_policy in children:
>>>     one_policy.startGame()                       # start the game
>>> for t in range(T):
>>>     for i in range(nbPlayers):
>>>         k_t[i] = children[i].choice()            # chose one arm, for each player
>>>     for k in range(nbArms):
>>>         players_who_played_k = [ k_t[i] for i in range(nbPlayers) if k_t[i] == k ]
>>>         reward = reward_t[k] = sampled from the arm k     # sample a reward
>>>         if len(players_who_played_k) > 1:
>>>            reward = 0
>>>         for i in players_who_played_k:
>>>             children[i].getReward(k, reward)
"""

__author__ = "Lilian Besson"
__version__ = "0.6"

# Mine, fully decentralized one
from .Selfish import Selfish

# Mine, centralized ones (but only knowledge of nbArms)
from .CentralizedFixed import CentralizedFixed
from .CentralizedCycling import CentralizedCycling

# Mine, centralized ones (with perfect knowledge)
from .OracleNotFair import OracleNotFair
from .OracleFair import OracleFair

# CentralizedMultiplePlay where ONE M multi-play bandit algorithm is ran, instead of decentralized one-play bandits ran by each of the M players
from .CentralizedMultiplePlay import CentralizedMultiplePlay
# CentralizedIMP where ONE M multi-play bandit algorithm is ran, instead of decentralized one-play bandits ran by each of the M players, with a small optimization
from .CentralizedIMP import CentralizedIMP

from .rhoRand import rhoRand  # Cf. [Anandkumar et al., 2009](http://ieeexplore.ieee.org/document/5462144/)
from .rhoRandRand import rhoRandRand  # Cf. [Anandkumar et al., 2009](http://ieeexplore.ieee.org/document/5462144/)
from .rhoEst import rhoEst  # Cf. [Anandkumar et al., 2009](http://ieeexplore.ieee.org/document/5462144/)
from .rhoLearn import rhoLearn  # Cf. [Anandkumar et al., 2009](http://ieeexplore.ieee.org/document/5462144/)
from .rhoRandSticky import rhoRandSticky  # New version, still experimental!
from .rhoRandRotating import rhoRandRotating  # New version, still experimental!
from .rhoRandALOHA import rhoRandALOHA  # New version, still experimental!

from .ALOHA import ALOHA, tnext_beta, tnext_log

# FIXME implement it
# from .TDFS import TDFS

# Adversarial settings, from some research papers
from .Scenario1 import Scenario1
