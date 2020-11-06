""" Test the Design of Experiments classes."""
import pytest
import numpy as np
from sao_opt.doe import RandomDoE


@pytest.fixture(name="doe")
def fix_doe():
    """ Instance of the RandomDoE class."""
    lower = np.array([0.5] * 24)
    upper = np.array([0.9] * 24)
    return RandomDoE(lower, upper)


def test_dim(doe):
    """ Verify dimension value."""
    assert doe.dim == 24


def test_num_samples(doe):
    """ Verify dimension value."""
    assert doe.num_samples == 47


def test_samples(doe):
    """ Test samples values."""
    assert doe.samples.shape == (47, 24)


def test_samples_upper(doe):
    """ Test if the samples in less the upper value."""
    assert (doe.samples < 0.9).all()


def test_samples_upper_false(doe):
    """ Test if the samples in less the upper value."""
    assert not (doe.samples < 0.6).all()


def test_samples_lower(doe):
    """ Test if the samples in less the upper value."""
    assert (doe.samples > 0.5).all()


def test_samples_lower_false(doe):
    """ Test if the samples in less the upper value."""
    assert not (doe.samples > 0.8).all()


def test_min_values_setter(doe):
    """ Test min values setter."""
    doe.min_values = np.array([0.6] * 24)
    assert (doe.samples > 0.6).all()


def test_min_values_setter_false(doe):
    """ Test min values setter."""
    doe.min_values = np.array([0.6] * 24)
    assert not (doe.samples < 0.6).all()


def test_max_values_setter(doe):
    """ Test max values setter."""
    doe.max_values = np.array([0.7] * 24)
    assert (doe.samples < 0.7).all()


def test_max_values_setter_false(doe):
    """ Test max values setter."""
    doe.max_values = np.array([0.7] * 24)
    assert not (doe.samples > 0.7).any()
