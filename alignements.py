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

        # voisin ∈ [-offset; LONGUEUR_ALIGNEMENT - offset[
        # voisin : décalage de l'index du pion a tester si membre de l'alignement ou non
        for decalageIndex in range(-offsetPositionAlignement, LONGUEUR_ALIGNEMENT - offsetPositionAlignement):

            if decalageIndex == 0:
                continue

            ligneDevantExiste = EstLigneValide(ligne + decalageIndex)
            ligneDerriereExiste =  EstLigneValide(ligne - decalageIndex)
            colonneDevantExiste = EstColonneValide(colonne + decalageIndex)

            # Utilisation des opérateurs séquenciels
            horizontal    = horizontal    and colonneDevantExiste                            and grille[colonne + decalageIndex][ligne] == joueur
            vertical      = vertical      and ligneDevantExiste                              and grille[colonne][ligne + decalageIndex] == joueur
            diagonaleGHDB = diagonaleGHDB and colonneDevantExiste and ligneDevantExiste  and grille[colonne + decalageIndex][ligne + decalageIndex] == joueur 
            diagonaleDHGB = diagonaleDHGB and colonneDevantExiste and ligneDerriereExiste and grille[colonne + decalageIndex][ligne - decalageIndex] == joueur

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
 