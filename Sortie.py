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

    for ligne in HAUTEUR:

        if ligne == 0:
            AfficherHautGrille()
        else:
            AfficherEntreLigne()

        for colonne in LARGEUR:
            # Pions
            print(grille[colonne][ligne].value, end = '│')

        print()

    AfficherBasGrille()

def AfficherHautGrille():
    print(f' ┌{"─┬"*(LARGEUR-1)}─┐', end='\n │')

def AfficherBasGrille():
    print(f' └{"─┴"*(LARGEUR-1)}─┘')

def AfficherEntreLigne():
    print(f' ├{"─┼"*(LARGEUR-1)}─┤', end='\n │')