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

#créer une variable startGame et lui associer le retour de l'exécution de la fonction input pour demander de jouer ou non
startGame = input("Voulez-vous jouer ? oui ou non : \n")
#si starGame est à oui
if startGame == "oui":
    #alors le jeu se lance
    continuer = True
    playerOne = input("Joueur X choisissez votre pseudo : \n")
    playerTwo = input("Joueur O choisissez votre pseudo : \n")
#sinon le jeu s'arrête
elif startGame == "non":
    print("\nTant pis, à une prochaine ! \n")
    continuer = False
#sinon redemander la question (2 chances)
else:
    startGame = input("Voulez-vous jouer ? oui ou non : \n")
    if startGame == "oui":
        continuer = True
        playerOne = input("Joueur X choisissez votre pseudo : \n")
        playerTwo = input("Joueur O choisissez votre pseudo : \n")
    elif startGame == "non":
        print("\nTant pis, à une prochaine ! \n")
        continuer = False
    else:
        startGame = input("Voulez-vous jouer ? oui ou non : \n")
        if startGame == "oui":
            continuer = True
            playerOne = input("Joueur X choisissez votre pseudo : \n")
            playerTwo = input("Joueur O choisissez votre pseudo : \n")
        elif startGame == "non":
            print("\nTant pis, à une prochaine ! \n")
            continuer = False

#tant que la variable continuer est égale à vrai alors le jeu se lance
while continuer == True :
    
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
            break
        
        if is_board_filled(tableGame):
            print("Egalité ! :/")
            break

        if playerShoot == playerOneShoot:
            playerShoot = playerTwoShoot
            playerTurn = playerTwo
        else : 
            playerShoot = playerOneShoot
            playerTurn = playerOne

        correctShoot = False
    
    #créer une variable otherGame et lui associer le retour de l'exécution de la fonction input qui demande si les joueurs veulent refaire une partie
    otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
    #si otherGame est égal à oui alors le jeu se relance
    if otherGame == "oui":
        print("C'est reparti !")
        tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
        continuer = True
    #si otherGame est égal à non alors le jeu s'arrête
    elif otherGame == "non":
        print("A bientôt !")
        continuer = False
    #sinon redemander la question (2 chances)
    else:
        otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
        if otherGame == "oui":
            print("C'est reparti !")
            tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
            continuer = True
        elif otherGame == "non":
            print("A bientôt !")
            continuer = False
        else:
            otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
            if otherGame == "oui":
                print("C'est reparti !")
                tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
                continuer = True
            elif otherGame == "non":
                print("A bientôt !")
                continuer = False

#FIN