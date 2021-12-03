# alignements.py
# Fonctions cherchant des alignements sur la grille

from config import *

""" 
Cherche un alignement gagnant à l'emplacement du dernier pion placé.

colonne : colonne du dernier pion placé
ligne : ligne du dernier pion placé

Retourne True si un alignement a été trouvé, sinon False
"""
def ChercherAlignement(colonne: int, ligne: int):

    assert(EstColonneValide(colonne))
    assert(EstLigneValide(ligne))

    joueur = grille[colonne][ligne]
    if joueur == Case.VIDE:
        return False

    # décalage de la plage d'index voisins à tester pour tester toutes les positions possibles du pion actuel dans l'alignement
    for offsetPositionAlignement in range(LONGUEUR_ALIGNEMENT):

        vertical = True
        horizontal = True
        diagonaleGHDB = True
        diagonaleDHGB = True

        # decalageIndex ∈ [-offsetPositionAlignement; LONGUEUR_ALIGNEMENT - offsetPositionAlignement[
        # decalageIndex : décalage de l'index du pion a tester si membre de l'alignement ou non
        for i in (i for i in range(-offsetPositionAlignement, LONGUEUR_ALIGNEMENT - offsetPositionAlignement) if i != 0 and (vertical or horizontal or diagonaleGHDB or diagonaleDHGB)):

            ligneDevant = EstLigneValide(ligne + i)
            colonneDevant = EstColonneValide(colonne + i)
            ligneDerriere = EstLigneValide(ligne - i)

            # Opérateurs séquentiels

            vertical      = vertical and ligneDevant and                          grille[colonne][ligne + i] == joueur
            horizontal    = horizontal and colonneDevant and                      grille[colonne + i][ligne] == joueur
            diagonaleGHDB = diagonaleGHDB and colonneDevant and ligneDevant and   grille[colonne + i][ligne + i] == joueur
            diagonaleDHGB = diagonaleDHGB and colonneDevant and ligneDerriere and grille[colonne + i][ligne - i] == joueur

        if vertical or horizontal or diagonaleGHDB or diagonaleDHGB: # si on a trouvé un alignement
            return True

    return False

""" Retourne la ligne de la case vide la plus basse à la colonne spécifiée, ou ERREUR_COLONNE_PLEINE si la colonne n'a aucune ligne vide. """
def ObtenirLigneDePose(colonne: int):

    assert(EstColonneValide(colonne))

    for ligne in reversed(range(HAUTEUR)):
        if grille[colonne][ligne] == Case.VIDE:
            return ligne

    return ERREUR_COLONNE_PLEINE
 
