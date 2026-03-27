# Integrated Transport Systems Model

## Overview

This project implements a system-level framework for transport planning under uncertainty.

It models the coordinated allocation of resources across a network using centralized decision-making, integrating flow optimization, stochastic demand, and multi-period simulation.

---

## Problem

Given a transportation network with supply and demand nodes, the objective is to determine how resources should be distributed over time while minimizing total cost and respecting capacity constraints.

Unlike local routing approaches, this model operates at a **system-wide level**, coordinating all flows globally.

---

## Model Structure

The system is based on a dynamic network flow formulation:

* Directed graph representation
* Capacity-constrained edges
* Flow conservation at nodes
* Multi-period evolution

The objective is to minimize expected transport cost:

[
\min \mathbb{E} \left[ \sum_{t} \sum_{i,j} c_{ij}(t,\omega) x_{ij}(t) \right]
]

---

## Methodology

### Centralized Planning

A global planner allocates flows across the network, ensuring coordinated decision-making.

### Multi-Period Simulation

The system evolves over time, capturing accumulation and dynamic behavior.

### Stochastic Demand

Demand is modeled as a random variable, introducing uncertainty.

### Monte Carlo Evaluation

Repeated simulations are used to estimate:

* Expected cost
* Variance
* System sensitivity

---

## Results

Example output:

```text
Centralized -> avg: 1701.46
Variance: 99692.71
```

### Interpretation

* The system successfully allocates flow across the network
* Centralized planning ensures global coordination
* High variance reveals strong sensitivity to uncertainty

---

## Key Insight

Centralized planning improves coordination and enables system-level optimization, but uncertainty introduces significant variability in performance.

This highlights the need for robust or adaptive planning strategies in real-world transport systems.

---

## Project Structure

```
core/           # network and flow model
planners/       # centralized planning logic
uncertainty/    # stochastic demand and costs
simulation/     # multi-period + Monte Carlo
experiments/    # evaluation pipeline
analysis/       # metrics
```

---

## How to Run

```bash
export PYTHONPATH=.
python experiments/system_evaluation.py
```

---

## Applications

* Logistics network optimization
* Supply chain coordination
* Urban transport systems
* Resource allocation under uncertainty

---

## Positioning

This project is not a routing heuristic implementation.
It is a **system-level transport model** integrating optimization, simulation, and uncertainty analysis.

---

## Author

Integrated systems engineering project
