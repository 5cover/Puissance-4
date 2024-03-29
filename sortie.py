﻿# sortie.py
# Fonctions d'affichage

from config import *

def AfficherGrille():
    # Afficher les numéros de colonnes
    print("  ", end = "")
    for ligneNo in range(1, LARGEUR+1):
        print(ligneNo, end=" ")

    # Sauter une ligne
    print()

    for ligne in range(HAUTEUR):

        if ligne == 0:
            AfficherHautGrille()
        else:
            AfficherEntreLigne()

        for colonne in range(LARGEUR):
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

def AfficherCestAuTourDe(nomJoueur: str):
    print(f"C'est au tour de {nomJoueur}.")

def AfficherMessageGagnant(nomJoueur: str):
    print(f"{nomJoueur} a gagné la partie.")

def AfficherMessageMatchNul():
    print("Match nul.")
