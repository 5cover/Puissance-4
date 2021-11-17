# config.py
# Variables globales

from enum import Enum

# Une variable de type Case peut être d'une de ces valeurs.
class Case(Enum):
    VIDE = ' '
    JOUEUR_1 = '▮'
    JOUEUR_2 = '▯'

HAUTEUR = 6
LARGEUR = 7

grille = [[Case.VIDE] * (LARGEUR + 1)] * (HAUTEUR + 1)
nomJoueur1 = ''
nomJoueur2 = ''
