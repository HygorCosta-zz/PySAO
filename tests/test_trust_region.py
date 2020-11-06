""" Test the trust region algorithm. """
import pytest
import numpy as np
from sao_opt.opt_problem import OptimizationProblem, Simulation
from sao_opt.trust_region import TrustRegion


@pytest.fixture(name="trust_region")
def fix_trust_region():
    """ Create a instance of the TrustRegion class."""
    problem = OptimizationProblem()
    simulation = Simulation()
    return TrustRegion(simulation.nominal, problem)


def test_init_x_center(trust_region):
    """ Verify initial attributes."""
    assert trust_region.x_center is not None
    assert len(trust_region.x_center) == 24
    assert trust_region.x_center[0] < 1


def test_init_lower(trust_region):
    """ Test initial lower."""
    eva = trust_region.lower
    true = 12*[0]
    assert np.array_equiv(eva, true)


def test_init_upper(trust_region):
    """ Test initial upper."""
    eva = trust_region.upper
    true = 12*[1]
    assert np.array_equiv(eva, true)


def test_update_lower(trust_region):
    """ Test initial lower."""
    breakpoint()
    trust_region.update_bounds()
    eva = trust_region.lower
    true = trust_region.x_center - 0.1
    assert np.array_equiv(eva, true)


def test_update_upper(trust_region):
    """ Test initial upper."""
    trust_region.update_bounds()
    eva = trust_region.upper
    true = trust_region.x_center + 0.1
    assert np.array_equiv(eva, true)
