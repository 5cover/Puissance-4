# entree.py
# Fonctions d'entrée utilisateur

from config import *

""" 
Demande à l'utilisateur s'il souhaite jouer contre l'ordinateur.

Retourne True si oui, False sinon.
""" 
def DemanderJouerAvecOrdinateur():
    reponse = ''
    while (reponse.lower() != 'o' and reponse.lower() != 'n'):
        reponse = input("Jouer avec l'ordinateur ? (o/n) ")
    return reponse.lower() == 'o'

def DemanderNomJoueur1():
    return input("Nom du joueur 1 : ")

def DemanderNomJoueur2():
    return input("Nom du joueur 2 : ")

