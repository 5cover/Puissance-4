# main.py
# Point d'entrée du programme

from random import randint
from config import *
from entree import *
from sortie import AfficherCestAuTourDe, AfficherGrille
from alignements import ChercherAlignement, ObtenirLigneDisponible

def JouerTour(nomJoueur, joueur):

    AfficherCestAuTourDe(nomJoueur)

    ligne = ERREUR_COLONNE_PLEINE
    while ligne == ERREUR_COLONNE_PLEINE:
        colonne = DemanderColonne()
        ligne = ObtenirLigneDisponible(colonne)
        

    grille[colonne][ligne] = joueur

    return ChercherAlignement(colonne, ligne)

def JouerTourAuto(nomJoueur, joueur):

    AfficherCestAuTourDe(nomJoueur)

    randLigne = ERREUR_COLONNE_PLEINE

    while randLigne == ERREUR_COLONNE_PLEINE:
            randColonne = randint(0, LARGEUR-1)
            randLigne = ObtenirLigneDisponible(randColonne)

    grille[randColonne][randLigne] = joueur

""" Boucle principale du programme """
def Main():

    jouerAvecPC = DemanderJouerAvecPC()
    nomJoueur1 = DemanderNomJoueur1()
    nomJoueur2 = "Ordinateur" if jouerAvecPC else DemanderNomJoueur2() # condition ternaire

    AfficherGrille()

    # Tant qu'aucun des deux joueurs n'a gagné
    while True:

        if JouerTour(nomJoueur1, Case.JOUEUR_1):
            break
        AfficherGrille()

        if jouerAvecPC:
            if JouerTourAuto(nomJoueur2, Case.JOUEUR_2):
                break
        elif JouerTour(nomJoueur2, Case.JOUEUR_2):
            break
        AfficherGrille()

    AfficherGrille()

Main()