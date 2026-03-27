from core.network import Network
from planners.centralized import centralized_plan
from uncertainty.demand import stochastic_demand
from simulation.monte_carlo import monte_carlo

nodes = ['factory','warehouse','city']

edges = {('factory','warehouse'):2, ('warehouse','city'):3, ('factory','city'):5}
capacities = {('factory','warehouse'):100, ('warehouse','city'):100, ('factory','city'):50}
base_demand = {'factory':100, 'warehouse':0, 'city':-100}

network = Network(nodes, edges, capacities)

avg, var = monte_carlo(network, base_demand, centralized_plan, stochastic_demand)

print('Centralized -> avg:', avg, 'var:', var)
