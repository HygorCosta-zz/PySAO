""" Create surrogate model for SAO. """
from scipy.interpolate import Rbf


class Surrogate:

    """Create the surrogate model."""

    def __init__(self, input_vars, output_vars, option=None):
        """Surrogate model.

        Parameters
        ----------
        input_vars: array
            Input variables.
        output_vars: array
            Output variables.


        """
        self._input_vars = input_vars
        self._output_vars = output_vars
        self.option = option

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

    def build_approximation(self, method):
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
            return method(*self.input_vars.T, self.output_vars,
                          self.option)
        return method(*self.input_vars.T, self.output_vars)


class RadialBasisSurrogate(Surrogate):

    """Radial Basis Surrogate. """

    def __init__(self, input_train, output_train,
                 func='cubic'):
        super().__init__(input_train, output_train, func)
        self.model = self.build_approximation(Rbf)

    def evaluate(self, input_vars):
        """ Evaluate the input variables and return the
        approximate value.

        Parameters
        ----------
        input_vars: array
            The same number of dimensions of the input_train.
        """
        return self.model(*input_vars.T)

    def update(self):
        """ Update the model."""
        self.model = self.build_approximation(Rbf)
