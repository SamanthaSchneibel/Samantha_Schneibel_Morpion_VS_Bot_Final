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

#définir la fonction caseFilled qui renvoie en paramètres (board, posx et posy)
    #si board[posx][posy] est égal à '-'
        #alors renvoyer faux
    #sinon 
        #alors renvoyer vrai

#definir la fonction is_player_win qui renvoie en paramètres (board et player)
    #créer la variable win égale à None

    #créer la variable n égale à la longueur de board
 
    #pour i allant de 0 à n-1
        #win est égal à vrai
        #pour j allant de 0 à n-1
            #si board[i][j] différent de player
                #alors win est égal à faux
                #alors casser la boucle
        #si win
            #alors renvoyer win

    
    #pour i allant de 0 à n-1
        #win est égal à vrai
        #pour j allant de 0 à n-1
            #si board[j][i] différent de player
                #alors win est égal à faux
                #alors casser la boucle
        #si win
            #alors renvoyer win

    #win est égal à vrai
    #pour i allant de 0 à n-1
        #si board[i][i] est différent de player
            #alors win est égal à faux
            #alors casser la boucle
    #si win
        #alors renvoyer win
    #renvoyer faux

    #win est égal à vrai
    #pour i allant de 0 à n-1
        #si board[i][n - 1 - i] est différent de player
            #alors win est égal à faux
            #alors casser la boucle
    #si win
        #alors renvoyer win
    #renvoyer faux

 
#définir la fonction is_board_filled de paramètre (board)
    #pour les lignes dans les board
        #pour les items dans les lignes
            #si item est égal à '-'
                #alors renvoyer faux
    #renvoyer vrai

#créer une variable menu et lui associer le retour de l'exécution de la fonction input pour demander ("Bienvenue dans le célèbre jeu du Morpion ! Affrontez-vous en 1vs1 ou confrontez-vous à notre bot à vos risques et périls :) \nVoulez-vous un rappel des règles ? oui ou non : \n")
#si menu est égal à oui
    #alors afficher ("Le jeu du Morpion se joue sur un tableau de 3 par 3. Le but du jeu est d'aligner avant son adversaire 3 symboles identiques (les X ou les O) horizontalement, verticalement ou en diagonale.")
#sinon si menu est égal à non
    #alors afficher ()
#sinon
    #alors afficher ("Error, entrez (oui) ou (non) \n")
    #alors utliser la variable menu et lui associer le retour de l'exécution de la fonction input pour demander ("Bienvenue dans le célèbre jeu du Morpion ! Affrontez-vous en 1vs1 ou confrontez-vous à notre bot à vos risques et périls :) \nVoulez-vous un rappel des règles ? oui ou non : \n")

#créer une variable game et lui associer le retour de l'exécution de la fonction input pour demander ("Voulez-vous jouer ? oui ou non : \n")
#si game est égal à oui
    #alors game est vrai
#sinon si game est égal à non
    #alors game est faux
#sinon
    #alors afficher ("Erreur, entrez (oui) ou (non) \n")
    #alors utliser la variable game et lui associer le retour de l'exécution de la fonction input pour demander ("Voulez-vous jouer ? oui ou non : \n")
    
#tant que game est égal à vrai
    #créer une variable gameMode et lui associer le retour de l'exécution de la fonction input pour demander ("Choissiez un mode de jeu : 1vs1 = 1 / 1vsBot = 2 \n")
    #si gameMode est égal à 1
        #alors créer une variable duoMode égale à vrai
    #sinon si gameMode est égal à 2
        #alors créer une variable soloMode égale à vrai
    #sinon
        #alors afficher ("Erreur, entrez (1) ou (2) \n")
        #alors utliser la variable gameMode et lui associer le retour de l'exécution de la fonction input pour demander ("Choissiez un mode de jeu : 1vs1 = 1 / 1vsBot = 2 \n")

    #tant que duoMode est vrai
        #soloMode est faux
        #créer une variable playerOne et lui associer le retour de l'exécution de la fonction input pour demander ("Joueur X choisissez votre pseudo : \n")
        #créer une variable plauerTwo et lui associer le retour de l'exécution de la fonction input pour demander ("Joueur O choisissez votre pseudo : \n")
    
        #créer une varaible playerOneShoot égale à X
        #créer une variable playerTwoShoot égal à O
        #créer une variable playStart qui renvoie un chiffre aléatoire entre 1 et 2

        #si playerStart est égal à 1
            #alors créer une variable playerTurn égale à playerOne
            #alors créer une variable playerShoot égale à playerOneShoot
        #sinon
            #alors créer une variable playerTurn égale à playerTwo
            #alors créer une variable playerShoot égale à playerTwoShoot

        #créer une variable correctShoot égale à faux
        #créer une variable playerWin égale à faux

        #exécuter la fonction showTable avec en paramètre (tableJeu)
        #tant que playerWin est égal à faux
            #tant que correctShoot est égal à faux
                #afficher ("Au Tour de " + playerTurn + "\n")
                #créer une variable choiceX et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n")
                #créer une variable choiceY et lui associer le retour de l'exécution de la fonction input pour demander ("Choisissez la colonne à modifier (colonne 1 = 0 / colonne 2 = 1 / colonne 3 = 2) : \n")
                #si la fonction caseFilled avec en paramètres (tablegame, choiceX et choiceY) est différent de vrai
                    #alors tableGame[choiceX][choiceY] est égal à playerShoot
                    #alors correctShoot est vrai
            #éxécuter la fonction showTable avec en paramètre (tableJeu)

            #si la fonction is_board_win de paramètres (tableGame et playerShoot)
                #alors afficher ("Le joueur " + playerTurn +  " à gagné la partie ! :) ")
                #alors casser la boucle

            #si la fonction is_board_filled de paramètre (tableGame)
                #alors afficher ("Egalité ! :/")
                #alors casser la boucle

            #si playerShoot est égal à playerOneShoot
                #alors playerShoot est égal à playerTwoShoot
                #alors playerTurn est égal à playerTwo
            #sinon
                #alors playerShoot est égal à playerOneShoot
                #alors playerTurn est égal à playerOne

            #correctShoot est faux
    
    #tant que soloMode est égal à vrai
        #duoMode est faux
        #créer une variable player et lui associer le retour de l'exécution de la fonction input pour demander ("Entrez votre pseudo : \n")
        #créer une variable bot égale à Abdel.exe



    #créer une variable otherGame et lui associer le retour de l'exécution de la fonction input pour demander ("Voulez-vous rejouer ? oui ou non : \n")
    #si otherGame est égal à oui
        #alors afficher ("C'est reparti !")
        #alors duoMode est vrai
        #alors game est vrai
        #alors tablegame est égal à [['-','-','-'],['-','-','-'],['-','-','-']]
    #sinon si otherGame est égal à non
        #alors afficher ("A bientôt !")
        #alors casser la boucle
    #sinon
        #alors afficher ("Erreur, enttrez (oui) ou (non) \n")
        #alors utliser la variable otherGame et lui associer le retour de l'exécution de la fonction input pour demander ("Voulez-vous rejouer ? oui ou non : \n")

#FIN