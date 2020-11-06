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
    assert matrix.shape == (4, 24)
    assert matrix[0][0] == 1
    assert matrix[0][4] == 0
    assert matrix[1][0] == 0
    assert matrix[1][4] == 1
    assert matrix[2][0] == 0
    assert matrix[2][12] == 1
    assert matrix[2][16] == 0


def test_get_upper(problem):
    """ Evaluate the upper bound in the linear constraint."""
    eva = problem.get_upper()
    true = [400/120, 440/79.5] * 2
    assert np.array_equal(eva, true)


def test_bounds(problem):
    """ Test the bound constraint."""
    eva = problem.bounds
    assert np.array_equiv(eva.lb, 12*[0])
    assert np.array_equiv(eva.ub, 12*[1])


def test_linear_create(problem):
    """ Test the linear constraint."""
    assert problem.linear is not None


def test_linear_constraint_dot_nominal(problem):
    """ Verify if 'matrix * x <= upper'."""
    upper = problem.get_upper()
    matrix = problem._create_matrix()
    eva = np.dot(matrix, problem.nominal[0].T)
    assert all(value <= ubound for value, ubound in zip(eva, upper))


def test_linear_constraint_dot_total(problem):
    """ Verify if 'matrix * x <= upper'."""
    upper = problem.get_upper()
    matrix = problem._create_matrix()
    x_top = np.array([1] * 24)
    eva = np.dot(matrix, x_top.T)
    assert all(value >= ubound for value, ubound in zip(eva, upper))
