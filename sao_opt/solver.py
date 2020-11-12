""" Numerical Solver for the optimization problem."""
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, minimize


class OptConstraints:

    """Parent class for all optimization solvers."""

    def __init__(self, bound=None, lmatrix=None, bmatrix=None):
        """

        Parameters
        ----------
        x0: array
            Initial value of the design variables.
        ite_max: int
            Maximum number of iterations.
        bound: array
            Bound constraints [lower, upper]
            lower <= x <= upper
        lmatrix: array
            Matrix of linear constraints.
        bmatrix: array
            Matrix for the bounds of the linear constraint.

        """
        self.bound = self.bound_const(bound)
        self.lcons = self.linear_constraint(lmatrix, bmatrix)

    @staticmethod
    def bound_const(bound):
        """ Defining bound constraints.

        Returns
        -------
        bound: instance of Bound class for scipy.

        """
        return Bounds(bound[0], bound[1])

    @staticmethod
    def linear_constraint(matrix, upper, lower=None):
        """ Defining the linear constraints.

        lower <= A * x <= upper

        Returns
        -------
        matrix: array
            Square matrix with values for multiply the design
            variables. (ndim, ndim)
        upper: array
            Linear upper constraint.
        lower: array
            Linear lower constraint.

        """
        if matrix is None:
            return None

        if lower is None:
            lower = np.zeros_like(upper)
        return LinearConstraint(matrix, lower, upper)


class TrustConstrSolver:

    """Trust region constraint algorith for scipy."""

    def __init__(self, lcons=None):
        self.lcons = lcons
        self._func = []
        self._x_init = []
        self._bound = []
        self.result = []

    @property
    def func(self):
        """ Getter for the func."""
        return self._func

    @func.setter
    def func(self, method):
        """ Setter for the func."""
        self._func = method

    @property
    def x_init(self):
        """ Getter for the x initial."""
        return self._x_init

    @x_init.setter
    def x_init(self, value):
        """ Setter for the x initial."""
        self._x_init = value

    @property
    def bound(self):
        """ Getter for bound constraint."""
        return self._bound

    @bound.setter
    def bound(self, new_bound):
        self._bound = Bounds(*new_bound)

    def maximize_npv(self):
        """ Solve the optimiziation problem."""
        if self.lcons:
            self.result = minimize(self.func,
                                   self.x_init,
                                   method='trust-constr',
                                   bounds=self.bound,
                                   constraints=self.lcons)
        else:
            self.result = minimize(self.func,
                                   self.x_init,
                                   method='trust-constr',
                                   bounds=self.bound)
