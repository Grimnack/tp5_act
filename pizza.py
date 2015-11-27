class CertificatPizza(object):
    """docstring for CertificatPizza"""
    def __init__(self, listePart):
        super(CertificatPizza, self).__init__()
        self.listePart = listePart[:]

class Part(object):
    """Objet part de pizza"""
    def __init__(self, x, y, largeur, hauteur):
        super(Part, self).__init__()
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

        
class PizzaProbleme(object):
    """docstring for PizzaProbleme"""
    def __init__(self, matrice, tailleMaxPart, nbJambon):
        super(PizzaProbleme, self).__init__()
        self.matrice = matrice[:]
        self.c = tailleMaxPart
        self.n = nbJambon


    def certificatCorrecte(CertificatPizza) :
        """Complexité de l'algorithme en O(2*h*l)"""
        matriceBool = []
        for ligne in self.matrice: 
            matriceBool.append([False]*len(self.matrice[0]))              
        for part in CertificatPizza : 
            cptJambon = 0
            if part.largeur * part.hauteur > self.c :
                return False 
            for l in range(part.largeur) : 
                for h in range(part.hauteur): 
                    if matriceBool[part.y + hauteur][part.x + largeur] 
                        return False
                    else :
                        matriceBool[part.y + hauteur][part.x + largeur] = True 
                        if self.matrice[part.y + hauteur][part.x + largeur] == 'H' : 
                            cptJambon = cptJambon + 1 
            if cptJambon < self.n : 
                return False
        return True

                        