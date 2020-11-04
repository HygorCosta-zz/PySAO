""" Save the results along the optimization. """
import pandas as pd


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
