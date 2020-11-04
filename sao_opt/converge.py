""" Converge class."""
import numpy as np


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
