""" Moviment Limit Strategys."""
import numpy as np


class TrustRegion:

    """Create and update a trust region for optimization."""

    def __init__(self, x_center, problem):
        """Create the Trust region.

        Parameters
        ----------
        x_center: array
            Central point.
        delta: array
            Length of the trust region in relation of the search space.
        lower: array
            Lower limit of the search space.
        upper: array
            Upper limit of the search space.

        """
        self.x_center = x_center
        self.delta = problem.delta
        self.pho = []
        self.lower = problem.lower
        self.upper = problem.upper

    def update_bounds(self):
        """ Find the new search region."""
        space = self.upper - self.lower
        new_lower = self.x_center - space * self.delta / 2
        if np.any(new_lower < self.lower):
            ind = new_lower < self.lower
            new_lower[ind] = self.lower[ind]
        new_upper = self.x_center - space * self.delta / 2
        if np.any(new_upper < self.upper):
            ind = new_upper > self.upper
            new_upper[ind] = self.upper[ind]
        self.lower = new_lower
        self.upper = new_upper

    def update_search_region(self, results):
        """ Update the values of x_center, delta and ro.

        Parameters
        ----------
        fobj: float
            High fidelity objetive function value in the center and
            optimal point of the trust region.
        fap: float
            Approximate objetive function value in the center of the
            trust region.
        x_center: array
            Position of the center point.
        x_start: array
            Positio of the optimal point.

        Returns
        -------
        new_x_center: array
            New position for the center of the trust region.
        new_delta: array
            New delta value.
        ro: float
            Term of accept.

        """
        f_center = results.fob_center[-1]
        f_star = results.fob_star[-1]
        fap_center = results.fap_center[-1]
        fap_star = results.fap_star[-1]
        x_center = results.x_center[-1]
        x_star = results.x_star[-1]

        if (f_center - f_star) == 0 and (fap_center - fap_star) == 0:
            self.pho = 0
        else:
            self.pho = (f_center - f_star) / (fap_center - fap_star)

        if self.pho <= 0:
            self.x_center = x_center
            self.delta = 0.5 * self.delta
        elif 0 < self.pho <= 0.25:
            self.x_center = x_star
            self.delta = 0.5 * self.delta
        elif (0.25 < self.pho < 0.75) or self.pho > 1.25:
            self.x_center = x_star
        elif 0.75 <= self.pho <= 1.25:
            self.x_center = x_star
            self.delta = 1.5 * self.delta
