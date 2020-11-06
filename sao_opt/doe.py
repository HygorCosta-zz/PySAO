""" Create a class for design experiments in SAO. """
from pyDOE import lhs, bbdesign


class DoE:

    """Design of Experiments."""

    def __init__(self, min_values=0, max_values=1):
        """Create a sample.

        Parameters
        ----------
        dim: int
            Number of dimensions.
        min_values: np-array
            Minimum value in each dimension.
        max_values: np-array
            Maximium value in each dimension.
        criterion: str
            Criterion to sample the points.

        """
        self._min_values = min_values
        self._max_values = max_values
        self.dim = len(min_values)
        self.num_samples = 2 * self.dim - 1

    @property
    def min_values(self):
        """ Getter for lower."""
        return self._min_values

    @min_values.setter
    def min_values(self, new_lower):
        """ Setter for lower."""
        self._min_values = new_lower

    @property
    def max_values(self):
        """ Getter for upper."""
        return self._max_values

    @max_values.setter
    def max_values(self, new_upper):
        """ Setter for upper."""
        self._max_values = new_upper

    def get_delta(self):
        """Get delta value for each dimension.

        Returns
        -------
        Delta interval for each dimension space.
            Array - (num_dim, 1)

        """
        return self.max_values - self.min_values

    def determine_plan_points(self, norm_points):
        """Determine the sample points.

        Returns
        -------
        Array: (num_samples, dim)

        """
        init = self.min_values
        delta = self.get_delta()
        return init + delta * norm_points


class RandomDoE(DoE):

    """Random points for design experiments."""

    def __init__(self, min_values, max_values):
        """Points created by random methods."""
        super().__init__(min_values, max_values)

    @property
    def samples(self):
        """ Update the samples. """
        return self.determine_plan_points(self.lhs_points())

    def lhs_points(self):
        """Latin Hypercube Samples.

        Returns
        -------
        np.array - (num_samples, num_dim)

        """
        return lhs(self.dim, self.num_samples)


class ResponseSurface(DoE):

    """ Response Surface Designs from PyDOE."""

    def __init__(self, min_values, max_values):
        super().__init__(min_values, max_values)

    @property
    def samples(self):
        """ Update the samples. """
        return self.determine_plan_points(self.bb_points())

    def bb_points(self):
        """Box-Behnken designs."""
        return (bbdesign(self.dim, 1) + 1) * 0.5
