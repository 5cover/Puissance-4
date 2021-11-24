# config.py
# Variables globales

from enum import Enum

# Une variable de type Case peut être d'une de ces valeurs.
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


# Représente un code d'erreur.
ERREUR_COLONNE_PLEINE = -1

# Tableau de lignes
# le for évite la réutilisation de la première ligne créée
grille = [[Case.VIDE] * HAUTEUR for _ in range(LARGEUR)]