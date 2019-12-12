from SMPyBandits.Arms import RestedRottingGaussian
from SMPyBandits.Policies import FEWA, EFF_FEWA, wSWA, GreedyOracle
from SMPyBandits.Environment.MAB_rotting import repetedRuns
import numpy as np
import datetime
import os
import logging

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_")
### SET Policies
policies = [
  [FEWA, {'alpha': .03, 'delta': 1}],
  [FEWA, {'alpha': .06, 'delta': 1}],
  [FEWA, {'alpha': .1, 'delta': 1}],
  [EFF_FEWA, {'alpha' : 0.06, 'delta':1, 'm':2}],
  [wSWA, {'alpha' : 0.002}],
  [wSWA, {'alpha' : 0.02}],
  [wSWA, {'alpha' : 0.2}],
]
policy_ind = 6
policy = policies[policy_ind]
policy_name = str(policy[0](nbArms=2, **policy[1]))
policy_name_nospace = policy_name.replace (' ', '_')

path = os.path.join('./data', 'REGRET_' + policy_name_nospace + '_' + date )
os.makedirs('./data/logging/', exist_ok = True)
logging.basicConfig(filename=os.path.join('./data/logging', date + '.log'), level=logging.INFO, format='%(asctime)s %(message)s')
logging.info("Policy : %s$" % (policy_name))

PARALLEL = -1 # Set positive int to indicate the number of core, -1 to use all the cores, and False to not parallelize
REPETITIONS =  4 # Set the number of repetitions
HORIZON = 10000 # Horizon T
sigma = 1 # Gaussian noise std

### SET L/2 in figure 1
mus = [.01 * 1.25 ** i for i in range(30)]
logging.info("CONFIG : CPU %s" % os.cpu_count())
logging.info("CONFIG : REPETITIONS %s" % REPETITIONS)
logging.info("CONFIG : HORIZON %s" % HORIZON)
logging.info("CONFIG : SIGMA %s" % sigma)

noisy_reward_res =[]
regret_res = []
time_res = []
overpull_res =[]
for m, mu in enumerate(mus):
  logging.info("GAME %s : $\mu = %s$" % (m, mu))
  print(mu)
  ### SET K arms
  arms = [
    [
      RestedRottingGaussian,
      {'decayingFunction': lambda n: mu if n <= HORIZON/4 else -mu, 'sigma': sigma, }
    ],
    [
      RestedRottingGaussian,
      {'decayingFunction': lambda n: 0, 'sigma': sigma,}
    ],
  ]
  rew, noisy_rew, time, pulls, cumul_pulls = repetedRuns(policy, arms, rep=REPETITIONS, T=HORIZON, parallel=PARALLEL)
  oracle_rew, noisy_oracle_rew, oracle_time, oracle_pull, oracle_cumul_pulls = repetedRuns([GreedyOracle, {}], arms, rep=1, T=HORIZON, oracle=True)
  regret = oracle_rew - rew
  logging.info("EVENT : SAVING ... ")
  regret_res.append(regret)
  np.save(path, np.array(regret_res))
logging.info("EVENT : END ... ")




