def monte_carlo(network, base_demand, planner, stochastic_fn, runs=30):
    from simulation.multi_period import run_multi_period
    results = []
    for _ in range(runs):
        cost = run_multi_period(network, base_demand, planner, stochastic_fn)
        results.append(cost)
    avg = sum(results)/len(results)
    var = sum((x-avg)**2 for x in results)/len(results)
    return avg, var
