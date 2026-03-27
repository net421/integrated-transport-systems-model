def compute_cost(flow, costs):
    total = 0
    for (i,j,t), value in flow.items():
        total += costs[(i,j)] * value
    return total
