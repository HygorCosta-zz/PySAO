""" Test the trust region algorithm. """
from unittest.mock import Mock
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


@pytest.fixture(name="problem")
def fix_problem():
    """ Create a instance of the class."""
    return OptimizationProblem()


@pytest.fixture(name="mock_results_0")
def fix_mock_results_0(problem):
    """ Create a mock class to replace results."""
    resul = Mock()
    resul.count = [1]
    resul.fob_center = [-39.32]
    resul.fob_star = [-39.32]
    resul.fap_center = [-35.98]
    resul.fap_star = [-35.98]
    resul.x_center = problem.nominal
    resul.x_star = [problem.nominal[0] - 0.2]
    return resul


@pytest.fixture(name="mock_results_pho_1")
def fix_mock_results_pho_1(problem):
    """ Create a mock class to replace results."""
    resul = Mock()
    resul.count = [1]
    resul.fob_center = [-20]
    resul.fob_star = [-40]
    resul.fap_center = [-25]
    resul.fap_star = [-125]
    resul.x_center = problem.nominal[0]
    resul.x_star = [problem.nominal[0] - 0.2]
    return resul


@pytest.fixture(name="mock_results_pho_2")
def fix_mock_results_pho_2(problem):
    """ Create a mock class to replace results."""
    resul = Mock()
    resul.count = [1]
    resul.fob_center = [-20]
    resul.fob_star = [-40]
    resul.fap_center = [-25]
    resul.fap_star = [-65]
    resul.x_center = problem.nominal[0]
    resul.x_star = [problem.nominal[0] - 0.2]
    return resul


@pytest.fixture(name="mock_results_pho_3")
def fix_mock_results_pho_3(problem):
    """ Create a mock class to replace results."""
    resul = Mock()
    resul.count = [1]
    resul.fob_center = [-20]
    resul.fob_star = [-40]
    resul.fap_center = [-25]
    resul.fap_star = [-35]
    resul.x_center = problem.nominal[0]
    resul.x_star = [problem.nominal[0] - 0.2]
    return resul


@pytest.fixture(name="mock_results_pho_4")
def fix_mock_results_pho_4(problem):
    """ Create a mock class to replace results."""
    resul = Mock()
    resul.count = [1]
    resul.fob_center = [-20]
    resul.fob_star = [-40]
    resul.fap_center = [-25]
    resul.fap_star = [-42]
    resul.x_center = problem.nominal[0]
    resul.x_star = [problem.nominal[0] - 0.2]
    return resul


def test_init_x_center(trust_region):
    """ Verify initial attributes."""
    assert trust_region.x_center is not None
    assert len(trust_region.x_center) == 24
    assert trust_region.x_center[0] < 1


def test_init_lower(trust_region):
    """ Test initial lower."""
    eva = trust_region.lower
    true = 24*[0]
    assert np.array_equiv(eva, true)


def test_init_upper(trust_region):
    """ Test initial upper."""
    eva = trust_region.upper
    true = 24*[1]
    assert np.array_equiv(eva, true)


def test_update_lower(trust_region):
    """ Test initial lower."""
    trust_region.update_bounds()
    eva = trust_region.lower
    true = trust_region.x_center - 0.1
    assert np.array_equal(eva, true)


def test_update_upper(trust_region):
    """ Test initial upper."""
    trust_region.update_bounds()
    eva = trust_region.upper
    true = trust_region.x_center + 0.1
    assert np.array_equal(eva, true)


def test_update_search_region_mock(trust_region, mock_results_0,
                                   problem):
    """ Test update of the search region."""
    trust_region.update_search_region(mock_results_0)
    assert trust_region.pho == 0
    assert np.array_equal(trust_region.x_center, problem.nominal[0])
    assert trust_region.delta == 0.1


def test_update_search_region_mock_pho_1(trust_region, mock_results_pho_1,
                                         problem):
    """ Test update of the search region."""
    trust_region.update_search_region(mock_results_pho_1)
    assert trust_region.pho == 0.2
    assert np.array_equal(trust_region.x_center,
                          problem.nominal[0] - 0.2)
    assert trust_region.delta == 0.1


def test_update_search_region_mock_pho_2(trust_region, mock_results_pho_2,
                                         problem):
    """ Test update of the search region."""
    trust_region.update_search_region(mock_results_pho_2)
    assert trust_region.pho == 0.5
    assert np.array_equal(trust_region.x_center,
                          problem.nominal[0] - 0.2)
    assert trust_region.delta == 0.2


def test_update_search_region_mock_pho_3(trust_region, mock_results_pho_3,
                                         problem):
    """ Test update of the search region."""
    trust_region.update_search_region(mock_results_pho_3)
    assert trust_region.pho == 2
    assert np.array_equal(trust_region.x_center,
                          problem.nominal[0] - 0.2)
    assert trust_region.delta == 0.2


def test_update_search_region_mock_pho_4(trust_region, mock_results_pho_4,
                                         problem):
    """ Test update of the search region."""
    trust_region.update_search_region(mock_results_pho_4)
    assert trust_region.pho < 1.25
    assert np.array_equal(trust_region.x_center,
                          problem.nominal[0] - 0.2)
    assert trust_region.delta == pytest.approx(0.3)
