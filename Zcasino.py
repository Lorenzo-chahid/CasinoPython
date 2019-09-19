import random
from math import ceil




argent_depart = 1000
name = input(" Quel est votre nom ? ")


continuer = 1

while continuer:
    if argent_depart <= 0:
        print("Vous n'avez plus assez d'argent !!! Aller faire un crédit :)")
        continuer = 0
    else:
        continuer

       
        # choix du nombre à la roulette 
        print("Bienvenue à la table {} , Vous avez {} $".format(name, argent_depart))
        choix = int(input("Veuillez choisir un nombre entre 0 et 49 : "))

        while choix > 49 or choix < 0:
            print("Merci de choisir un nombre valide!")
            choix = int(input("Veuillez choisir un nombre entre 0 et 49 : "))
            if choix >= 0 and choix <=49:
                   # Mise d'argent 
                mise  = int(input("Veuillez miser la somme que vous souhaitez mettre :  "))
                while mise > argent_depart or mise < argent_depart:
                    print("Veuillez miser votre argent pas votre femme !")
                    mise  = int(input("Veuillez miser la somme que vous souhaitez mettre :  "))
                
            
                roulette = random.randrange(0,50)
                pair = roulette % 2 == 0
                impair = roulette % 2 == 1
                argent_depart = argent_depart - mise 
                print("Les dés sont lancés  ") 
                print("Tic....tic..tic..tic..")
                print('......... ..')

                number_win = roulette 

                
                if number_win != choix and choix == pair:
                    argent_depart += ceil(mise /2 )
                    print("Le numero gagnat est le {}".format(number_win))
                    print("Vous avez perdu ! Mais vous êtes sur le noir ! Vous récupérez 50 de votre mise ")
                    print( "Vous avez maintenant : {} $".format(argent_depart))
                elif number_win != choix and choix == impair:
                    argent_depart  += ceil(mise /2 )
                    print("Le numero gagnat est le {} $".format(number_win))
                    print("Vous avez perdu ! Mais vous êtes sur le rouge ! Vous récupérez 50 de votre mise ")
                    print( "Vous avez maintenant : {} $".format(argent_depart))
                elif number_win == choix:
                    argent_depart = argent_depart  + ceil(mise * 3)
                    print("vous avez gagnez le jackpot ! ")
                    print( "Vous avez maintenant : {} $".format(argent_depart))
                else:
                    argent_depart  - mise 
                    print("Le numero gagnat est le {}".format(number_win))
                    print("perdu complet !")
                    print("Il vous reste {} $".format(argent_depart))

                
                boucle = input("Voulez vous continuer de jouer ? tape 'Y' or 'N' ").upper()
                try:
                    pass
                except:
                    pass
                if boucle == 'N':
                    continuer = 0
                    print("Vous partez avec la somme de {} $".format(argent_depart))
                    print("Merci et à bientôt")
                elif boucle == 'Y':
                    print(" Vous continuez !!!")
                    continuer = 1
                else:
                    print("Je ne comprend pas !")
            

        
     





