""" Tests for Simulation class."""
import pytest
from sao_opt.opt_problem import Simulation


@pytest.fixture(name="simulation")
def fix_simulation():
    """ Create instance of Simulation class."""
    return Simulation()


def test_reservoir_param_type(simulation):
    """ Verify reservoir param."""
    assert isinstance(simulation.res_param, dict)


def test_reservoir_param_path(simulation):
    """ Verify reservoir param."""
    path = simulation.res_param["path"]
    true = "/home/hygorcosta/Documentos/Phd/SAO/PyMEX/reservoir_tpl"
    assert path == true


def test_reservoir_param_prices(simulation):
    """ Verify reservoir param."""
    eva = simulation.res_param["prices"]
    true = [126, 19, 6, 0]
    assert eva == true


def test_reservoir_param_max_plat(simulation):
    """ Verify reservoir param."""
    eva = simulation.res_param["max_plat_prod"]
    true = 400
    assert eva == true


def test_len_nominal(simulation):
    """ Test nominal rate."""
    assert len(simulation.nominal) == 24


def test_high_fidelity(simulation):
    """ Test run high fidelity simulation."""
    breakpoint()
    eva = simulation.high_fidelity(simulation.nominal)
    assert eva is not None
