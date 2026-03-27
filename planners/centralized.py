def centralized_plan(network, demand):
    flow = {}
    remaining = demand.copy()

    supply_nodes = [n for n, v in remaining.items() if v > 0]
    demand_nodes = [n for n, v in remaining.items() if v < 0]

    # Paso 1: enviar a nodos intermedios
    for (i, k), cost in network.edges.items():
        if i in supply_nodes and remaining[i] > 0:
            cap = network.capacities[(i, k)]

            send = min(remaining[i], cap)

            if send > 0:
                flow[(i, k, 0)] = send
                remaining[i] -= send
                remaining[k] = remaining.get(k, 0) + send

    # Paso 2: de intermedios a demanda
    for (k, j), cost in network.edges.items():
        if j in demand_nodes and remaining[j] < 0 and remaining.get(k, 0) > 0:
            cap = network.capacities[(k, j)]

            send = min(remaining[k], -remaining[j], cap)

            if send > 0:
                flow[(k, j, 0)] = send
                remaining[k] -= send
                remaining[j] += send

    return flow