import numpy as np

class Herbe:
    def __init__(self, x_lim, y_lim):
        self.herbe = np.zeros((x_lim, y_lim))
        self.herbe[0][3] = 0.8  #Un point particulier a plus d'herbe que les autres

    def pousse_herbe(self, taux):
        self.herbe = np.minimum(self.herbe + taux, np.ones_like(self.herbe))
