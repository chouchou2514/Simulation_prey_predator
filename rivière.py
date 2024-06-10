class Riviere :
    def __init__(self,x_debut,y_debut,longueur,direction):
        self.x_debut=x_debut
        self.y_debut =y_debut
        self.longueur = longueur
        self.direction = direction
        self.positions_riviere = self.creer_riviere()

#On fait une fonction qui créer les positions de la rivière
    def creer_riviere(self):
        positions=[] #positions des points de la rivière
        if self.direction =='horizontal':
            for x in range(self.x_debut, self.x_debut + self.longueur):
                positions.append((x,self.y_debut))
        elif self.direction =='vertical':
            for y in range(self.y_debut, self.y_debut + self.longueur):
                positions.append((self.x_debut,y))
        return positions

#On fait une fonction qui dit si un couple (x,y) est dans la rivière
    def dans_riviere(self,x,y):
        if (x, y) in self.creer_riviere():
            return True
        else:
            return False
