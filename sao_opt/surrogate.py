""" Create surrogate model for SAO. """
from scipy.interpolate import Rbf
from .doe import RandomDoE


class RadialBasisSurrogate():

    """Radial Basis Surrogate. """

    def __init__(self, input_train, output_train,
                 func='cubic'):
        self._input_vars = input_train
        self._output_vars = output_train
        self.option = func
        self.model = []
        self.build_model()

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
        new_lb: array-like
            Lower boundaries.
        new_ub: array-like
            Upper boundaries.
        """
        doe = RandomDoE(new_lb, new_ub)
        output = func(doe.samples)
        self.input_vars = doe.samples
        self.output_vars = output
        self.build_model()
