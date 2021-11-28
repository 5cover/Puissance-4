# alignements.py
# Fonctions cherchant des alignements sur la grille

from config import *

""" 
Cherche un alignement gagnant à l'emplacement du dernier pion placé.

colonne : colonne du dernier pion placé
ligne : ligne du dernier pion placé

Retourne True si un alignement a été trouvé, sinon False
"""
def ChercherAlignement(colonne, ligne):

    assert(colonne >= 0 and colonne < LARGEUR) # colonne ∈ [0 ; LARGEUR[
    assert(ligne >= 0 and ligne < HAUTEUR) # colonne ∈ [0 ; HAUTEUR[

    joueur = grille[colonne][ligne]
    if joueur == Case.VIDE:
        return False
    # décalage de la plage d'index voisins à tester pour tester toutes les positions possibles du pion actuel dans l'alignement
    for offset in range(LONGUEUR_ALIGNEMENT):

        vertical = True
        horizontal = True
        diagonaleGHDB = True
        diagonaleDHGB = True

        # voisin ∈ [-offset; LONGUEUR_ALIGNEMENT - offset[
        # voisin : décalage de l'index du pion a tester si membre de l'alignement ou non
        for decalageIndex in range(-offset, LONGUEUR_ALIGNEMENT - offset):

            if decalageIndex == 0:
                continue

            lignePlusVoisinExiste = ligne + decalageIndex >= 0 and ligne + decalageIndex < HAUTEUR
            ligneMoinsVoisinExiste = ligne - decalageIndex >= 0 and ligne - decalageIndex < HAUTEUR
            colonnePlusVoisinExiste = colonne + decalageIndex >= 0 and colonne + decalageIndex < LARGEUR

            horizontal    = horizontal    and colonnePlusVoisinExiste                            and grille[colonne + decalageIndex][ligne] == joueur
            vertical      = vertical      and lignePlusVoisinExiste                              and grille[colonne][ligne + decalageIndex] == joueur
            diagonaleGHDB = diagonaleGHDB and colonnePlusVoisinExiste and lignePlusVoisinExiste  and grille[colonne + decalageIndex][ligne + decalageIndex] == joueur 
            diagonaleDHGB = diagonaleDHGB and colonnePlusVoisinExiste and ligneMoinsVoisinExiste and grille[colonne + decalageIndex][ligne - decalageIndex] == joueur

        if vertical or horizontal or diagonaleGHDB or diagonaleDHGB: # si on a trouvé un alignement
            return True
    return False

""" Retourne la ligne de la case vide la plus basse à la colonne spécifiée, ou ERREUR_COLONNE_PLEINE si la colonne n'a aucune ligne vide. """
def ObtenirLigneDisponible(colonne):
    for ligne in reversed(range(HAUTEUR)):
        if grille[colonne][ligne] == Case.VIDE:
            return ligne
    return ERREUR_COLONNE_PLEINE
 