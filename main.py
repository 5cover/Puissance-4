# main.py
# Point d'entrée du programme

from config import *
from entree import ChoisirJoueurs
from sortie import AfficherGrille
from alignements import ChercherAlignement

def PlacerPion(colonne, joueur):
    for ligne in range(HAUTEUR-1, 0, -1):
        if grille[colonne][ligne] == Case.VIDE:
            grille[colonne][ligne] = joueur
            break

ChoisirJoueurs()
AfficherGrille()
PlacerPion(2, Case.JOUEUR_1)
ChercherAlignement(2, Case.JOUEUR_1)
AfficherGrille()
