""" Tests for surrogate model."""
import pytest
import numpy as np
from scipy.interpolate import Rbf
from sao_opt.surrogate import RadialBasisSurrogate


def sphere(input_value):
    """ Sphere function."""
    resul = []
    for array in input_value:
        resul.append(np.sum(np.power(array, 2)))
    return np.array(resul)


@pytest.fixture(name='rbf')
def fix_rbf():
    """ Create a RadialBasisSurrogate instance."""
    input_train = np.random.uniform(-5.12, 5.12, (47, 24))
    output = sphere(input_train)
    return RadialBasisSurrogate(input_train, output)


def test_create_class(rbf):
    """ Test if the class was created."""
    assert rbf is not None


def test_call(rbf):
    """ Test the output values."""
    input_eval = np.random.uniform(-5.12, 5.12, (10, 24))
    assert rbf(input_eval) is not None
    assert rbf(input_eval).shape == (10, )


def test_update(rbf):
    """ Test update function. """
    model1 = rbf.model
    lower = np.array([0.4]*24)
    upper = np.array([0.8]*24)
    rbf.update(sphere, lower, upper)
    model2 = rbf.model
    assert model1 is not model2
