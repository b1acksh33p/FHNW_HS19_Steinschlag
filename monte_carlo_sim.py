import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import datetime

mu_masse_1 = 5.944892676091842
s_masse_1 = 1.0452954216771342
mu_masse 2 = 4.012421689011621
s_masse_2 = 1.2811831375376432
mu_speed_1 = 8.788235294117646
s_speed_1 = 1.9745088303442118
mu_speed_2 = 37.790625
s_speed_2 = 5.31080027956004
alpha_t_delta_1 = 0.7720943018929209
beta_t_delta_1 = 32.180388904581854
alpha_t_delta_2 = 0.6924339239082432
beta_t_delta_2 = 85.33142881264439


def random_masse_1():
    masse_1 = np.random.lognormal(mu_masse_1, s_masse_1, 1).round(1)
    return masse_1

def random_masse_2():
    masse_2 = np.random.lognormal(mu_masse_2, s_masse_2, 1).round(1)
    return masse_2

def random_speed_1():
    speed_1 = np.random.normal(mu_speed_1, s_speed_1, 1).round(2)
    return speed_1

def random_speed_2():
    speed_2 = np.random.normal(mu_speed_2, s_speed_2, 1).round(2)
    return speed_2

def random_t_delta_1():
    t_delta_1 = int(np.random.gamma(alpha_t_delta_1, beta_t_delta_1, 1).round(0))
    return t_delta_1

def random_t_delta_2():
    t_delta_2 = int(np.random.gamma(alpha_t_delta_2, beta_t_delta_2, 1).round(0))

results = pd.results