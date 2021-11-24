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

    vertical = True
    horizontal = True
    diagonaleGHDB = True
    diagonaleDHGB = True


    # décalage de la plage d'index voisins à tester pour tester toutes les positions possibles du pion actuel dans l'alignement
    for offset in range(LONGUEUR_ALIGNEMENT):

        # voisin ∈ [-offset; LONGUEUR_ALIGNEMENT - offset[
        # voisin : décalage de l'index du pion a tester si membre de l'alignement ou non
        for voisin in range(-offset, LONGUEUR_ALIGNEMENT - offset):

            if voisin == 0:
                continue

            lignePlusVoisinExiste = ligne + voisin >= 0 and ligne + voisin < HAUTEUR
            ligneMoinsVoisinExiste = ligne - voisin >= 0 and ligne - voisin < HAUTEUR
            colonnePlusVoisinExiste = colonne + voisin >= 0 and colonne + voisin < LARGEUR

            horizontal    = horizontal    and colonnePlusVoisinExiste                            and grille[colonne + voisin][ligne] == joueur
            vertical      = vertical      and lignePlusVoisinExiste                              and grille[colonne][ligne + voisin] == joueur
            diagonaleGHDB = diagonaleGHDB and colonnePlusVoisinExiste and lignePlusVoisinExiste  and grille[colonne + voisin][ligne + voisin] == joueur 
            diagonaleDHGB = diagonaleDHGB and colonnePlusVoisinExiste and ligneMoinsVoisinExiste and grille[colonne + voisin][ligne - voisin] == joueur

        if vertical or horizontal or diagonaleGHDB or diagonaleGHDB: # si on a trouvé un alignement
            return True
    return False

""" Retourne la ligne de la case vide la plus basse à la colonne spécifiée, ou ERREUR_COLONNE_PLEINE si la colonne n'a aucune ligne vide. """
def ObtenirLigneDisponible(colonne):
    for ligne in reversed(range(HAUTEUR)):
        if grille[colonne][ligne] == Case.VIDE:
            return ligne
    return ERREUR_COLONNE_PLEINE

 