# config.py
# Variables globales

from enum import Enum

# Une variable de type Case peut être d'une de ces valeurs.
class Case(Enum):
    VIDE = ' '
    JOUEUR_1 = '▮'
    JOUEUR_2 = '▯'

# Nombre de lignes de la grille
HAUTEUR = 6
# Nombre de colonnes de la grille
LARGEUR = 7


# le for évite la réutilisation de la première ligne créée

# Tableau de lignes (pas de colonnes)
grille = [[Case.VIDE] * HAUTEUR for _ in range(LARGEUR)]
nomJoueur1 = ''
nomJoueur2 = ''
