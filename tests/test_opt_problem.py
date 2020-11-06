""" Test with OptimizationProblem class."""
import pytest
import numpy as np
from sao_opt.opt_problem import OptimizationProblem


@pytest.fixture(name="problem")
def fix_problem():
    """ Create a instance of the class."""
    return OptimizationProblem()


def test_opt_param(problem):
    """ Test opt_param dictionary. """
    assert problem.opt_param["delta"] == 0.2
    assert problem.opt_param["ite_max"] == 50
    assert problem.opt_param["ite_max_sao"] == 20
    assert problem.opt_param["tol_opt"] == 1e-5
    assert problem.opt_param["tol_delta"] == 1e-3


def test_create_matrix(problem):
    """ Test the linear constraint matrix."""
    matrix = problem._create_matrix()
    true = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]]
    assert np.array_equal(matrix, true)


def test_get_upper(problem):
    """ Evaluate the upper bound in the linear constraint."""
    eva = problem.get_upper()
    true = [400/120, 440/79.5]
    assert np.array_equal(eva, true)


def test_bounds(problem):
    """ Test the bound constraint."""
    eva = problem.bounds
    assert np.array_equiv(eva.lb, 12*[0])
    assert np.array_equiv(eva.ub, 12*[1])


def test_linear_const(problem):
    """ Test the linear constraint."""
    breakpoint()
    assert problem.linear is not None
