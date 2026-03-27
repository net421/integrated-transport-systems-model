def run_multi_period(network, base_demand, planner, stochastic_fn=None, T=5):
    total_cost = 0
    for t in range(T):
        demand = {}
        for k,v in base_demand.items():
            demand[k] = stochastic_fn(v) if stochastic_fn else v
        flow = planner(network, demand)
        cost = sum(network.edges[(i,j)] * val for (i,j,_), val in flow.items())
        total_cost += cost
    return total_cost
