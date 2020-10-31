""" Framework layout to run SAO - Sequential Approximate Optimizaion."""
import numpy as np
from sao_opt.doe import DoE
# from sao_opt.surrogate import Surrogate

# ---------- Problem Layer -----------------
DIM = 2
SAMPLES = 4
min_val = np.array([2, 10])
max_val = np.array([5, 15])

# ---------- Routine Layer ----------------
doe = DoE(DIM, SAMPLES, min_val, max_val)
sample_points = doe.determine_plan_points()

# TODO: evaluate sample_points with IMEX.

# surrogate = Surrogate(sample_points, imex_eval)


# ---------- Sequence Layer -----------------
