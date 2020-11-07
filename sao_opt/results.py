""" Save the results along the optimization. """
import pandas as pd


class AppendResults:

    """Append the results and save."""

    def __init__(self):
        self.count = []
        self.fob_center = []
        self.fob_star = []
        self.fap_center = []
        self.fap_star = []
        self.x_center = []
        self.x_star = []
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

    def update_count(self):
        """ Add counter."""
        if not self.count:
            self.count.append(1)
        else:
            self.count.append(self.count[-1] + 1)

    def update_fobj(self, fobj):
        """ Append objective function."""
        self.fob_center.append(fobj[0])
        self.fob_star.append(fobj[1])
        self.fap_center.append(fobj[2])
        self.fap_star.append(fobj[3])

    def update_x_center(self, x_center):
        """ Append x_center. """
        self.x_center.append(x_center)

    def update_x_star(self, x_star):
        """ Append x_center. """
        self.x_star.append(x_star)

    def update_delta(self, delta):
        """ Append delta. """
        self.delta.append(delta)

    def update_pho(self, pho):
        """ Update rho."""
        self.pho.append(pho)


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
        self._solver = solver
        self._surrogate = surrogate
        self._trust_region = trust_region

    @property
    def solver(self):
        """Getter solver."""
        return self._solver

    @solver.setter
    def solver(self, new_solver):
        """ Setter solver. """
        self._solver = new_solver

    @property
    def surrogate(self):
        """ Getter surrogate."""
        return self._surrogate

    @surrogate.setter
    def surrogate(self, new_surrogate):
        """ Setter surrogate."""
        self._surrogate = new_surrogate

    @property
    def trust_region(self):
        """ Getter trust_region."""
        return self.trust_region

    @trust_region.setter
    def trust_region(self, new_region):
        """ Setter trust_region."""
        self._trust_region = new_region

    def evaluate_fobj_star(self):
        """ Evaluate the x in the high fidelity model."""
        x_star = self.solver.results.x
        return self.simulation.high_fidelity(x_star)

    def evaluate_fobj_center(self):
        """ Evaluate x in the center of the trust region. """
        x_center = self.solver.x_init
        return self.simulation.high_fidelity(x_center)

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
        self.update_x_star(self.solver.result.x)
        self.update_delta(self.trust_region.delta)
        self.update_pho(self.trust_region.rho)
        self.update_count()
        self.describe()
