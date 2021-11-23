# main.py
# Point d'entrée du programme

from config import *
from entree import ChoisirJoueurs
from sortie import AfficherGrille
from alignements import ChercherAlignement, ObtenirLigneDisponible



ChoisirJoueurs()
AfficherGrille()


grille[2][ObtenirLigneDisponible(2)] = Case.JOUEUR_1
ChercherAlignement(2, ObtenirLigneDisponible(2), Case.JOUEUR_1)

AfficherGrille()
