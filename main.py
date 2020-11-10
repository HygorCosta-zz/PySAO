""" Framework layout to run SAO - Sequential Approximate Optimizaion."""
from sao_opt.doe import RandomDoE
from sao_opt.trust_region import TrustRegion
from sao_opt.opt_problem import OptimizationProblem, Simulation
from sao_opt.surrogate import RadialBasisSurrogate
from sao_opt.solver import TrustConstrSolver
from sao_opt.sequence import Sequence
from sao_opt.converge import Converge
from sao_opt.results import Results

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

# Evaluate in High fidelity model
samples_output = simulation(doe.samples)

# Surrogate model
surrogate = RadialBasisSurrogate(doe.samples, samples_output)

# Optimizer Solver
solver = TrustConstrSolver(surrogate, x0, problem.bounds, problem.linear)

# Results
results = Results(simulation, solver, surrogate, trust_region)

# Converge
converge = Converge(results, problem)


# ---------- Sequence Layer -----------------
sequence = Sequence(simulation, trust_region, surrogate,
                    solver, converge, results)
sequence.run()

# ----------- Final Resusts ------------------
