""" Test AppendResults class."""
import pytest
import numpy as np
from sao_opt.results import AppendResults


@pytest.fixture(name='results')
def fix_results():
    """ Create a instance of the class AppendResults."""
    return AppendResults()


def test_create_instance(results):
    """ Verify if the instance is not None."""
    assert results is not None


def test_update_count(results):
    """ Test update counter."""
    results.update_count()
    assert np.array_equal(results.count, [1])
    results.update_count()
    assert np.array_equal(results.count, [1, 2])


def test_update_fobj(results):
    """ Test update for objective function."""
    fobj = [1, 2, 3, 4]
    results.update_fobj(fobj)
    assert np.array_equal(results.fob_center, [1])
    assert np.array_equal(results.fob_star, [2])
    assert np.array_equal(results.fap_center, [3])
    assert np.array_equal(results.fap_star, [4])
    fobj = [2, 3, 4, 5]
    results.update_fobj(fobj)
    assert np.array_equal(results.fob_center, [1, 2])
    assert np.array_equal(results.fob_star, [2, 3])
    assert np.array_equal(results.fap_center, [3, 4])
    assert np.array_equal(results.fap_star, [4, 5])


def test_update_x_center(results):
    """ Test update for x_center. """
    x_center = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results.update_x_center(x_center)
    assert np.array_equal(results.x_center[0], x_center)
    assert len(results.x_center) == 1
    x_center = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results.update_x_center(x_center)
    assert np.array_equal(results.x_center[0], x_center)
    assert np.array_equal(results.x_center[1], x_center)
    assert len(results.x_center) == 2


def test_update_x_star(results):
    """ Test update for x_center. """
    x_star = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results.update_x_star(x_star)
    assert np.array_equal(results.x_star[0], x_star)
    assert len(results.x_star) == 1
    x_star = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results.update_x_star(x_star)
    assert np.array_equal(results.x_star[0], x_star)
    assert np.array_equal(results.x_star[1], x_star)
    assert len(results.x_star) == 2


def test_update_delta(results):
    """ Test update delta. """
    delta = 0.5
    results.update_delta(delta)
    assert np.array_equal(results.delta, [0.5])
    delta = 0.2
    results.update_delta(delta)
    assert np.array_equal(results.delta, [0.5, 0.2])


def test_update_pho(results):
    """ Test update delta. """
    pho = 0.5
    results.update_pho(pho)
    assert np.array_equal(results.pho, [0.5])
    pho = 0.2
    results.update_pho(pho)
    assert np.array_equal(results.pho, [0.5, 0.2])
