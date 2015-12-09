import random as r

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


    def certificatCorrecte(self,CertificatPizza) :
        """Complexité de l'algorithme en O(2*h*l)
            pour le moment ne verifie pas si ça sort de la pizza
        """
        matriceBool = []
        for ligne in self.matrice: 
            matriceBool.append([False]*len(self.matrice[0]))              
        for part in CertificatPizza : 
            cptJambon = 0
            if part.largeur * part.hauteur > self.c :
                return False 
            for l in range(part.largeur) : 
                for h in range(part.hauteur): 
                    if matriceBool[part.y + h][part.x + l] :
                        return False
                    else :
                        matriceBool[part.y + h][part.x + l] = True 
                        if self.matrice[part.y + h][part.x + l] == 'H' : 
                            cptJambon = cptJambon + 1 
            if cptJambon < self.n : 
                return False
        return True

    def toutesLesParts(self) :
        """Génération de toutesLesParts
        parcours la pizza et a chaque point,
        crée les parts possibles depuis ce point"""
        lesParts = []
        lesDiviseurs = []
        for i in xrange(1,self.tailleMaxPart) :
            if tailleMaxPart % i == 0 :
                lesDiviseurs.append(i)
        for y in range(self.matrice) :
            for x in range(self.matrice[0]) :
                for diviseur in lesDiviseurs :
                    for yP in range(diviseur) :
                        cptJambon = 0
                        for xP in range(tailleMaxPart/diviseur) :
                            if self.matrice[y+yP][x + xP] == 'H' :
                                cptJambon = cptJambon + 1
                            if cptJambon >= self.n :
                                lesParts.append(Part((x+xP),(y+yP),(tailleMaxPart/diviseur),diviseur))
        return lesParts


    def solutionAlea(self, liste):
        '''
        solution de la question 3.1.2
        '''
        listePart = []
        r.shuffle(liste)
        matriceBool = []
        for ligne in self.matrice: 
            matriceBool.append([False]*len(self.matrice[0]))
        for part in liste :
            peutCouper = True
            for x in range(part.largeur) :
                for y in xrange(part.hauteur) :
                    if matriceBool[y+part.y][x+part.x] :
                        peutCouper = False
                if peutCouper :
                    for x in range(part.largeur) :
                        for y in xrange(part.hauteur) :
                            matriceBool[y+part.y][x+part.x] = True
                    listePart.append(part)
        return (listePart, matriceBool)

    def score(self,matriceBool):
        cpt = 0
        for ligne in matriceBool :
            for case in ligne :
                if case :
                    cpt = cpt + 1
        return cpt

    def genereFichierSolution(self, listePart):
        return True
            





def creerPizzaDepuisFichier(filename) :
    source = open(file, 'r')
    lignes = source.readline()
    


                        