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
        self.opt_param = self.opt_parameters()
        self.nominal = self.x_nominal()

    @staticmethod
    def reservoir_parameters():
        """ Return the reservoir configuration."""
        with open('../PyMEX/reservoir_config.yaml') as file:
            res_param = yaml.load(file, Loader=yaml.FullLoader)
        return res_param

    @staticmethod
    def opt_parameters():
        """ Return the reservoir configuration."""
        with open('../opt_config.yaml') as file:
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
        rate_cycle = np.repeat([nom_prod, nom_inj], [nb_prod, nb_inj])
        return [np.tile(rate_cycle, self.res_param["nb_cycles"])]

    def run(self, controls):
        """ Return the npv for the controls."""
        model = ParallelPyMex(controls, self.res_param)
        return model.pool_pymex()

    def high_fidelity(self, controls):
        """High fidelity model."""
        pool_size = self.opt_param["pool_size"]
        model = ParallelPyMex(controls, self.res_param, pool_size)
        return model.pool_pymex()


class OptimizationProblem(Simulation):

    """The basic elements of the reservoir problem."""

    def __init__(self):
        """Returns the npv of the controls.

        Parameters
        ----------
        controls: array
            Wells rate.

        """
        super().__init__()
        self.bounds = self.bounds_constr()
        self.linear = self.linear_const()
        self.delta = self.opt_param["delta"]
        self.ite_max = self.opt_param["ite_max"]
        self.ite_max_sao = self.opt_param["ite_max_sao"]
        self.tol_opt = self.opt_param["tol_opt"]
        self.tol_delta = self.opt_param["tol_delta"]

    def _create_matrix(self):
        """ Create matrix A for linear constraint."""
        nb_prod = self.res_param["nb_prod"]
        nb_inj = self.res_param["nb_inj"]
        num_cycles = self.res_param["nb_cycles"]
        nb_wells = nb_prod + nb_inj
        n_var = num_cycles * nb_wells
        matrix = np.zeros((2 * num_cycles, n_var))
        for i in range(2 * num_cycles):
            if (i % 2) == 0:
                # For producers
                start = int(i / 2 * nb_wells)
                stop = int(start + nb_prod)
                matrix[i, start: stop] = 1
            else:
                # For injectors
                start = int((i - 1) / 2 * nb_wells + nb_prod)
                stop = int(start + nb_inj)
                matrix[i, start:stop] = 1
        return matrix

    def get_upper(self):
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

        prod = _prod_norm(self.res_param)
        inj = _inj_norm(self.res_param)
        num_cycles = self.res_param["nb_cycles"]
        return np.tile([prod, inj], num_cycles)

    def bounds_constr(self):
        """ Create bound constraints."""
        size = self.res_param["nb_prod"] + self.res_param["nb_inj"]
        lower = np.zeros((size, 1))
        upper = np.ones((size, 1))
        return Bounds(lower, upper)

    def linear_const(self):
        """ Linear constraints for optimization problem."""

        if "max_plat_prod" in self.res_param:
            lower = [0, 0] * self.res_param["nb_cycles"]
            upper = self.get_upper()
            matrix = self._create_matrix()
            return LinearConstraint(matrix, lower, upper)
        return None
