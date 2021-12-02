# config.py
# Variables globales et configuration

from enum import Enum
from random import randint

# Représente les caractères de représentation d'une case.
# Il s'agit d'une énumération. Une variable de type Case peut prendre l'une de ces valeurs.
class Case(Enum):
    VIDE = '\0'
    JOUEUR_1 = '█'
    JOUEUR_2 = '░'

# Nombre de lignes de la grille
HAUTEUR = 6

# Nombre de colonnes de la grille
LARGEUR = 7

# Longueur d'un alignement nécessaire pour gagner la partie
LONGUEUR_ALIGNEMENT = 4

# Représente un code d'erreur de colonne pleine.
ERREUR_COLONNE_PLEINE = -1

# Tableau de lignes
# le for évite la réutilisation (passage par référence) de la première ligne créée
grille = [[Case.VIDE] * HAUTEUR for _ in range(LARGEUR)]

"""
Retourne un booléen vrai si la colonne spécifiée peut être utilisée comme index dans la grille du jeu, tel que :
colonne ∈ [0 ; LARGEUR[
"""
def EstColonneValide(colonne: int):
    return colonne >= 0 and colonne < LARGEUR

"""
Retourne un booléen vrai si la ligne spécifiée peut être utilisée comme index dans la grille du jeu, tel que :
ligne ∈ [0 ; HAUTEUR[
"""
def EstLigneValide(ligne: int):
    return ligne >= 0 and ligne < HAUTEUR

""" Retourne une colonne valide choisie aléatoirement """
def GenererColonneAleatoire():
    return randint(0, LARGEUR-1)