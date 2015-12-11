#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


    def certificatCorrecte(self,certificatPizza) :
        """Complexité de l'algorithme en O(2*h*l)
            pour le moment ne verifie pas si ça sort de la pizza
        """
        matriceBool = []
        for ligne in self.matrice: 
            matriceBool.append([False]*len(self.matrice[0]))              
        for part in  certificatPizza.listePart: 
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
        lesDimensions = []
        largeur = len(self.matrice[0])
        hauteur = len(self.matrice)
        for i in range(self.c+1) :
            for j in range(self.c+1) :
                if self.n <= i * j <= self.c :
                    lesDimensions.append((i,j))
        for y in range(hauteur) :
            for x in range(largeur) :
                for (i,j) in lesDimensions :
                    cptJambon = 0 
                    if not (((y + j - 1) >= hauteur) or ((x + i - 1) >= largeur) ):
                        for xi in range(i) :
                            for yj in range(j):
                                if self.matrice[y+yj][x+xi] == 'H' :
                                    cptJambon += 1
                        if cptJambon >= self.n :
                            lesParts.append(Part(x,y,i,j))
        return lesParts


    def solutionAlea(self, liste):
        '''
        solution de la question 3.1.2
        '''
        listePart = []
        r.shuffle(liste)
        matriceBool = []
        #Matrice des déjà pris
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


matricePizza = [['T','T','T','T','T'],['T','H','H','H','T'],['T','T','T','T','T']]
petitePizza = PizzaProbleme(matricePizza,6,1)
part1 = Part(0,0,2,3) 
part2 = Part(2,0,1,3)
part3 = Part(3,0,2,3)
certificat = CertificatPizza([part1,part2,part3])
# print "test certificatCorrecte : ", petitePizza.certificatCorrecte(certificat)
print "test toutesLesParts, ", len(petitePizza.toutesLesParts())