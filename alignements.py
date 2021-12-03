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

        # decalageIndex ∈ [-offset; LONGUEUR_ALIGNEMENT - offset[ sans 0 (inutile de chercher un alignement avec un décalage d'index de 0)
        # decalageIndex : décalage de l'index du pion a tester si membre de l'alignement ou non
        for decalageIndex in (decalageIndex for decalageIndex in range(-offsetPositionAlignement, LONGUEUR_ALIGNEMENT - offsetPositionAlignement) if decalageIndex != 0 and (vertical or horizontal or diagonaleGHDB or diagonaleDHGB)):

            ligneDevant = EstLigneValide(ligne + decalageIndex)
            colonneDevant = EstColonneValide(colonne + decalageIndex)
            ligneDerriere = EstLigneValide(ligne - decalageIndex)

            # Opérateurs séquentiels

            vertical = vertical and ligneDevant and grille[colonne][ligne + decalageIndex] == joueur
            horizontal = horizontal and colonneDevant and grille[colonne + decalageIndex][ligne] == joueur
            diagonaleGHDB = diagonaleGHDB and colonneDevant and ligneDevant and grille[colonne + decalageIndex][ligne + decalageIndex] == joueur
            diagonaleDHGB = diagonaleDHGB and colonneDevant and ligneDerriere and grille[colonne + decalageIndex][ligne - decalageIndex] == joueur

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
 