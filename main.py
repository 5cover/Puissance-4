# main.py
# Point d'entrée du programme

from config import *
from entree import *
from sortie import AfficherGrille
from alignements import ChercherAlignement, ObtenirLigneDisponible

""" Boucle principale du programme """
def main():
    jouerAvecPC = DemanderJouerAvecOrdinateur()
    nomJoueur1 = DemanderNomJoueur1()
    nomJoueur2 = "Ordinateur" if jouerAvecPC else DemanderNomJoueur2() # condition ternaire

    colonneDernierTour = 0
    ligneDernierTour = 0

    while not ChercherAlignement(colonneDernierTour, ligneDernierTour):
        pass



main()