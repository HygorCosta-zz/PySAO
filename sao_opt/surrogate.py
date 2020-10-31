""" Create surrogate model for SAO. """
from scipy.interpolate import Rbf


class Surrogate:

    """Create the surrogate model."""

    def __init__(self, input_vars, output_vars, function="rbf",
                 option="multiquadratic"):
        """Surrogate model.

        Parameters
        ----------
        input_vars: array
            Input variables.
        output_vars: array
            Output variables.


        """
        self.input_vars = input_vars
        self.output_vars = output_vars
        self.function = function
        self.option = option

    def rbf_interpolator(self):
        """ Creat the rbf interpolator.

        Returns
        -------
        Rbf instance.

        """
        return Rbf(*self.input_vars.T, self.output_vars,
                   self.option)

    def inter_methods(self):
        """ Interpolate methods.

        Parameters
        ----------
        option: str
            Select among: RBF - radial basis function.
                          SVM - support vector machine.

        Returns
        -------
        Method.
        """
        methods = {"rbf": self.rbf_interpolator()}
        return methods[self.function]

    def build_approximation(self, inter_var):
        """ Interpolated values.

        Parameters
        ----------
        inter_var: array
            Variables to find the interpolated value.

        Returns
        -------
        int_value: array
            Interpolated values from the input variables.
        """
        return self.inter_methods()(*inter_var.T)
