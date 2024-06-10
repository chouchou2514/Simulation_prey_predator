import random
import numpy as np
import matplotlib.pyplot as plt
from animal import Animal
from herbe import Herbe
import constante as ct
from rivière import Riviere

class Lapin(Animal):
    def __init__(self, x, y,energie,age):
        super().__init__(x, y,energie,age)

    #On fait une fonction qui définit le déplacement du lapin
    def deplacement(self,riviere):
        #Définition du pas en fonction de la position du lapin
        pas_x = [0, 1] if self.x == 0 else [-1, 0] if self.x == 29 else [-1, 0, 1]
        pas_y = [0, 1] if self.y == 0 else [-1, 0] if self.y == 29 else [-1, 0, 1]

        dx = random.choice(pas_x)
        dy = random.choice(pas_y)

        #On vérifie que le déplacement n'emmène pas le lapin dans l'eau
        if riviere.dans_riviere(self.x + dx, self.y + dy) == False:
            self.x += dx
            self.y += dy
            self.energie -= ct.energie_depla_lapin #Perte d'énergie

    #On fait une fonction qui permet aux lapins de se reproduire sur la même case
    def reproduction(self, proie_population):
        if self.energie > ct.energie_repro_lapin and self.age> ct.age_repro_lapin: #Conditions : avoir une énergie minimale et avoir un âge particulier
            for autre_lapin in proie_population:
                if autre_lapin.energie > ct.energie_repro_lapin and autre_lapin.age> ct.age_repro_lapin:
                    if autre_lapin is not self and autre_lapin.x == self.x and autre_lapin.y == self.y: #les deux lapins sont au meme endroit
                        nouveau_lapin = Lapin(self.x, self.y,energie=4,age=0)

                        autre_lapin.energie -= ct.perte_repro_lapin #Perte d'énergie
                        self.energie -= ct.perte_repro_lapin

                        return nouveau_lapin

    #On crée une fonction qui fait disparaitre les lapins
    def mort_lapin(self,proie_population):
        if self.energie <ct.energie_min_lapin or self.age > ct.age_max_lapin: #Conditions : âge maximal ou énergie minimale
                proie_population.remove(self)

    #On crée une fonction qui permet aux lapins de se nourrir
    def nourriture(self, herbe):
        if herbe[self.y][self.x] > 0 and self.energie < ct.energie_manger_lapin: #Conditions : il y a de l'herbe et le lapin a faim
            self.energie += ct.gain_manger_lapin #Gain d'énergie
            herbe[self.y][self.x] = max(0,herbe[self.y][self.x] - ct.perte_herbe_lapin) #Réduction de la quantité d'herbe sur la case