""" Tests for Sequence class."""
from unittest.mock import Mock
from pytest_mock import mocker
import pytest
import numpy as np
from sao_opt.sequence import Sequence


def sphere(design_var):
    """ Evalute design_var in sphere function."""
    return np.sum(np.power(design_var, 2))


@pytest.fixture(name='trust_region')
def fix_trust_region():
    """ Create a mock class for trust_region."""
    trust_region = Mock()
    trust_region.lower = np.array([-5.12, -5.12, -5.12, -5.12, -5.12])
    trust_region.upper = np.array([5.12, 5.12, 5.12, 5.12, 5.12])
