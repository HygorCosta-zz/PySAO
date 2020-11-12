""" Optimization with high fidelity model."""
import numpy as np
from scipy.optimize import minimize, Bounds, rosen
from sao_opt.opt_problem import Simulation, OptimizationProblem

if __name__ == "__main__":

    # ----------- Init Layer -----------
    simulation = Simulation()
    problem = OptimizationProblem()
    x0 = np.ones_like(simulation.nominal)
    bounds = Bounds(0, 1)
    linear = problem.linear

    # ---------- Optimization Layer --------
    results = minimize(simulation, x0, method='trust-constr',
                       bounds=bounds, constraints=linear)
    breakpoint()
    print(" Optimization is finish.!! \n")
    print(f"Optimal value: {results.fun}")
    print(f"Optimal x: {results.x}")
