""" Write importante information in Results file."""
import time
import csv


class WriteResults:

    """Write results in results.csv"""

    def __init__(self, time_spend, nfev, problem):
        """

        Parameters
        ----------
        time_spend: float
            Spend time during optimization in seconds.
        nfev: int
            Number of high fidelity functions evaluations.
        problem: instance of OptimizationProblem

        """
        self.time_spend = time_spend
        self.nfev = nfev
        self.problem = problem
        self.writer = None
        self.save_results()

    def time_in_hours(self):
        """ Get time value in hours.

        Returns
        -------
        Stream with time in hours, minutes and seconds.
        """
        elap_time = time.strftime('%H:%M:%S', time.gmtime(self.time_spend))
        self.writer.writerow([f"Time spend: {elap_time}"])

    def write_opt_options(self):
        """ Write opt options inside the results file."""
        for key, value in self.problem.opt_param.items():
            self.writer.writerow([key, value])
        self.writer.writerow(["\n"])

    def write_res_param(self):
        """ Write opt options inside the results file."""
        for key, value in self.problem.res_param.items():
            self.writer.writerow([key, value])
        self.writer.writerow(["\n"])

    def write_nfev(self):
        """ Write the number of high fidelity functions evaluations."""
        self.writer.writerow([f"Number HF fev: {self.nfev}"])

    def save_results(self):
        """ Save results."""
        with open('results.csv', 'a') as csv_file:
            self.writer = csv.writer(csv_file)
            self.time_in_hours()
            self.write_nfev()
            self.write_res_param()
            self.write_opt_options()
