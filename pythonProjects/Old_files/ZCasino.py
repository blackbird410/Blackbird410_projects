from random import randrange
from math import ceil

mise_d = int(input("Votre mise de depart :"))

while mise_d >= 0:
    gain = 0
    mise = -1
    n_joueur = -1
    # Generation du nombre aleatoire
    n_gagnant = randrange(50)

    while n_joueur >= 50 or n_joueur < 0:
        n_joueur = int(input("Vous misez sur quel numero [0-50[:\n"))

    while mise > mise_d or mise < 0:
        mise = int(input("Vous misez combien ?\n"))

    mise_d -= mise

    if n_joueur == n_gagnant:
        print("FELICITATIONS ! Vous avez gagne. Votre gain est de ", 2 * mise, ".")
        gain += 3 * mise
        mise_d += gain
    elif (n_joueur % 2) == (n_gagnant % 2):
        print("Vous avez eu la meme couleur.\n")
        mise -= ceil(mise / 2)
        mise_d += mise
    else:
        print("Vous avez malheureusement perdu.\n")
        mise = 0

    print("CAPITAL : ", mise_d, "\nNUMERO GAGNANT : ", n_gagnant, "\n")
    s = -1
    while s > 1 or s < 0:
        s = int(input("Voulez-vous continuer ?\n1-OUI    0-NON\n"))

    if s:
        print("ON RELANCES !!!\n\n")
    else:
        print("A la prochaine !\n")
        mise_d = -1
        break
