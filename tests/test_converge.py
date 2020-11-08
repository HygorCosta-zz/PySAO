""" Test the Converge class. """
from unittest.mock import Mock
import pytest
from sao_opt.converge import Converge


@pytest.fixture(name='results_false')
def fix_results_false():
    """ Mock results class."""
    results = Mock()
    results.fob_star = [0.4, 0.3, 0.2, 0.1, 0.05, 0.01]
    results.count = [1, 2, 3, 4, 5, 6]
    results.delta = [0.2, 0.2, 0.3, 0.1, 0.1, 0.1]
    return results


@pytest.fixture(name='results_true')
def fix_results_true():
    """ Mock results class."""
    results = Mock()
    results.fob_star = [0.4, 0.3, 0.01, 0.01, 0.01, 0.01]
    results.count = [1, 2, 3, 4, 5, 51]
    results.delta = [0.2, 0.2, 0.3, 0.1, 0.1, 0.00001]
    return results


@pytest.fixture(name='problem')
def fix_problem():
    """ Mock problem class. """
    problem = Mock()
    problem.tol_opt = 1e-5
    problem.tol_delta = 1e-2
    problem.iter_max = 50
    return problem


@pytest.fixture(name='converge_false')
def fix_converge_false(results_false, problem):
    """ Create a instance class."""
    return Converge(results_false, problem)


@pytest.fixture(name='converge_true')
def fix_converge_true(results_true, problem):
    """ Create a instance class."""
    return Converge(results_true, problem)


def test_create_instance(converge_false):
    """ Test if the istance was created."""
    assert converge_false is not None


def test_create_flag(converge_false):
    """ Test if the istance was created."""
    assert converge_false.flag == []
    assert not converge_false.converge


def test_converge_to_local_optima(converge_false):
    """ Test if the local optima converged is
    returned False."""
    assert not converge_false.converge_to_local_optima()


def test_converge_to_local_optima_true(converge_true):
    """ Test if the local optima converged is
    returned False."""
    assert converge_true.converge_to_local_optima()


def test_stop_region_false(converge_false):
    """ Test if stop region method is converged."""
    converge_false.converge_delta()
    assert not converge_false.converge


def test_stop_region_true(converge_true):
    """ Test if stop region method is converged."""
    converge_true.converge_delta()
    assert converge_true.converge


def test_converge_delta(converge_false):
    """ Test if converge delta is False."""
    converge_false.converge_delta()
    assert not converge_false.converge


def test_converge_delta_true(converge_true):
    """ Test if converge delta is True."""
    converge_true.converge_delta()
    assert converge_true.converge


def test_max_iter_false(converge_false):
    """ Test if iter max is False."""
    converge_false.max_iter()
    assert not converge_false.converge


def test_max_iter_true(converge_true):
    """ Test if iter max is True."""
    converge_true.max_iter()
    assert converge_true.converge


def test_call_function(converge_false):
    """ Test if call function return False."""
    assert not converge_false()


def test_call_function_true(converge_true):
    """ Test if call function return True."""
    assert converge_true()
