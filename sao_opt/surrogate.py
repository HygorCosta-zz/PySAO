""" Create surrogate model for SAO. """
import numpy as np
from scipy.interpolate import Rbf
from scipy.spatial import distance
from .doe import RandomDoE


class RadialBasisSurrogate():

    """Radial Basis Surrogate. """

    def __init__(self):
        self._input_vars = []
        self._output_vars = []
        self.option = None
        self.model = []

    @property
    def input_vars(self):
        """ Getter for input."""
        return self._input_vars

    @input_vars.setter
    def input_vars(self, new_input):
        """ Setter input_vars."""
        self._input_vars = new_input

    @property
    def output_vars(self):
        """ Getter for output."""
        return self._output_vars

    @output_vars.setter
    def output_vars(self, new_output):
        """ Setter for output."""
        self._output_vars = new_output

    def __call__(self, design_var):
        """ Evaluate the input variables and return the
        approximate value.

        Parameters
        ----------
        input_vars: array
            The same number of dimensions of the input_train.
        """
        return self.model(*design_var.T)

    def build_model(self):
        """ Interpolated values.

        Parameters
        ----------
        method: type of approximation.

        Returns
        -------
        int_value: array
            Interpolated values from the input variables.
        """
        if self.option is not None:
            self.model = Rbf(*self.input_vars.T,
                             self.output_vars,
                             function=self.option)
        self.model = Rbf(*self.input_vars.T, self.output_vars)

    def update(self, func, new_lb, new_ub):
        """ Update the model.

        Parameters
        ----------
        func: method
            Function to evaluate the samples.
        new_lb: array-like Lower boundaries.
        new_ub: array-like
            Upper boundaries.
        """
        doe = RandomDoE(new_lb, new_ub)
        output = func(doe.samples)
        self.input_vars = doe.samples
        self.output_vars = output
        self.build_model()


class RbfPoly:

    """Radial Basis with polynomial tail."""

    def __init__(self, doe):
        self.doe = doe
        self._input_vars = []
        self._output_vars = []
        self.num_samples = []
        self.dim = []
        self.lamb = []
        self.gamma = []

    @property
    def input_vars(self):
        """ Getter for input."""
        return self._input_vars

    @input_vars.setter
    def input_vars(self, new_input):
        """ Setter input_vars."""
        self._input_vars = new_input

    @property
    def output_vars(self):
        """ Getter for output."""
        return self._output_vars

    @output_vars.setter
    def output_vars(self, new_output):
        """ Setter for output."""
        self._output_vars = new_output

    def samples_dim(self):
        """ Get the number of samples and dimension
        of the problem."""
        self.num_samples, self.dim = self.input_vars.shape

    def euclid_distance(self):
        """ Return the euclidian distance between all samples."""
        samples = self.input_vars
        return distance.cdist(samples, samples)

    def get_phi(self):
        """ Get phi value for cubic RBF."""
        dist = self.euclid_distance()
        return np.power(dist, 3)

    def get_p(self):
        """ Get P matrix."""
        ones = np.ones((self.num_samples, 1))
        return np.hstack((self.input_vars, ones))

    def get_a_matrix(self):
        """ Get matrix A for rbf."""
        phi = self.get_phi()
        p_matrix = self.get_p()
        zeros = np.zeros((self.dim + 1, self.dim + 1))
        row1 = np.hstack((phi, p_matrix))
        row2 = np.hstack((p_matrix.T, zeros))
        return np.vstack((row1, row2))

    def get_rhs(self):
        """ Get Rhs matrix for rbf."""
        zeros = np.zeros((self.dim + 1, ))
        return np.hstack((self.output_vars, zeros))

    def model(self):
        """ Solve the linear system."""
        self.samples_dim()
        matrix_a = self.get_a_matrix()
        matrix_rhs = self.get_rhs()
        inv_a = np.linalg.pinv(matrix_a)
        params = inv_a.dot(matrix_rhs)
        self.lamb = params[:self.num_samples]
        self.gamma = params[self.num_samples:]

    def update(self, func):
        """ Update the model.

        Parameters
        ----------
        func: method
            Function to evaluate the samples.
        new_lb: array-like
            Lower boundaries.
        new_ub: array-like
            Upper boundaries.
        """
        output = func(self.doe.samples)
        self.input_vars = self.doe.samples
        self.output_vars = output
        self.model()

    def __call__(self, new_points):
        """ Predict the value in new_points."""
        if new_points.ndim == 1:
            new_points = new_points.reshape(1, -1)
        dist = distance.cdist(new_points, self.input_vars)
        nsam = new_points.shape[0]
        # Cubic RBF
        phi = np.power(dist, 3)
        yest_1 = phi.dot(self.lamb)
        matrix_x = np.hstack((new_points, np.ones((nsam, 1))))
        yest_2 = matrix_x.dot(self.gamma)
        return yest_1 + yest_2
