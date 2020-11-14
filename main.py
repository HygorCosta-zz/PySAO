""" Framework layout to run SAO - Sequential Approximate Optimizaion."""
import time
from sao_opt.doe import RandomDoE
from sao_opt.trust_region import TrustRegion
from sao_opt.opt_problem import OptimizationProblem, Simulation
from sao_opt.surrogate import RbfPoly
from sao_opt.solver import TrustConstrSolver
from sao_opt.sequence import Sequence
from sao_opt.converge import Converge
from sao_opt.results import Results

start = time.process_time()

# ---------- Problem Layer -----------------
# Create problem
simulation = Simulation()
problem = OptimizationProblem()

# Initial guess
x0 = simulation.nominal


# ---------- Init Routine Layer ----------------
# Trust region
trust_region = TrustRegion(x0, problem)

# Lhs sample
doe = RandomDoE(trust_region.lower, trust_region.upper)

# Surrogate model
surrogate = RbfPoly(doe)

# Optimizer Solver
solver = TrustConstrSolver(problem.linear)

# Results
results = Results()

# Converge
converge = Converge(results, problem)


# ---------- Sequence Layer -----------------
sequence = Sequence(simulation, trust_region, surrogate,
                    solver, converge, results)
sequence.run()

# ----------- Final Resusts ------------------
end = time.process_time()
with open("results.csv", "a") as result:
    result.write(f"CPU time consume: {end - start} seg.")
    result.write(f"Number of hf evaluations: \
    {sequence.simulation.num_simulations}.")
