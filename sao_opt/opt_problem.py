""" Optimization problem to be solved."""
import yaml
import numpy as np
from scipy.optimize import LinearConstraint, Bounds
from PyMEX.utilits import ParallelPyMex


class Simulation:

    """ Reservoir parameters for simulation."""

    def __init__(self):
        """ Reservoir parameters."""
        self.res_param = self.reservoir_parameters()
        self.nominal = self.x_nominal()

    @staticmethod
    def reservoir_parameters():
        """ Return the reservoir configuration."""
        with open('../PyMEX/reservoir_config.yaml') as file:
            res_param = yaml.load(file, Loader=yaml.FullLoader)
        return res_param

    def x_nominal(self):
        """ Determine the nominal controls for the wells. """

        def _prod_nom(res_param):
            """ Producer norm max plat."""
            plat_prod = res_param["max_plat_prod"]
            prod_rate = res_param["max_rate_prod"]
            nb_prod = res_param["nb_prod"]
            prod_total = prod_rate * nb_prod
            x_prod = plat_prod / prod_total
            if x_prod > 1:
                x_prod = 1
            return x_prod

        def _inj_nom(res_param):
            """ Producer norm max plat."""
            plat_inj = res_param["max_plat_inj"]
            inj_rate = res_param["max_rate_inj"]
            nb_inj = res_param["nb_inj"]
            inj_total = inj_rate * nb_inj
            x_inj = plat_inj / inj_total
            if x_inj > 1:
                x_inj = 1
            return x_inj

        nb_prod = self.res_param["nb_prod"]
        nb_inj = self.res_param["nb_inj"]
        nom_prod = _prod_nom(self.res_param)
        nom_inj = _inj_nom(self.res_param)
        return np.repeat([nom_prod, nom_inj], [nb_prod, nb_inj])

    def run(self, controls):
        """ Return the npv for the controls."""
        model = ParallelPyMex(controls, self.res_param)
        return model.pool_pymex()

    def high_fidelity(self, controls):
        """High fidelity model."""
        pool_size = self.res_param["pool_size"]
        model = ParallelPyMex(controls, self.res_param, pool_size)
        return model.pool_pymex()


class OptimizationProblem:

    """The basic elements of the reservoir problem."""

    def __init__(self, res_param):
        """Returns the npv of the controls.

        Parameters
        ----------
        controls: array
            Wells rate.

        """
        self.opt_param = self.opt_parameters()
        self.ite_max = self.opt_param["ite_max"]
        self.bounds = self.bounds_constr(res_param)
        self.linear = self.linear_const(res_param)
        self.delta = self.opt_param["delta"]
        self.ite_max_sao = self.opt_param["ite_max_sao"]
        self.tol_opt = self.opt_param["tol_opt"]
        self.tol_delta = self.opt_param["tol_delta"]

    @staticmethod
    def opt_parameters():
        """ Return the reservoir configuration."""
        with open('../PyMEX/opt_config.yaml') as file:
            res_param = yaml.load(file, Loader=yaml.FullLoader)
        return res_param

    @staticmethod
    def _create_matrix(res_param):
        """ Create matrix A for linear constraint."""
        nb_prod = res_param["nb_prod"]
        nb_inj = res_param["nb_inj"]
        prod = np.repeat([1, 0], [nb_prod, nb_inj])
        inj = np.repeat([0, 1], [nb_prod, nb_inj])
        return [prod, inj]

    @staticmethod
    def get_upper(res_param):
        """ Get the upper linear constraint."""

        def _prod_norm(res_param):
            """ Producer norm max plat."""
            plat_prod = res_param["max_plat_prod"]
            prod_rate = res_param["max_rate_prod"]
            return plat_prod / prod_rate

        def _inj_norm(res_param):
            """ Producer norm max plat."""
            plat_inj = res_param["max_plat_inj"]
            inj_rate = res_param["max_rate_inj"]
            return plat_inj / inj_rate

        prod = _prod_norm(res_param)
        inj = _inj_norm(res_param)
        return [prod, inj]

    @staticmethod
    def bounds_constr(res_param):
        """ Create bound constraints."""
        size = res_param["nb_prod"] + res_param["nb_inj"]
        lower = np.zeros((size, 1))
        upper = np.ones((size, 1))
        return Bounds(lower, upper)

    def linear_const(self, res_param):
        """ Linear constraints for optimization problem."""

        if "max_plat_prod" in res_param:
            lower = [0, 0]
            upper = self.get_upper(res_param)
            matrix = self._create_matrix(res_param)
            return LinearConstraint(matrix, lower, upper)
        return None
