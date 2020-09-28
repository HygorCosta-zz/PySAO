""" Create a class for design experiments in SAO. """
from pyDOE import lhs


class DoE:

    """Design of Experiments."""

    def __init__(self, dim, samples, min_values=0, max_values=1,
                 criterion='maximin'):
        """Create a sample.

        Parameters
        ----------
        dim: int
            Number of dimensions.
        samples: int
            Number of samples per dimension.
        min_values: np-array
            Minimum value in each dimension.
        max_values: np-array
            Maximium value in each dimension.
        criterion: str
            Criterion to sample the points.

        """
        self.dim = dim
        self.samples = samples
        self.min_values = min_values
        self.max_values = max_values
        self. criterion = criterion

    def get_delta(self):
        """Get delta value for each dimension.

        Returns
        -------
        Delta interval for each dimension space.
            Array - (num_dim, 1)

        """
        return self.max_values - self.min_values

    def lhs_points(self):
        """Latin Hypercube Samples.

        Returns
        -------
        np.array - (num_samples, num_dim)

        """
        return lhs(self.dim, self.samples, self.criterion)

    def determine_plan_points(self):
        """Determine the sample points.

        Returns
        -------
        Array: (num_samples, dim)

        """
        init = self.min_values
        delta = self.get_delta()
        normalized_points = self.lhs_points()
        return init + delta * normalized_points
