# entree.py
# Fonctions d'entrée utilisateur

from alignements import ObtenirLigneDePose
from config import *

""" 
Demande à l'utilisateur s'il souhaite jouer contre l'ordinateur.

Retourne True si oui, False sinon.
""" 
def DemanderJouerAvecPC():
    reponse = ''
    while (reponse.lower() != 'o' and reponse.lower() != 'n'):
        reponse = input("Jouer avec l'ordinateur ? (o/n) ")
    return reponse.lower() == 'o'

def DemanderNomJoueur1():
    return input("Nom du joueur 1 : ")

def DemanderNomJoueur2():
    return input("Nom du joueur 2 : ")

"""Retourne une colonne valid où jouer, choisie par l'utilisateur."""
def DemanderColonne():
    colonne = int(input("Colonne : ")) - 1
    while not EstColonneValide(colonne) or ObtenirLigneDePose(colonne) == ERREUR_COLONNE_PLEINE:
        try:
            # on enlève 1 : les colonnes commencent par 1 pour l'utilisateur mais par 0 en index de grille.
            colonne = int(input("Colonne : ")) - 1

        # Sans cette ligne, le programme plante si input reçoit une entrée invalide.
        # Il s'agit d'une exception.
        # Ici, on retourne au début de la boucle en cas d'exception de type ValueError.
        except ValueError:
            continue

    return colonne


"""Retourne une colonne valide où jouer, choisie automatiquement par l'ordinateur."""
def DemanderColonnePC():

    randColonne = GenererColonneAleatoire()

    while ObtenirLigneDePose(randColonne) == ERREUR_COLONNE_PLEINE:
            randColonne = GenererColonneAleatoire()

    return randColonne
