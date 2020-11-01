""" Moviment Limit Strategys."""
import numpy as np


class TrustRegion:

    """Create and update a trust region for optimization."""

    def __init__(self, x_center, delta, lower, upper):
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
        self.delta = delta
        self.lower = lower
        self.upper = upper

    def determine_search_region(self):
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
        return new_lower, new_upper

    def update_search_region(self, fobj, fap, x_center, x_star):
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
        f_center, f_star = fobj
        fap_center, fap_star = fap
        if (f_center - f_star) == 0 and (fap_center - fap_star) == 0:
            pho = 0
        else:
            pho = (f_center - f_star) / (fap_center - fap_star)

        if pho <= 0:
            self.x_center = x_center
            self.delta = 0.5 * self.delta
        elif 0 < pho <= 0.25:
            self.x_center = x_star
            self.delta = 0.5 * self.delta
        elif (0.25 < pho < 0.75) or pho > 1.25:
            self.x_center = x_star
        elif 0.75 <= pho <= 1.25:
            self.x_center = x_star
            self.delta = 1.5 * self.delta
