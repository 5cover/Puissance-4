# entree.py
# Fonctions d'entrée utilisateur

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

"""
Demande à l'utilisateur la colonne ou placer un pion.

Retourne le numéro de la colonne entré.
"""
def DemanderColonne():
    colonne = -1
    while colonne < 0 or colonne >= LARGEUR:
        try:
            # on enlève 1 : les colonnes commence par 1 pour l'utilisateur mais par 0 en index de grille.
            colonne = int(input("Colonne : ")) - 1

        # Si l'entrée est invalide
        except ValueError:
            continue

    return colonne