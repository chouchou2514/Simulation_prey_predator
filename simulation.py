import random
import numpy as np
import matplotlib.pyplot as plt
from animal import Animal
from lapin import Lapin
from herbe import Herbe
from loup import Loup
from rivière import Riviere
from terrier import Terrier
import constante as ct


class Simulation:

    def __init__(self, riviere, terriers_positions, x_lim, y_lim, nb_proies, nb_predateurs):
        #On définit la taille de l'environnement, l'herbe, les terriers et la rivère
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.riviere = riviere
        self.terriers = Terrier(terriers_positions, riviere)
        self.herbe = Herbe(x_lim, y_lim)

        #On définit les populations à l'aide de la fonction initialiser_population
        self.proie_population = self.initialiser_population(Lapin, nb_proies)
        self.predateur_population = self.initialiser_population(Loup, nb_predateurs)

        #On définit les autres constantes nécessaires aux graphiques
        self.global_plot = self.set_plot()
        self.herbe_qte = []
        self.proie_pop_size = []
        self.predateur_pop_size = []

    #On fait une fonction qui initialise les populations
    def initialiser_population(self, ClasseAnimal, nombre):
        population = []
        while len(population) < nombre:
            x, y = random.randint(0, 29), random.randint(0, 29)
            if not self.riviere.dans_riviere(x, y):  #les animaux ne doivent pas naitre dans la rivière
                population.append(ClasseAnimal(x, y, 10, random.randint(0, 20)))
        return population

    def set_plot(self, width=25.6, height=13.3):
        """Initialize plot with two empty subplots.

        Args:
            width (float, optional): Width of the plot. Defaults to 25.6 (suits for 2560*1440 screen).
            height (float, optional): Height of the plot. Defaults to 13.3 (suits for 2560*1440 screen).

        Returns:
            tuple: First element of tuple is the figure container. Second element of the tuple is a tuple with the two
            subplots.
        """
        return plt.subplots(1, 2, figsize=(width, height))

    def update_plot(self):
        """Update 2D environment plot and population line plot.

        Args:
            global_plot (tuple): Tuple with the figure container and a tuple with the two subplots.
            grass (array): Numpy array representing the environment.
            grass_qty (list): List with grass quantity for each step of the simulation.
            prey_population (list): List of individuals. Each individual is a dictionary with at least 'x' and 'y' keys.
            prey_pop_size (list): List of number of individuals for each step.
            predator_population (list): List of individuals. Each individual is a dictionary with at least 'x' and 'y' keys.
            predator_pop_size (list): List of number of individuals for each step.
        """

        fig, (ax1, ax2) = self.global_plot

        # Plots
        ax1.cla()
        ax2.cla()

        #Création de la rivière initiale de valeurs nulles
        riviere_init = np.zeros((self.x_lim, self.y_lim))
        for (x, y) in self.riviere.positions_riviere:
            riviere_init[y, x] = 1  #les matrices sont à l'envers donc on inverse x et y

        #Afficher la rivière en bleu et l'herbe en vert
        ax1.imshow(self.herbe.herbe, cmap='Greens', vmin=0, vmax=1)  #grass dans la classe herbe
        ax1.imshow(riviere_init, cmap='Blues', alpha=0.7)

        # On crée les listes des positions des terriers et on les place
        terriers_x = []
        terriers_y = []
        for (x, y) in self.terriers.positions_terriers:
            terriers_x.append(x)
            terriers_y.append(y)
        ax1.scatter(terriers_x, terriers_y, color='saddlebrown', marker='s', s=160,label='Terriers')

        #On crée les listes des positions des proies et on les place
        proies_x = []
        proies_y = []
        for lapin in self.proie_population:
            proies_x.append(lapin.x)
            proies_y.append(lapin.y)
        ax1.scatter(proies_x, proies_y, color='b', marker=6,label='Lapins')

        #On crée les listes des positions des prédateurs et on les place
        predateurs_x = []
        predateurs_y = []
        for loup in self.predateur_population:
            predateurs_x.append(loup.x)
            predateurs_y.append(loup.y)
        ax1.scatter(predateurs_x, predateurs_y, color='r', marker=7,label='Loups')

        ax1.legend(loc='upper right', bbox_to_anchor=(0, 1)) #bbox_to_anchor=(0, 1) place la légende à droite et au-dessus de l'axe
        ax1.set_title('Environnement')

        #On place les points sur le graphique des courbes
        ax2.plot(self.herbe_qte, color='g',label ='Herbe')
        ax2.plot(self.proie_pop_size, color='b', label= 'Lapins')
        ax2.plot(self.predateur_pop_size, color='r', label='Loups')

        ax2.legend(loc= 'upper left')
        ax2.set_title('Evolution des populations')

        self.herbe_qte.append((np.sum(self.herbe.herbe)))
        self.proie_pop_size.append(len(self.proie_population))
        self.predateur_pop_size.append(len(self.predateur_population))

        fig.canvas.flush_events()
        fig.canvas.draw()

        plt.pause(0.01)

    def run_simulation(self, taux):

        self.herbe_qte = [np.sum(self.herbe.herbe)]
        self.proie_pop_size = [len(self.proie_population)]
        self.predateur_pop_size = [len(self.predateur_population)]

        for s in range(5000):
            print(f'Step {s}')
            self.herbe.pousse_herbe(taux)

            #Boucles pour appeler les fonctions des lapins
            for lapin in self.proie_population:
                lapin.deplacement(self.riviere)

            for lapin in self.proie_population:
                lapin.nourriture(self.herbe.herbe)

            for lapin in self.proie_population:
                nouveau_lapin = lapin.reproduction(self.proie_population)
                if nouveau_lapin:
                    self.proie_population.append(nouveau_lapin)

            for lapin in self.proie_population:
                lapin.mort_lapin(self.proie_population)

            for lapin in self.proie_population:
                lapin.age += 1

            # Boucles pour appeler les fonctions des loups
            for loup in self.predateur_population:
                loup.deplacement(self.riviere, self.terriers, self.proie_population)

            for loup in self.predateur_population:
                loup.nourriture(self.proie_population, self.terriers)

            for loup in self.predateur_population:
                nouveau_loup = loup.reproduction(self.predateur_population)
                if nouveau_loup:
                    self.predateur_population.append(nouveau_loup)

            for loup in self.predateur_population:
                loup.mort_loup(self.predateur_population)

            for loup in self.predateur_population:
                loup.age += 1

            self.update_plot()

        plt.waitforbuttonpress()


if __name__ == "__main__":
    #random.seed(10)
    riviere = Riviere(x_debut=15, y_debut=2, longueur=26, direction='vertical')  #Position de la rivière
    terriers_positions = [(random.randint(0, 29), random.randint(0, 29)) for _ in range(15)]  # Positions des terriers
    simulation = Simulation(riviere, terriers_positions, x_lim=30, y_lim=30, nb_proies=130, nb_predateurs=40)
    simulation.run_simulation(ct.pousse_herbe)
