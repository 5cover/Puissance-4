# alignements.py
# Fonctions cherchant des alignements sur la grille

from config import *

""" 
Cherche un alignement gagnant � l'emplacement du derni� pion plac�.
Retourn True si un alignement a �t� trouv�, sinon False
"""
def ChercherAlignement(colonne, ligne, joueur):

    vertical = True
    horizontal = True
    diagonaleGaucheDroite = True
    diagonaleDroiteGauche = True

    for offset in range(LONGUEUR_ALIGNEMENT):

        for voisin in range(-offset, LONGUEUR_ALIGNEMENT - offset):
            horizontal            = grille[colonne + voisin][ligne]          == joueur and horizontal
            vertical              = grille[colonne]         [ligne + voisin] == joueur and vertical
            diagonaleGaucheDroite = grille[colonne + voisin][ligne + voisin] == joueur and diagonaleGaucheDroite
            diagonaleDroiteGauche = grille[colonne - voisin][ligne - voisin] == joueur and diagonaleDroiteGauche

    return vertical or horizontal or diagonaleGaucheDroite or diagonaleDroiteGauche

""" Retourne la ligne de la case vide la plus basse � la colonne sp�cifi�e, ou -1 si la colonne n'a aucune ligne vide. """
def ObtenirLigneDisponible(colonne):
    for ligne in reversed(range(HAUTEUR)):
        if grille[colonne][ligne] == Case.VIDE:
            return ligne
    return -1

 