#DEBUT

#on admet qu'une fonction random existe qui renvoie un chiffre aléatoire
from random import randint

#créer la surface du jeu
tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]

#créer la fonction tableGame qui renvoie la surface du jeu
def showTable(tableGame):
    print("\n--------------")
    for row in tableGame :
        for item in row:
            print(item, end="  ")
        print()
    print("--------------\n")

#créer la fonction caseFilled qui vérifie que le coup d'un joueur est valide
def caseFilled(board, posx, posy):
    if board[posx][posy] == '-':
        return False
    else:
        return True

#créer une fonction qui renvoie si un joueur gagne
def is_player_win(board, player):
    win = None

    n = len(board)

    #on vérifie les lignes
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    #on vérifie les colonnes
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    #on vérifie les diagonales
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

#on vérifie si la surface du jeu est pleine 
def is_board_filled(board):
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True

menu = input("Bienvenue dans le célèbre jeu du Morpion ! Affrontez-vous en 1vs1 ou confrontez-vous à notre bot à vos risques et périls :) \nVoulez-vous un rappel des règles ? oui ou non : \n")
if menu == "oui":
    print("Le jeu du Morpion se joue sur un tableau de 3 par 3. Le but du jeu est d'aligner avant son adversaire 3 symboles identiques (les X ou les O) horizontalement, verticalement ou en diagonale.")
elif menu == "non":
    print()
else:
    print("Error, entrez (oui) ou (non) \n")
    menu = input("Bienvenue dans le célèbre jeu du Morpion ! Affrontez-vous en 1vs1 ou confrontez-vous à notre bot à vos risques et périls :) \nVoulez-vous un rappel des règles ? oui ou non : \n")
    
game = input("Voulez-vous jouer ? oui ou non : \n")
if game == "oui":
    game = True
elif game == "non":
    game == False
    print("Tant pis, à bientôt !")
else:
    print("Erreur, entrez (oui) ou (non) \n")
    game = input("Voulez-vous jouer ? oui ou non : \n")

while game == True:
    gameMode = int(input("Choissiez un mode de jeu : 1vs1 = 1 / 1vsBot = 2 \n"))
    if gameMode == 1:
        duoMode = True
    elif gameMode == 2:
        soloMode = True
    else:
        print("Erreur, entrez (1) ou (2) \n")
        gameMode = int(input("Choissiez un mode de jeu : 1vs1 = 1 / 1vsBot = 2 \n"))
        
    while duoMode == True:
        soloMode = False
        playerOne = input("Joueur X choisissez votre pseudo : \n")
        playerTwo = input("Joueur O choisissez votre pseudo : \n")

        playerOneShoot = "X"
        playerTwoShoot = "O"
        playerStart = randint(1, 2)
    
        if playerStart == 1:
            playerTurn = playerOne
            playerShoot = playerOneShoot
        else:
            playerTurn = playerTwo
            playerShoot = playerTwoShoot
    
        correctShoot = False
        playerWin = False 
    
        showTable(tableGame)
        while playerWin == False:
            while correctShoot == False:
                print("Au Tour de " + playerTurn + "\n")
                choiceX = int(input("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n"))
                choiceY = int(input("Choisissez la colonne à modifier (colonne 1 = 0 / colonne 2 = 1 / colonne 3 = 2) : \n"))
                if caseFilled(tableGame, choiceX, choiceY) != True:
                    tableGame[choiceX][choiceY] = playerShoot
                    correctShoot = True 
            showTable(tableGame)

            if is_player_win(tableGame, playerShoot):
                print("Le joueur " + playerTurn +  " à gagné la partie ! :) ")
                duoMode = False
                game = False
                break
        
            if is_board_filled(tableGame):
                print("Egalité ! :/")
                duoMode = False
                game = False
                break

            if playerShoot == playerOneShoot:
                playerShoot = playerTwoShoot
                playerTurn = playerTwo
            else: 
                playerShoot = playerOneShoot
                playerTurn = playerOne

            correctShoot = False

    while soloMode == True:
        duoMode = False
        player = input("Entrez votre pseudo : \n")
        bot = "Abdel.exe"




    otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
    if otherGame == "oui":
        print("C'est reparti !")
        duoMode = True
        game = True
        tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
    elif otherGame== "non":
        print("A bientôt !")
        break
    else:
        print("Erreur, enttrez (oui) ou (non) \n")
        otherGame = input("Voulez-vous rejouer ? oui ou non : \n")

#FIN