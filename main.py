""" Framework layout to run SAO - Sequential Approximate Optimizaion."""
from sao_opt.doe import RandomDoE
from sao_opt.trust_region import TrustRegion
from sao_opt.opt_problem import OptimizationProblem
from sao_opt.surrogate import RadialBasisSurrogate
from sao_opt.sequence import Sequence

# ---------- Problem Layer -----------------
# Create problem
problem = OptimizationProblem()

# Create trust region
x_init = problem.nominal
delta = problem.delta
bound = problem.bounds

# Optimization settings
ite_max = problem.ite_max
lcons = problem.linear


# ---------- Init Routine Layer ----------------
# Trust region
trust_region = TrustRegion(x_init, delta, bound.lb, bound.ub)
new_lb, new_ub = trust_region.determine_search_region()

# Lhs sample
doe = RandomDoE(new_lb, new_ub)

# Evaluate in High fidelity model
samples_output = problem.high_fidelity(doe.samples)

# Surrogate model
surrogate = RadialBasisSurrogate(doe.samples, samples_output)

# ---------- Sequence Layer -----------------
