""" Join all the class for optimization. """
import pandas as pd
import warnings
import numpy as np
from .opt_problem import OptimizationProblem
from .surrogate import RadialBasisSurrogate
from .solver import TrustConstrSolver
from .trust_region import TrustRegion


class Converge:

    """Docstring for Converge. """

    def __init__(self, results, problem):
        """TODO: to be defined.

        Parameters
        ----------
        results: Results()
            instance of the Results class.

        """
        self.results = results
        self.problem = problem
        self.flag = []
        self.converge = False

    def converge_to_local_optima(self):
        """ Mean the optima value in the last 4 iterations."""
        last_star = self.results.fob_star[-1]
        mean_start = np.mean(self.results.fob_star[-4:])
        dif = mean_start - last_star
        if dif < self.problem.tol_opt:
            return True
        return False

    def stop_region(self):
        """ Verify if the optimization stop in a local
        optima."""
        if self.results.count[-1] > 5 and \
                self.converge_to_local_optima():
            self.flag = 1
            print("SAO convergiu = Parado nas últimas 5 rodadas.")
            self.converge = True
        else:
            self.converge = False

    def converge_delta(self):
        """ Verify if the delta converge."""
        count = self.results.count[-1]
        delta = self.results.delta[-1]
        tol_delta = self.problem.tol_delta
        if count > 1 and delta < tol_delta:
            self.flag = 2
            print("Parado devido a pequena região de confiança.")
            self.converge = True
        else:
            self.converge = False

    def max_iter(self):
        """ Verify if the max iter was achieved."""
        ite = self.results.count[-1]
        iter_max = self.problem.iter_max
        if ite >= iter_max:
            self.flag = 3
            print("Num max de iterações do SAO.")
            self.converge = True
        else:
            self.converge = False

    def is_true(self):
        """ Verify all kinds of converge."""
        if self.stop_region():
            return True
        if self.converge_delta():
            return True
        if self.max_iter():
            return True
        return False


class Results:

    """Docstring for Results. """

    def __init__(self):
        """TODO: to be defined.

        Parameters
        ----------
        Docstring for Results. : TODO


        """
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

    def update(self, fobj, x_center, delta, pho):
        """ Update all optimization values."""
        self.update_fobj(fobj)
        self.update_x_center(x_center)
        self.update_delta(delta)
        self.update_rho(pho)
        self.describe()


class Sequence:

    """Main class of the framework."""

    def __init__(self, problem, doe, trust_region, surrogate):
        """
        Parameters
        ----------
        doe: RandomDoe()
            instance of the class RandomDoe.
        surrogate: RadialBasisSurrogate()
            instance of the class RadialBasisSurrogate.
        opt_solver: TrustConstrSolver
            instance of the class TrustConstrSolver.
        strategy: TrustRegion()
            instance of the class TrustRegion.

        """
        self.problem = problem
        self.doe = doe
        self.trust_region = trust_region
        self.surrogate = surrogate
        self.cont = 0
        self.results = Results()

    def sequence(self):
        """ Apply optimization sequence. """
        converge = Converge(self.results, self.problem)

        x_init = self.problem.nominal
        bound = self.problem.bounds
        lcons = self.problem.linear

        while not converge.is_true():

            solver = TrustConstrSolver(self.surrogate.evaluate,
                                       x_init, bound, lcons)
            result = solver.maximize_npv()
            # Trust Region

            # Create init samples
            samples = self.doe.samples

            # Evaluate in high fidelity model.
            samples_output = self.problem.high_fidelity(samples)

            # Create the surrogate model.
            surrogate = RadialBasisSurrogate(samples, samples_output)

            # Set optimization solver.
            ite_max = self.opt_problem.ite_max
            bound = self.opt_problem.bounds
            lcons = self.opt_problem.linear
            x_init = self.opt_problem.nominal

            # Optimum values
            if result.sucess:
                print("Successfully optimization.")
                x_star = result.x
                f_star = result.f
            else:
                warnings.warn("Optimization not exited successfully.")

            # Trust Region strategy
