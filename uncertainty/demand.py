import random

def stochastic_demand(base):
    return max(0, int(random.gauss(base, 5)))
