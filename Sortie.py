# sortie.py
# Fonctions d'affichage

import config

def AfficherGrille():

    # Afficher les numéros de colonnes
    print("  ", end = "")
    for ligneNo in range(1, LARGEUR+1):
        print(ligneNo, end=" ")

    # Sauter une ligne
    print()

    for ligne in range(HAUTEUR):

        if ligne == 0:
            # Haut de la grille
            print(f' ┌{"─┬"*(LARGEUR-1)}─┐', end='\n │')
        else:
            # Séparation entre les lignes
            print(f' ├{"─┼"*(LARGEUR-1)}─┤', end='\n │')

        for colonne in range(LARGEUR):
            # Pions
            print(grille[colonne][ligne].value, end = '│')

        print()

    # Bas de la grille
    print(f' └{"─┴"*(LARGEUR-1)}─┘')
