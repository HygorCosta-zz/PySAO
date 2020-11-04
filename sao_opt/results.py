""" Save the results along the optimization. """
import pandas as pd
from sao_opt.opt_problem import Simulation


class AppendResults:

    """Append the results and save."""

    def __init__(self):
        self.count = []
        self.fob_center = []
        self.fob_star = []
        self.fap_center = []
        self.fap_star = []
        self.x_center = []
        self.delta = []
        self.pho = []

    def describe(self):
        """ Create a file to describe the optimization
        evolution."""
        datas = {
            'fobj_center': self.fob_center,
            'fobj_start': self.fob_star,
            'fap_center': self.fap_center,
            'fap_star': self.fap_star,
            'x_center': self.x_center,
            'delta': self.delta,
            'pho': self.pho
        }
        dframe = pd.DataFrame(datas)
        dframe.to_csv("../results.out")

    def update_count(self, count):
        """ Add counter."""
        self.count.append(count)

    def update_fobj(self, fobj):
        """ Append objective function."""
        self.fob_center.append(fobj[0])
        self.fob_star.append(fobj[1])
        self.fap_center.append(fobj[2])
        self.fap_star.append(fobj[3])

    def update_x_center(self, x_center):
        """ Append x_center. """
        self.x_center.append(x_center)

    def update_delta(self, delta):
        """ Append delta. """
        self.delta.append(delta)

    def update_rho(self, rho):
        """ Update rho."""
        self.pho.append(rho)


class Results(AppendResults):

    """Results of the simulation."""

    def __init__(self, simulation, solver, surrogate, trust_region):
        """Results from high fidelity model, surrogate model,
        delta and rho.

        Parameters
        ----------
        simulation: instance of Simulation()


        """
        super().__init__()
        self.simulation = simulation
        self.solver = solver
        self.surrogate = surrogate
        self.trust_region = trust_region

    def evaluate_fobj_star(self):
        """ Evaluate the x in the high fidelity model."""
        x_star = self.solver.results.x
        return self.simulation.high_fidelity(x_star)

    def evaluate_fobj_center(self):
        """ Evaluate x in the center of the trust region. """
        x_center = self.solver.x_init
        return self.simulation.high(x_center)

    def evaluate_fap_star(self):
        """ Optimal point in the surrogate model."""
        return self.solver.results.fun

    def evaluate_fap_center(self):
        """ Surrogate value for x_center."""
        x_center = self.solver.x_init
        return self.surrogate.evaluate(x_center)

    def fobj_list(self):
        """ Create a list of fobj and fap."""
        fobj_star = self.evaluate_fobj_star()
        fobj_center = self.evaluate_fobj_center()
        fap_star = self.evaluate_fap_star()
        fap_center = self.evaluate_fap_star()
        return [fobj_star, fobj_center, fap_star, fap_center]

    def update(self):
        """ Update the results."""
        self.update_fobj(self.fobj_list())
        self.update_x_center(self.solver.x_init)
        self.update_delta(self.trust_region.delta)
        self.update_rho(self.trust_region.rho)
        self.describe()
