# main.py
# Point d'entrée du programme

from random import randint
from config import *
from entree import *
from sortie import AfficherCestAuTourDe, AfficherGrille
from alignements import ChercherAlignement, ObtenirLigneDisponible

def JouerTour(nomJoueur, joueur):

    assert(joueur != Case.VIDE) # un joueur ne peut pas jouer une case vide (abscence de pion)

    AfficherCestAuTourDe(nomJoueur)

    ligne = ERREUR_COLONNE_PLEINE
    while ligne == ERREUR_COLONNE_PLEINE:
        colonne = DemanderColonne()
        ligne = ObtenirLigneDisponible(colonne)
        

    grille[colonne][ligne] = joueur

    return colonne,ligne

def JouerTourAuto(nomJoueur, joueur):

    AfficherCestAuTourDe(nomJoueur)

    randLigne = ERREUR_COLONNE_PLEINE

    while randLigne == ERREUR_COLONNE_PLEINE:
            randColonne = randint(0, LARGEUR-1)
            randLigne = ObtenirLigneDisponible(randColonne)

    grille[randColonne][randLigne] = joueur

    return randColonne,randLigne

""" Boucle principale du programme """
def Main():

    jouerAvecPC = DemanderJouerAvecPC()
    nomJoueur1 = DemanderNomJoueur1()
    nomJoueur2 = "Ordinateur" if jouerAvecPC else DemanderNomJoueur2() # condition ternaire

    AfficherGrille()

    # Boucle infine
    while True:

        (colonne, ligne) = JouerTour(nomJoueur1, Case.JOUEUR_1)

        AfficherGrille()

        if ChercherAlignement(colonne, ligne):
            break

        if jouerAvecPC:
            (colonne, ligne) = JouerTourAuto(nomJoueur2, Case.JOUEUR_2)
        else:
            (colonne, ligne) = JouerTour(nomJoueur2, Case.JOUEUR_2)
        
        AfficherGrille()

        if ChercherAlignement(colonne, ligne):
            break


Main()