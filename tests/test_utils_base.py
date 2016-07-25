from numpy.testing import assert_array_almost_equal
import numpy as np

from pyriemann.utils.base import (sqrtm, invsqrtm, logm, expm, powm)


def test_sqrtm():
    """Test matrix square root"""
    C = 2*np.eye(3)
    Ctrue = np.sqrt(2)*np.eye(3)
    assert_array_almost_equal(sqrtm(C), Ctrue)


def test_invsqrtm():
    """Test matrix inverse square root"""
    C = 2*np.eye(3)
    Ctrue = (1.0/np.sqrt(2))*np.eye(3)
    assert_array_almost_equal(invsqrtm(C), Ctrue)


def test_logm():
    """Test matrix logarithm"""
    C = 2*np.eye(3)
    Ctrue = np.log(2)*np.eye(3)
    assert_array_almost_equal(logm(C), Ctrue)


def test_expm():
    """Test matrix exponential"""
    C = 2*np.eye(3)
    Ctrue = np.exp(2)*np.eye(3)
    assert_array_almost_equal(expm(C), Ctrue)


def test_powm():
    """Test matrix power"""
    C = 2*np.eye(3)
    Ctrue = (2**0.5)*np.eye(3)
    assert_array_almost_equal(powm(C, 0.5), Ctrue)
