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

    def __init__(self, func, ite_max, opt_constr=None):
        self.func = func
        self.ite_max = ite_max
        self.opt_constr = opt_constr

    def solve_problem(self, x_init, bound):
        """ Solve the optimiziation problem."""
        if self.opt_constr is not None:
            lcons = self.opt_constr.lcons
        else:
            bound = None
            lcons = None
        return minimize(self.func, x_init, method='trust-constr',
                        bounds=bound, constraints=lcons)
