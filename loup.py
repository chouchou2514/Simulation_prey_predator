import random
import numpy as np
import matplotlib.pyplot as plt
from animal import Animal
from lapin import Lapin
import constante as ct
from rivière import Riviere
from terrier import Terrier

class Loup(Animal):
    def __init__(self, x, y,energie,age):
        super().__init__(x, y,energie,age)

    # On fait une fonction qui définit le déplacement du loup
    def deplacement(self,riviere,terriers,lapins):

        lapin_le_plus_proche = self.trouver_lapin_proche(lapins)

        if lapin_le_plus_proche:
            dx = lapin_le_plus_proche.x - self.x
            dy = lapin_le_plus_proche.y - self.y

        else:
            # Définition du pas en fonction de la position du loup
            pas_x = [0, 1] if self.x == 0 else [-1, 0] if self.x == 29 else [-1, 0, 1]
            pas_y = [0, 1] if self.y == 0 else [-1, 0] if self.y == 29 else [-1, 0, 1]

            dx = random.choice(pas_x)
            dy = random.choice(pas_y)

        # On vérifie que le déplacement n'emmène pas le loup dans l'eau
        if riviere.dans_riviere(self.x + dx, self.y + dy)==False and terriers.dans_terrier(self.x+dx,self.y+dy)==False:
            self.x += dx
            self.y += dy
            self.energie -= ct.energie_depla_loup #Perte d'énergie

    #On fait une fonction qui permet de trouver le lapin le plus proche d'un loup
    def trouver_lapin_proche(self,lapins):
        lapin_proche=None
        distance_minimale= 1 #les loups vont vers les lapins seulement si ils sont à une case d'eux
        for lapin in lapins:
            distance = abs(self.x-lapin.x)+ abs(self.y - lapin.y)
            if distance<= distance_minimale:
                distance_minimale= distance
                lapin_proche = lapin
        return lapin_proche



    # On fait une fonction qui permet aux loups de se reproduire sur la même case
    def reproduction(self, predateur_population):
        if self.energie > ct.energie_repro_loup and ct.age_repro_max_loup > self.age > ct.age_repro_min_loup: #Conditions : avoir une énergie minimale et avoir un âge particulier
            for autre_loup in predateur_population:
                if autre_loup.energie > ct.energie_repro_loup and ct.age_repro_max_loup > autre_loup.age > ct.age_repro_min_loup:
                    if autre_loup is not self and autre_loup.x == self.x and autre_loup.y == self.y:  # les deux loups sont au meme endroit

                        #On impose une probabilité pour la reproduction des loups
                        chance_louveteau = random.uniform(0, 1)
                        if chance_louveteau <0.45:
                            pass
                        else:
                            nouveau_loup = Loup(self.x, self.y, energie=4, age=0)

                            autre_loup.energie -= ct.perte_repro_loup #Perte d'énergie
                            self.energie -= ct.perte_repro_loup

                            return nouveau_loup

    #On fait une fonction qui fait disparaitre les loups
    def mort_loup(self,predateur_population):
        if self.energie < ct.energie_min_loup or self.age > ct.age_max_loup: #Conditions : âge maximal ou énergie minimale
            predateur_population.remove(self)

    # On crée une fonction qui permet aux lapins de se nourrir
    def nourriture(self, proie_population,terriers):
        if self.energie <ct.energie_manger_loup: #Conditions : il y a de l'herbe et le lapin a faim
            for proie in proie_population:
                if self.x== proie.x and self.y == proie.y and not terriers.dans_terrier(self.x,self.y): #le lapin et le loup sont sur la même case
                                                                                                        # et le lapin n'est pas dans un terrier

                    #On impose une probabilité pour l'alimentation des loups
                    chance_manger = random.uniform(0, 1)
                    if chance_manger <= 0.4: #on diminue la chance des loups de manger car les lapins les fuient
                        proie_population.remove(proie)
                        self.energie += ct.gain_manger_loup #Gain d'énergie avec l'alimentation




