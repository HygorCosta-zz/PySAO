""" Framework layout to run SAO - Sequential Approximate Optimizaion."""
import numpy as np
from design_of_experiments import DoE

# ---------- Problem Layer -----------------
DIM = 2
SAMPLES = 4
min_val = np.array([2, 10])
max_val = np.array([5, 15])

# ---------- Sequence Layer ----------------
doe = DoE(DIM, SAMPLES, min_val, max_val)
sample_points = doe.determine_plan_points()


# ---------- Routine Layer -----------------
