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
    def __init__(self, x, y, largeur, hauteur, nbJambon=-1):
        super(Part, self).__init__()
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.nbJambon = nbJambon

        
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
        test = True
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
                            lesParts.append(Part(x,y,i,j,cptJambon))
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
        return (listePart, self.score(matriceBool))

    def score(self,matriceBool):
        cpt = 0
        for ligne in matriceBool :
            for case in ligne :
                if case :
                    cpt = cpt + 1
        return cpt

    def ecritSolution(self, listePart) :
        fichier = open('resultat.out','w')
        fichier.write(str(len(listePart))+'\n')
        for part in listePart :
            chaine = str(part.y) + ' ' + str(part.x) + ' ' + str(part.y + part.hauteur - 1) + ' ' + str(part.x + part.largeur - 1) + '\n'
            fichier.write(chaine)
        fichier.close()

            
    def aleaIteration(self,listePart, iteration) :
        bestScore = 0
        bestListePart = []
        for i in range(iteration) :
            print i
            (newListePart,score) = self.solutionAlea(listePart)
            if score > bestScore :
                bestScore = score
                bestListePart = newListePart
        self.ecritSolution(bestListePart)
        print 'score : ', score

    def separerListePosition(self,listePart) :
        '''transforme une liste de parts en liste de liste par position'''
        matriceLists = []
        for ligne in self.matrice:
            matriceLists.append([[]]*len(self.matrice[0]))
        for part in listePart :
            matriceLists[part.y][part.x].append(part)
        for ligne in matriceLists :
            for liste in ligne :
                r.shuffle(liste)
        return matriceLists 


    def solutionGlouton(self,listePart,comparateur) :
        '''parcourir toute la pizza et deposer une a une les parts'''
        r.shuffle(listePart)
        listePart.sort(cmp=comparateur)
        listeFinale = []
        matriceBool = []
        #Matrice des déjà pris
        for ligne in self.matrice: 
            matriceBool.append([False]*len(self.matrice[0]))
        for part in listePart :
            peutCouper = True
            for x in range(part.largeur) :
                for y in range(part.hauteur) :
                    if matriceBool[part.y + y][part.x + x] :
                        peutCouper = False
            if peutCouper :
                for x in range(part.largeur) :
                    for y in xrange(part.hauteur) :
                        matriceBool[y+part.y][x+part.x] = True
                listeFinale.append(part)
        print len(listeFinale)
        return (listeFinale,self.score(matriceBool))

def comparateur(part1, part2):
    if part1.y > part2.y :
        return -1
    elif part1.y < part2.y :
        return 1
    elif part1.x > part2.x :
        return -1
    elif part1.x < part2.x :
        return 1
    else :
        return 0

def comparateur2(part1,part2):
    taille1 = part1.largeur * part1.hauteur
    taille2 = part2.largeur * part2.hauteur
    if taille1/part1.nbJambon > taille2/part2.nbJambon :
        return -1
    elif taille1/part1.nbJambon < taille2/part2.nbJambon :
        return 1
    else :
        return 0

def comparateur3(part1,part2):
    taille1 = part1.largeur * part1.hauteur
    taille2 = part2.largeur * part2.hauteur
    if taille1 > taille2 :
        return -1
    elif taille2 > taille1 :
        return 1
    else :
        if part1.nbJambon < part2.nbJambon :
            return -1
        elif part1.nbJambon > part2.nbJambon :
            return 1
        else :
            return 0

def creerPizzaDepuisFichier(filename) :
    f = open(filename, 'r')
    premiereLigne = True
    matrice = []
    c = 12
    n = 3
    for ligne in f :
        line = []
        if premiereLigne :
            #je vais faire un truc degueux car une seule instance du probleme
            premiereLigne = False
        else :
            for char in ligne :
                if char != '\n' :
                    line.append(char)
        if line != [] :
            matrice.append(line)
    f.close()
    return PizzaProbleme(matrice,c,n)


grossePizza = creerPizzaDepuisFichier('data.in')
toutesLesParts = grossePizza.toutesLesParts()
print "test toutesLesParts, ", len(toutesLesParts)
(listePart , score) = grossePizza.solutionAlea(toutesLesParts)
print 'score random: ', score
# grossePizza.aleaIteration(toutesLesParts,1000)
(listePart,score) = grossePizza.solutionGlouton(toutesLesParts,comparateur)
print 'score glouton simple: ', score

(listePart,score) = grossePizza.solutionGlouton(toutesLesParts,comparateur2)
print 'score glouton perso: ', score

(listePart,score) = grossePizza.solutionGlouton(toutesLesParts,comparateur3)
print 'score glouton perso 2: ', score