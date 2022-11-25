#DEBUT

#on admet qu'une fonction random existe qui renvoie un chiffre aléatoire
#on damet qu'une fonction input existe qui renvoie l'entrée de l'utilisateur

#créer une liste tableJeu qui servira de table de jeu [['-','-','-'],['-','-','-'],['-','-','-']]

#définir la fonction showTable qui renvoie en paramètre (tableJeu)
    #alors afficher ("\n--------------")
    #pour les lignes dans tableJeu
        #pour les items dans la ligne
            #afficher (item, end="  ")
        #afficher ()
    #afficher ("--------------\n")

#définir la fonction caseFilled qui renvoie en paramètres (tableGame, posx et posy)
    #si tableGame[posx][posy] est égal à '-'
        #alors renvoyer faux
    #sinon 
        #alors renvoyer vrai

#definir la fonction is_player_win qui renvoie en paramètres (tableGame et form)
    #si la valeur 0 de la liste 0 0 est égale à celle de la valeur de la liste 0 1 est égale à la valeur de la liste 0 2  qui est égale au paramètre form
        #alors retourner vrai
    #sinon #si la valeur 0 de la liste 1 0 est égale à celle de la valeur de la liste 1 1 est égale à la valeur de la liste 2 2  qui est égale au paramètre form
        #alors retourner vrai
    #sinon #si la valeur 0 de la liste 2 0 est égale à celle de la valeur de la liste 1 0 est égale à la valeur de la liste 2 0  qui est égale au paramètre form
        #alors retourner vrai
    #sinon #si la valeur 0 de la liste 0 0 est égale à celle de la valeur de la liste 1 0 est égale à la valeur de la liste 2 0  qui est égale au paramètre form
        #alors retourner vrai
    #sinon #si la valeur 0 de la liste 0 1 est égale à celle de la valeur de la liste 1 1 est égale à la valeur de la liste 2 1  qui est égale au paramètre form
        #alors retourner vrai
    #sinon #si la valeur 0 de la liste 0 2 est égale à celle de la valeur de la liste 1 2 est égale à la valeur de la liste 2 2  qui est égale au paramètre form
        #alors retourner vrai
    #sinon #si la valeur 0 de la liste 0 0 est égale à celle de la valeur de la liste 1 1 est égale à la valeur de la liste 2 2  qui est égale au paramètre form
        #alors retourner vrai
    #sinon #si la valeur 0 de la liste 0 2 est égale à celle de la valeur de la liste 1 1 est égale à la valeur de la liste 2 0  qui est égale au paramètre form
        #alors retourner vrai
    #sinon
        #alors retourner faux

#définir la fonction is_tableGame_filled de paramètre (tableGame)
    #pour les lignes dans les tableGame
        #pour les items dans les lignes
            #si item est égal à '-'
                #alors renvoyer faux
    #renvoyer vrai

#définir la fonction deuxParmiTrois de paramètres (a, b, c et deja_existant)
    #si a est égal à b est égal à deja_existant et c est égal à "-"
        #alors retourner 3
    #sinon si c est égal à a est égal à deja_existant et b est égal à "-"
        #alors retourner 2
    #sinon si c est égal à b est égal à deja_existant et a est égal à "-"
        #alors retourner 1
    #sinon
        #alors retourner liste vide

#définir la fonction unParmiTrois de paramètres (a, b et c)
    #si a est égal à "O" et b est égal à c est égal à "-"
        #alors retourner 1
    #sinon si c est égal à "O" et a est égal à b est égal à "-"
        #alors retourner 3
    #sinon si b est égal à "O" et c est égal à a est égal à "-"
        #alors retourner 2

#définir la fonction gagner de paramètres (tableGame et playerBotShoot)
    #pour i allant à 3
        #créer la variable ligne égale à deuxParmiTrois de paramètres (tableGame[i][0], tableGame[i][1], tableGame[i][2], playerBotShoot)
        #créer la variable colonne égale à deuxParmiTrois de paramètres (tableGame[0][i], tableGame[1][i], tableGame[2][i], playerBotShoot)
        #si ligne est différent de liste vide
            #alors retourner liste i ligne - 1
        #si colonne est différent de liste vide
            #alors retourner liste colonne - 1 i
    #créer la variable diag1 égale à deuxParmiTrois de paramètres (tableGame[0][0], tableGame[1][1], tableGame[2][2], playerBotShoot)
    #créer la variable diag2 égale à deuxParmiTrois de paramètres (tableGame[0][2], tableGame[1][1], tableGame[2][0], playerBotShoot)
    #si diag1 est différent de liste vide
        #alors retourner la liste diag1 - 1 diag1 - 1
    #si diag2 est différent de liste vide
        #alors retourner la liste diag2 - 1 3 - diag2
    #retourner liste vide

#éfinir la fonction pasGagner de paramètres (tableGame et playerBotShoot)
    #pour i allant à 2
        #créer la variable ligne égale à unParmiTrois de paramètres (tableGame[i*2][0], tableGame[i*2][1], tableGame[i*2][2])
        #créer la variable colonne égale à unParmiTrois de paramètres (tableGame[0][i*2], tableGame[1][i*2], tableGame[2][i*2])
        #si ligne est différent de liste vide
            #alors retourner liste i * 2 ligne
        #si colonne est différent de liste vide
            #alors retourner liste colonne i * 2
    #créer la variable diag1 égale à deuxParmiTrois de paramètres (tableGame[0][0], tableGame[1][1], tableGame[2][2])
    #créer la variable diag2 égale à deuxParmiTrois de paramètres (tableGame[0][2], tableGame[1][1], tableGame[2][0])
    #si diag1 est différent de liste vide
        #alors retourner la liste diag1 diag1
    #si diag2 est différent de liste vide
        #alors retourner la liste diag2 2 - diag2
    #retourner liste vide

#définir la fonction bot de paramètres (tableGame, playerSoloShoot et playerBotShoot)
#créer la varaible wino égale à gagner de paramètres (tableGame et playerBotShoot)
#si la liste 1 1 est égal à "-"
    #alors la liste 1 1 est égal à playerBotShoot
#sinon si la liste 1 1 est égal à "X" ET la liste 0 0 est égal à "-"
    #alors la liste 0 0 est égal à playerBotShoot
#sinon si wino est différent de liste vide
    #alors tableGame[wino[0]][wino[1]] = playerBotShoot
#sinon si la liste 0 0 est égale à "X" ET la liste 2 2 est égal à "X"
    #alors la liste 1 0 est égale à playerBotShoot
#sinon si la liste 0 2 est égale à "X" ET la liste 2 0 est égale à "X"
    #alors la liste 1 2 est égale à playerBotShoot
#sinon si liste 2 2 est égale à "X" ET la liste 1 2 est égale à "X"
    #alors la liste 0 2 est égale à playerBotShoot
#sinon si gagner de paramètres (tableGame et playerSoloShoot) est différent de liste vide
    #alors tableGame[gagner(tableGame, playerSoloShoot)[0]][gagner(tableGame, playerSoloShoot)[1]] est égal à playerBotShoot
#sinon si pasGagner de paramètres (tableGame et playerBotShoot) est différent de liste vide
    #alors créer une variable a_jouer égale à pasGagner de paramètres (tableGame et playerBotShoot)
    #alors tableGame[a_jouer[0]][a_jouer[1]] est égal à playerBotShoot
#sinon si la liste 0 0 est égale à "-"
    #alors la liste 0 0 est égale à playerBotShoot
#sinon si la liste 0 2 est égale à "-"
    #alors la liste 0 2 est égale à playerBotShoot
#sinon si la liste 2 0 est égale à "-"
    #alors la liste 2 0 est égale à playerBotShoot
#sinon si la liste 2 2 est égale à "-"
    #alors la liste 2 2 est égale à playerBotShoot
#sinon si la liste 0 1 est égale à "-"
    #alors la liste 0 1 est égale à playerBotShoot
#sinon si la liste 1 2 est égale à "-"
    #alors la liste 1 2 est égale à playerBotShoot
#sinon si la liste 2 1 est égale à "-"
    #alors la liste 2 1 est égale à playerBotShoot

#définir la fonction coup de paramètres (playerTurn, playerShoot, playerSoloShoot, playerBotShoot et playerSolo)
    #créer une variable game égale à vrai
    #tant que game est vrai
        #if playerTurn est égal à PlayerSolo
            #créer une variable choiceX et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n")
            #créer une variable choiceY et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez la colonne à modifier (colonne 1 = 0 / colonne 2 = 1 / colonne 3 = 2) : \n")
            #si choiceX est dans la liste 0 1 2 ET choiceY dans la liste 0 1 2
                #si caseFilled de paramètres (tableGame, choiceX et choiceY) est différent de vrai
                    #tableGame[choiceX][choiceY] est égal à playerShoot
            #sinon si choiceX n'est pas dans la liste 0 1 2 ET choiceY n'est pas dans la liste 0 1 2
                #alors afficher ("Erreur, rentrez un numéro valide \n")
                #alors exécuter coup de paramètres (playerTurn, playerShoot, playerSoloShoot, playerBotShoot et playerSolo)

            #exécuter showTable de paramètre (tableGame)

            #si is_player_win de paramètres (tableGame et playerSoloShoot)
                #si playerSolo est égal à "Antoine"
                    #alors afficher (playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                #sinon
                    #alors afficher (playerBot +  " à gagné la partie ! :) \n")
                #alors galme est faux
                #alors casser la boucle

            #sinon si is_tablegame_filled de paramètre (tableGame)
                #si playerSolo est égal à "Antoine"
                    #alors afficher (playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                #sinon
                    #alors afficher ("Egalité ! :/ \n")
                #alors galme est faux
                #alors casser la boucle

            #exécuter bot de paramètres (tableGame, playerSoloShoot et playerBotShoot)

            #exécuter showTable de paramètre (tableGame)

            #si is_player_win de paramètres (tableGame et playerBotShoot)
                #si playerSolo est égal à "Antoine"
                    #alors afficher (playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                #sinon
                    #alors afficher (playerBot +  " à gagné la partie ! :) \n")
                #alors galme est faux
                #alors casser la boucle

            #sinon si is_tablegame_filled de paramètre (tableGame)
                #si playerSolo est égal à "Antoine"
                    #alors afficher (playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                #sinon
                    #alors afficher ("Egalité ! :/ \n")
                #alors galme est faux
                #alors casser la boucle

        #sinon si playerTurn est égal à playerBot

            #exécuter bot de paramètres (tableGame, playerSoloShoot et playerBotShoot)

            #exécuter showTable de paramètre (tableGame)

            #si is_player_win de paramètres (tableGame et playerBotShoot)
                #si playerSolo est égal à "Antoine"
                    #alors afficher (playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                #sinon
                    #alors afficher (playerBot +  " à gagné la partie ! :) \n")
                #alors galme est faux
                #alors casser la boucle

            #sinon si is_tablegame_filled de paramètre (tableGame)
                #si playerSolo est égal à "Antoine"
                    #alors afficher (playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                #sinon
                    #alors afficher ("Egalité ! :/ \n")
                #alors galme est faux
                #alors casser la boucle

            #créer une variable choiceX et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n")
            #créer une variable choiceY et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez la colonne à modifier (colonne 1 = 0 / colonne 2 = 1 / colonne 3 = 2) : \n")
            #si choiceX est dans la liste 0 1 2 ET choiceY dans la liste 0 1 2
                #si caseFilled de paramètres (tableGame, choiceX et choiceY) est différent de vrai
                    #tableGame[choiceX][choiceY] est égal à playerShoot
            #sinon si choiceX n'est pas dans la liste 0 1 2 ET choiceY n'est pas dans la liste 0 1 2
                #alors afficher ("Erreur, rentrez un numéro valide \n")
                #alors exécuter coup de paramètres (playerTurn, playerShoot, playerSoloShoot, playerBotShoot et playerSolo)

            #exécuter showTable de paramètre (tableGame)

            #si is_player_win de paramètres (tableGame et playerSoloShoot)
                #si playerSolo est égal à "Antoine"
                    #alors afficher (playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                #sinon
                    #alors afficher (playerBot +  " à gagné la partie ! :) \n")
                #alors galme est faux
                #alors casser la boucle

            #sinon si is_tablegame_filled de paramètre (tableGame)
                #si playerSolo est égal à "Antoine"
                    #alors afficher (playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                #sinon
                    #alors afficher ("Egalité ! :/ \n")
                #alors galme est faux
                #alors casser la boucle

#définir la fonction menu
    #créer une variable house égale à vrai
    #tant que house est égal à vrai
        #créer une variable home et lui associer le retour de l'exécution de la fonction input pour demander ("Bienvenue dans le célèbre jeu du Morpion ! Affrontez-vous en 1vs1 ou confrontez-vous à notre bot à vos risques et périls :) \nVoulez-vous un rappel des règles ? oui ou non : \n")
        #si home est égal à oui
            #alors afficher ("Le jeu du Morpion se joue sur un tableau de 3 par 3. Le but du jeu est d'aligner avant son adversaire 3 symboles identiques (les X ou les O) horizontalement, verticalement ou en diagonale.")
            #alors créer la variable startGame et lui associer le retour de l'exécution de la fonction input pour demander ("Voulez-vous jouer ? oui ou non : \n")
        #sinon si menu est égal à non
            #alors créer la variable startGame et lui associer le retour de l'exécution de la fonction input pour demander ("Voulez-vous jouer ? oui ou non : \n")
        #sinon
            #alors afficher ("Erreur, entrez 'oui' ou 'non' \n")

        #si startGame est égal à oui
            #alors créer la variable modeGame et lui associer le retour de l'exécution de la fonction input pour demander ("Choissiez un mode de jeu : 1vs1 = 1 / 1vsBot = 2 \n")
            #si modeGame est égal à 2
                #alors créer la variable playerSolo et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez votre pseudo : \n")
                #alors exécuter soloMode de paramètre (playerSolo)
            #sinon si modeGame est égal à 1
                #alors créer la variable playerOne et lui associer le retour de l'exécution de la fonction input pour demander ("Joueur X choisissez votre pseudo : \n")
                #alors créer la variable playerTwo et lui associer le retour de l'exécution de la fonction input pour demander ("Joueur O choisissez votre pseudo : \n")
                #alors exécuter duoMode de paramètres (playerOne et playerTwo)
            #sinon
                #alors afficher ("Erreur, entrez '1' ou '2' \n")

        #sinon si starGame est égal à non
            #alors afficher ("Tant pis, à bientôt !")
            #alors house est faux
        #sinon
            #alors afficher ("Erreur, entrez 'oui' ou 'non' \n")
            
#définir la fonction soloMode de paramètre (playerSolo)
    #global tableGame, playerBot
    #playerBot est égal à "Abdel.exe"
    #playerSoloShoot est égal à "X"
    #playerBotShoot est égal à "O"

    #créer la variable choiceTurn et lui associer le retour de l'exécution de la fonction input pour demander ("Qui commence ? " + playerSolo + " = 1 / Bot = 2 \n")

    #si choiceTurn est égal à 1
        #alors playerTurn est égal à playerSolo
        #alors playerShoot est égal à playerSoloShoot
    #sinon si choiceTurn est égal à 2
        #alors playerTurn est égal à playerBot
        #alors playerShoot est égal à playerSoloShoot
    #sinon
        #alors afficher ("Erreur, entrez '1' ou '2' \n")
        #alors #créer la variable choiceTurn et lui associer le retour de l'exécution de la fonction input pour demander ("Qui commence ? " + playerSolo + " = 1 / Bot = 2 \n")

    #exécuter showTable de paramètre (tableGame)
    #exécuter bot de paramètres (tableGame, playerSoloShoot et playerBotShoot)

    #créer la variable rejouer égale à vrai
    #tant que rejouer est vrai
        #créer la variable choiceTurn et lui associer le retour de l'exécution de la fonction input pour demander ("Voulez-vous rejouer ? oui ou non : \n")
        #si otherGame est égal à oui
            #alors afficher ("C'est reparti !")
            #alors tableGame est égal à [['-','-','-'],['-','-','-'],['-','-','-']]
            #exécuter soloMode de paramètre (playerSolo)
        #sinon si otherGame est égal à non
            #alors afficher ("A bientôt !")
            #alors rejouer est faux
        #sinon
            #alors afficher ("Erreur, entrez 'oui' ou 'non' \n")

#définir la fonction duoMode de paramètre (playerOne et playerTwo)
    #tableGame est égal à [['-','-','-'],['-','-','-'],['-','-','-']]
    #playerOneShoot est égal à "X"
    #playerTwoShoot est égal à "O"
    #playerStart est égal à la fonction randint qui renvoie un chiffre aléatoire entre 1 et 2

    #si playerStart est égal à 1
        #alors playerTurn est égal à playerOne
        #alors playerShoot est égal à playerOneShoot
    #sinon
        #alors playerTurn est égal à playerTwo
        #alors playerShoot est égal à playerTwoShoot

    #créer une varibale correctShoot égale à faux
    #créer une variable playerWin égale à faux

    #exécuter showTable de paramètre (tableGame)
    #tant que playerWin est faux
        #tant que correctShoot est faux
            #créer une variable choiceX et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n")
            #créer une variable choiceY et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez la colonne à modifier (colonne 1 = 0 / colonne 2 = 1 / colonne 3 = 2) : \n")
            #si choiceX est dans la liste 0 1 2 ET choiceY dans la liste 0 1 2
                #si caseFilled de paramètres (tableGame, choiceX et choiceY) est différent de vrai
                    #tableGame[choiceX][choiceY] est égal à playerShoot
                    #correctShoot est vrai
        #exécuter showTable de paramètre (tableGame)

    #si is_player_win de paramètres (tableGame et playerOneShoot)
        #alors afficher ("Le joueur " + playerOne +  " à gagné la partie ! :) ")
        #alors casser la boucle

    #si is_player_win de paramètres (tableGame et playerTwoShoot)
        #alors afficher ("Le joueur " + playerTwo +  " à gagné la partie ! :) ")
        #alors casser la boucle

    #si is_player_win de paramètres (tableGame)
        #alors afficher ("Egalité ! :/")
        #alors casser la boucle

    #si playerShoot est égal à playerOneShoot
        #alors playerShoot est égal à playerTwoShoot
        #alors playerTurn est égal à playerTwo
    #sinon
        #alors playerShoot est égal à playerOneShoot
        #alors playerTurn est égal à playerOne

    #correctShoot est faux

    #créer la variable rejouer égale à vrai
    #tant que rejouer est vrai
        #créer la variable choiceTurn et lui associer le retour de l'exécution de la fonction input pour demander ("Voulez-vous rejouer ? oui ou non : \n")
        #si otherGame est égal à oui
            #alors afficher ("C'est reparti !")
            #alors tableGame est égal à [['-','-','-'],['-','-','-'],['-','-','-']]
            #exécuter soloMode de paramètre (playerSolo)
        #sinon si otherGame est égal à non
            #alors afficher ("A bientôt !")
            #alors rejouer est faux
        #sinon
            #alors afficher ("Erreur, entrez 'oui' ou 'non' \n")

#exécuter menu()

#FIN