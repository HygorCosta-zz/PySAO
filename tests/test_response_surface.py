""" Test for responde surface res_surf."""

import pytest
import numpy as np
from sao_opt.doe import ResponseSurface


@pytest.fixture(name="res_surf")
def fix_response_surface():
    """ Instance of the RandomDoE class."""
    lower = np.array([0.5] * 24)
    upper = np.array([0.9] * 24)
    return ResponseSurface(lower, upper)


def test_dim(res_surf):
    """ Verify dimension value."""
    assert res_surf.dim == 24


def test_num_samples(res_surf):
    """ Verify dimension value."""
    assert res_surf.num_samples == 47


def test_samples(res_surf):
    """ Test samples values."""
    dim_res = 46 * res_surf.dim + 1
    assert res_surf.samples.shape == (dim_res, 24)


def test_samples_upper(res_surf):
    """ Test if the samples in less the upper value."""
    assert (res_surf.samples <= 0.9).all()


def test_samples_upper_false(res_surf):
    """ Test if the samples in less the upper value."""
    assert not (res_surf.samples < 0.6).all()


def test_samples_lower(res_surf):
    """ Test if the samples in less the upper value."""
    assert (res_surf.samples >= 0.5).all()


def test_samples_lower_false(res_surf):
    """ Test if the samples in less the upper value."""
    assert not (res_surf.samples > 0.8).all()


def test_min_values_setter(res_surf):
    """ Test min values setter."""
    res_surf.min_values = np.array([0.6] * 24)
    assert (res_surf.samples >= 0.6).all()


def test_min_values_setter_false(res_surf):
    """ Test min values setter."""
    res_surf.min_values = np.array([0.6] * 24)
    assert not (res_surf.samples < 0.6).all()


def test_max_values_setter(res_surf):
    """ Test max values setter."""
    res_surf.max_values = np.array([0.7] * 24)
    assert (res_surf.samples <= 0.7).all()


def test_max_values_setter_false(res_surf):
    """ Test max values setter."""
    res_surf.max_values = np.array([0.7] * 24)
    assert not (res_surf.samples > 0.7).any()
