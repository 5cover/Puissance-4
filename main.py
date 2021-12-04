# main.py
# Point d'entrée du programme
from config import *
from entree import *
from sortie import *
from alignements import *
from sys import exit 

def JouerTour(nomJoueur: str, joueur: Case):

    AfficherCestAuTourDe(nomJoueur)
    colonne = DemanderColonne()
    ligne = ObtenirLigneDePose(colonne)

    grille[colonne][ligne] = joueur

    AfficherGrille()

    QuitterSiGagnant(colonne, ligne, nomJoueur)

def JouerTourAuto(nomJoueur: str, joueur: Case):

    AfficherCestAuTourDe(nomJoueur)
    colonne = DemanderColonnePC()
    ligne = ObtenirLigneDePose(colonne)

    grille[colonne][ligne] = joueur

    AfficherGrille()

    QuitterSiGagnant(colonne, ligne, nomJoueur)

def QuitterSiGagnant(colonne: int, ligne: int, nomJoueur: str):
    if ChercherAlignement(colonne, ligne):
        AfficherMessageGagnant(nomJoueur)
        exit()

""" Boucle principale du programme """
def Main():

    jouerAvecPC = DemanderJouerAvecPC()
    nomJoueur1 = DemanderNomJoueur1()
    nomJoueur2 = "Ordinateur" if jouerAvecPC else DemanderNomJoueur2() # condition ternaire

    AfficherGrille()

    # Boucle principaele
    while True:
        
        if GrilleEstPleine():

            AfficherMessageMatchNul()
            exit()

        else:

            JouerTour(nomJoueur1, Case.JOUEUR_1)

            if jouerAvecPC:

                JouerTourAuto(nomJoueur2, Case.JOUEUR_2)

            else:

                JouerTour(nomJoueur2, Case.JOUEUR_2)

Main()