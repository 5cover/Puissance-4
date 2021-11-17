from enum import Enum

# Énumération de 3 valeurs
class Case(Enum):
    VIDE = ' '
    JOUEUR_1 = '▮'
    JOUEUR_2 = '▯'

HAUTEUR = 6
LARGEUR = 7

grille = [[Case.VIDE] * (LARGEUR + 1)] * (HAUTEUR + 1)

def AfficherGrille():

    for ligne in range(HAUTEUR):

        if ligne == 0:
            print(f'   ┌{"─┬"*(LARGEUR-1)}─┐', end=f'\n {ligne} │')
        else:
            print(f'   ├{"─┼"*(LARGEUR-1)}─┤', end=f'\n {ligne} │')

        for colonne in range(LARGEUR):
            print(grille[colonne][ligne].value, end = '│')

        print("\n", end="")

    print(f'   └{"─┴"*(LARGEUR-1)}─┘')
AfficherGrille()