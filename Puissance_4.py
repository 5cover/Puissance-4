from enum import Enum

# Énumération de 3 valeurs
class Case(Enum):
    VIDE = ' '
    JOUEUR_1 = '▮'
    JOUEUR_2 = '▯'

HAUTEUR = 6
LARGEUR = 7

grille = [[Case.VIDE] * (LARGEUR + 1)] * (HAUTEUR + 1)
nomJoueur1 = ''
nomJoueur2 = ''


def AfficherGrille():

    for ligne in range(HAUTEUR):

        if ligne == 0:
            print(f'   ┌{"─┬"*(LARGEUR-1)}─┐', end=f'\n {ligne} │')
        else:
            print(f'   ├{"─┼"*(LARGEUR-1)}─┤', end=f'\n {ligne} │')

        for colonne in range(LARGEUR):
            print(grille[colonne][ligne].value, end = '│')

        print("\n", end="")

    print(f'   └{"─┴"*(LARGEUR-1)}─┘')

def DemanderJouerAvecOrdinateur():
    reponse = ''
    while (reponse != 'O' and reponse != 'N'):
        reponse = input("Jouer avec l'ordinateur ? (O/N) ")
    return reponse == 'O'

def ChoisirJoueurs():

    if DemanderJouerAvecOrdinateur():
        nomJoueur1 = input("Votre nom : ")
        nomJoueur2 = "Ordinateur"
    else:
        nomJoueur1 = input("Nom du joueur 1 :")
        nomJoueur2 = input("Nom du joueur 2 :")

ChoisirJoueurs()
AfficherGrille()