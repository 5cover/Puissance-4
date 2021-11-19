# entree.py
# Fonctions d'entrée utilisateur

from config import *

def DemanderJouerAvecOrdinateur():
    reponse = ''
    while (reponse.lower() != 'o' and reponse.lower() != 'n'):
        reponse = input("Jouer avec l'ordinateur ? (o/n) ")
    return reponse == 'o'

def ChoisirJoueurs():

    if DemanderJouerAvecOrdinateur():
        nomJoueur1 = input("Votre nom : ")
        nomJoueur2 = "Ordinateur"
    else:
        nomJoueur1 = input("Nom du joueur 1 : ")
        nomJoueur2 = input("Nom du joueur 2 : ")
