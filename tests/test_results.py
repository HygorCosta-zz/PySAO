""" Test the Results class."""
import pytest
import numpy as np
from unittest.mock import Mock
from sao_opt.results import Results


def sphere(design_var):
    """ Sphere function."""
    if not isinstance(design_var, np.ndarray):
        design_var = np.array(design_var)

    resp = []
    if design_var.ndim == 1:
        value = np.sum(np.power(design_var, 2))
        resp.append(value)
    else:
        for array in design_var:
            value = np.sum(np.power(array, 2))
            resp.append(value)
    return resp


@pytest.fixture(name='results')
def fix_results():
    """ Create a instance of the Results class."""
    simulation = Mock()
    simulation.high_fidelity = sphere
    solver = Mock()
    solver.results.x = [1, 1, 1, 1]
    solver.x_init = [0.5, 0.5, 0.5, 0.5]
    solver.results.fun = 0.123
    trust_region = Mock()
    trust_region.delta = 0.2
    trust_region.rho = 0.5
    surrogate = Mock()
    surrogate.evaluate = sphere
    return Results(simulation, solver, surrogate, trust_region)


def test_instance_created(results):
    """ Test if the instance class was created."""
    assert results is not None


def test_evaluate_fobj_star(results):
    """ Test evaluate objective function star."""
    fobj_start = results.evaluate_fobj_star()
    true = sphere([1, 1, 1, 1])
    assert fobj_start == true


def test_evaluate_fobj_center(results):
    """ Test evaluate objective function center."""
    fobj_center = results.evaluate_fobj_center()
    true = sphere([0.5, 0.5, 0.5, 0.5])
    assert fobj_center == true


def test_evaluate_fap_star(results):
    """ Test the value of the approximate function
    in the optimal point."""
    true = 0.123
    eva = results.evaluate_fap_star()
    assert true == eva
