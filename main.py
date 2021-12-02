# main.py
# Point d'entrée du programme
from config import *
from entree import *
from sortie import *
from alignements import *

""" Boucle principale du programme """
def Main():

    jouerAvecPC = DemanderJouerAvecPC()
    nomJoueur1 = DemanderNomJoueur1()
    nomJoueur2 = "Ordinateur" if jouerAvecPC else DemanderNomJoueur2() # condition ternaire

    AfficherGrille()

    # Boucle infine
    while True:

        AfficherCestAuTourDe(nomJoueur1) # Afficher tour

        derniereColonne = DemanderColonne() # Demande colonne
        derniereLigne = ObtenirLigneDePose(derniereColonne) # Obtenir ligne

        grille[derniereColonne][ObtenirLigneDePose(derniereColonne)] = Case.JOUEUR_1 # Placer le pion

        AfficherGrille() # Afficher la grille

        if ChercherAlignement(derniereColonne, derniereLigne): # Chercher un alignement
            break

        AfficherCestAuTourDe(nomJoueur2)

        derniereColonne = DemanderColonnePC() if jouerAvecPC else DemanderColonne()
        derniereLigne = ObtenirLigneDePose(derniereColonne)

        grille[derniereColonne][derniereLigne] = Case.JOUEUR_2

        AfficherGrille()

        if ChercherAlignement(derniereColonne, derniereLigne):
            break


Main()