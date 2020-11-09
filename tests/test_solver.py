""" Test Solver class."""
from scipy.optimize import Bounds
import pytest
import numpy as np
from sao_opt.solver import TrustConstrSolver


def sphere(design_var):
    """ Evalute design_var in sphere function."""
    return np.sum(np.power(design_var, 2))


@pytest.fixture(name="solver")
def fix_solver():
    """ Crete a instance of the TrustConstrSolver class."""
    x_init = np.array([2, 2, 2, 2, 2])
    lower = np.full_like(x_init, -5.12)
    upper = np.full_like(x_init, 5.12)
    bounds = Bounds(lower, upper)
    return TrustConstrSolver(sphere, x_init, bounds)


def test_if_instance_was_created(solver):
    """ Test if the fixture was created."""
    assert solver is not None


def test_optimize_sucess(solver):
    """ Test if the optimization was successfully."""
    solver.maximize_npv()
    assert solver.result.success


def test_optimize_value(solver):
    """ Test if the solver find the optimal value."""
    solver.maximize_npv()
    assert solver.result.fun == pytest.approx(0, 0.01)


def test_optimize_variable(solver):
    """ Test if the solver find the optimal design variable."""
    solver.maximize_npv()
    assert np.allclose(solver.result.x, [0, 0, 0, 0, 0])
