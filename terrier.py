class Terrier:
    def __init__(self, positions_terriers,riviere):
        self.positions_terriers=self.creer_terrier(positions_terriers, riviere)

    #On fait une fonction qui créer les terriers en dehors de l'eau
    def creer_terrier(selfself,positions_terriers,riviere):
        positions=[]
        for (x,y) in positions_terriers:
            if not riviere.dans_riviere(x,y): #les terriers ne doivent pas être dans la rivière
                positions.append((x,y))
        return positions

    # On fait une fonction qui dit si un couple (x,y) est dans un terrier
    def dans_terrier(self, x, y):
        if (x,y) in self.positions_terriers:
            return True
        else:
            return False
