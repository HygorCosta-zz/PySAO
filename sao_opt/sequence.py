""" Join all the class for optimization. """


class Sequence:

    """Main class of the framework."""

    def __init__(self, simulation, doe, trust_region, surrogate, solver,
                 converge, results):
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
        self.simulation = simulation
        self.doe = doe
        self.trust_region = trust_region
        self.surrogate = surrogate
        self.solver = solver
        self.converge = converge
        self.results = results

    def run(self):
        """ Apply optimization sequence. """

        while not self.converge.is_true():

            # Update lower and upper
            self.trust_region.update_bounds()
            new_lb = self.trust_region.lower
            new_ub = self.trust_region.upper

            # New Surrogate
            self.surrogate.update(new_lb, new_ub)

            # New solver parameters
            self.solver.bound = [new_lb, new_ub]

            # Optimize
            self.solver.maximize_npv()

            # Results update
            self.results.solver = self.solver
            self.results.surrogate = self.surrogate
            self.results.trust_region = self.trust_region
            self.results.update()

            # New center point and delta
            self.trust_region.update_search_region(self.results)
        print(" Optimization is finish.!! \n")
