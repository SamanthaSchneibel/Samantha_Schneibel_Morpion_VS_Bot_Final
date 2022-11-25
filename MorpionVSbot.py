#DEBUT

#on admet qu'une fonction random existe qui renvoie un chiffre aléatoire
from random import randint

#créer une liste tableJeu qui servira de table de jeu [['-','-','-'],['-','-','-'],['-','-','-']]
tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]

#définir la fonction showTable qui renvoie la table de jeu
def showTable(tableGame): 
    print("\n--------------")
    for row in tableGame :
        for item in row:
            print(item, end="  ")
        print()
    print("--------------\n")

#définir la fonction caseFilled pour savoir quelles cases sont utilisées
def caseFilled(tableGame, posx, posy):
    if tableGame[posx][posy] == '-':
        return False
    else:
        return True

#definir la fonction is_player_win
def is_player_win(tableGame,form):
    if tableGame[0][0] == tableGame[0][1] == tableGame[0][2] == form:
        return True
    elif tableGame[1][0] == tableGame[1][1] == tableGame[1][2]== form:
        return True
    elif tableGame[2][0] == tableGame[2][1] == tableGame[2][2]== form:
        return True
    elif tableGame[0][0] == tableGame[1][0] == tableGame[2][0]== form:
        return True
    elif tableGame[0][1] == tableGame[1][1] == tableGame[2][1]== form:
        return True
    elif tableGame[0][2] == tableGame[1][2] == tableGame[2][2]== form:
        return True
    elif tableGame[0][0] == tableGame[1][1] == tableGame[2][2]== form:
        return True
    elif tableGame[0][2] == tableGame[1][1] == tableGame[2][0]== form:
        return True
    else:
        return False

#définir la fonction is_tableGame_filled
def is_tableGame_filled(tableGame):
    for row in tableGame:
        for item in row:
            if item == '-':
                return False
    return True

#définir la fonction deuxParmiTrois de paramètres (a, b, c et deja_existant)
def deuxParmiTrois(a, b, c, deja_existant):
    if a == b == deja_existant and c == "-":
        return 3
    if c == a == deja_existant and b == "-":
        return 2
    if c == b == deja_existant and a == "-":
        return 1
    else :
        return [] 

#définir la fonction unParmiTrois de paramètres (a, b et c)
def unParmiTrois(a, b, c):
    if a == "O" and b == c == "-":
        return 1
    elif c == "O" and a == b == "-":
        return 3
    elif b == "O" and c == a == "-":
        return 2
    else:
        return []

#définir la fonction gagner de paramètres (tableGame et playerBotShoot)
def gagner(tableGame, playerBotShoot):
    for i in range(3):
        ligne = deuxParmiTrois(tableGame[i][0], tableGame[i][1], tableGame[i][2], playerBotShoot)
        colonne = deuxParmiTrois(tableGame[0][i], tableGame[1][i], tableGame[2][i], playerBotShoot)
        if ligne != []:
            return [i, ligne-1]
        if colonne != []:
            return [colonne-1, i]
    diag1 = deuxParmiTrois(tableGame[0][0], tableGame[1][1], tableGame[2][2], playerBotShoot)
    diag2 = deuxParmiTrois(tableGame[0][2], tableGame[1][1], tableGame[2][0], playerBotShoot)
    if diag1 != []:
        return [diag1-1, diag1-1]
    if diag2 != []:
        return [diag2-1, 3-diag2]
    return []

#éfinir la fonction pasGagner de paramètres (tableGame et playerBotShoot)
def pasGagner(tableGame, playerBotShoot):
    for i in range(2):
        ligne = unParmiTrois(tableGame[i*2][0], tableGame[i*2][1], tableGame[i*2][2])
        colonne = unParmiTrois(tableGame[0][i*2], tableGame[1][i*2], tableGame[2][i*2])
        if ligne != []:
            return [i*2, ligne]
        if colonne != []:
            return [colonne, i*2]
    diag1 = unParmiTrois(tableGame[0][0], tableGame[1][1], tableGame[2][2])
    diag2 = unParmiTrois(tableGame[0][2], tableGame[1][1], tableGame[2][0])
    if diag1 != []:
        return [diag1, diag1]
    if diag2 != []:
        return [diag2, 2-diag2]
    return []

#définir la fonction du bot   
def bot(tableGame, playerSoloShoot, playerBotShoot):
    wino = gagner(tableGame, playerBotShoot)
    if tableGame[1][1] == "-":
        tableGame[1][1] = playerBotShoot
    elif tableGame[1][1] == "X" and tableGame[0][0] == "-":
        tableGame[0][0] = playerBotShoot
    elif wino != []:
        tableGame[wino[0]][wino[1]] = playerBotShoot
    elif tableGame[0][0] == "X" and tableGame[2][2] == "X":
        tableGame[1][0] = playerBotShoot
    elif tableGame[0][2] == "X" and tableGame[2][0] == "X":
        tableGame[1][2] = playerBotShoot
    elif tableGame[2][2] == "X" and tableGame[1][2] == "X":
        tableGame[0][2] = playerBotShoot
    elif gagner(tableGame, playerSoloShoot) != []:
        tableGame[gagner(tableGame, playerSoloShoot)[0]][gagner(tableGame, playerSoloShoot)[1]] = playerBotShoot
    elif pasGagner(tableGame, playerBotShoot) != []:
        a_jouer=pasGagner(tableGame, playerBotShoot)
        tableGame[a_jouer[0]][a_jouer[1]] = playerBotShoot
    elif tableGame[0][0] == "-":
        tableGame[0][0] = playerBotShoot
    elif tableGame[0][2] == "-":
        tableGame[0][2] = playerBotShoot
    elif tableGame[2][0] == "-":
        tableGame[2][0] = playerBotShoot
    elif tableGame[2][2] == "-":
        tableGame[2][2] = playerBotShoot
    elif tableGame[0][1] == "-":
        tableGame[0][1] = playerBotShoot
    elif tableGame[1][0] == "-":
        tableGame[1][0] = playerBotShoot
    elif tableGame[1][2] == "-":
        tableGame[1][2] = playerBotShoot
    elif tableGame[2][1] == "-":
        tableGame[2][1] = playerBotShoot

#définir la fonction des coups
def coup(playerTurn, playerShoot, playerSoloShoot, playerBotShoot, playerSolo):
    game = True
    while game == True:
        if playerTurn == playerSolo:
            choiceX = int(input("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n"))
            choiceY = int(input("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n"))
            if choiceX in [0,1,2] and choiceY in [0,1,2]:
                if caseFilled(tableGame, choiceX, choiceY) != True:
                    tableGame[choiceX][choiceY] = playerShoot
            elif choiceX not in [0,1,2] and choiceY not in [0,1,2]:
                print("Erreur, rentrez un numéro valide \n")
                coup(playerTurn, playerShoot, playerSoloShoot, playerBotShoot, playerSolo)
                    
            showTable(tableGame)
            
            if is_player_win(tableGame, playerSoloShoot):
                if playerSolo == "Antoine":
                    print(playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                else:
                    print(playerBot +  " à gagné la partie ! :) \n")
                game = False
                break

            elif is_tableGame_filled(tableGame):
                if playerSolo == "Antoine":
                    print(playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                else:
                    print("Egalité ! :/ \n")
                game = False
                break
            
            bot(tableGame, playerSoloShoot, playerBotShoot)
            
            showTable(tableGame)
            
            if is_player_win(tableGame, playerBotShoot):
                if playerSolo == "Antoine":
                    print(playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                else:
                    print(playerBot +  " à gagné la partie ! :) \n")
                game = False
                break

            elif is_tableGame_filled(tableGame):
                if playerSolo == "Antoine":
                    print(playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                else:
                    print("Egalité ! :/ \n")
                break

        elif playerTurn == playerBot:
        
            bot(tableGame, playerSoloShoot, playerBotShoot)

            showTable(tableGame)
            
            if is_player_win(tableGame, playerBotShoot):
                if playerSolo == "Antoine":
                    print(playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                else:
                    print(playerBot +  " à gagné la partie ! :) \n")
                game = False
                break

            elif is_tableGame_filled(tableGame):
                if playerSolo == "Antoine":
                    print(playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                else:
                    print("Egalité ! :/ \n")
                game = False
                break

            choiceX = int(input("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n"))
            choiceY = int(input("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n"))
            if choiceX in [0,1,2] and choiceY in [0,1,2]:
                if caseFilled(tableGame, choiceX, choiceY) != True:
                    tableGame[choiceX][choiceY] = playerShoot
            elif choiceX not in [0,1,2] and choiceY not in [0,1,2]:
                print("Erreur, rentrez un numéro valide \n")
                coup(playerTurn, playerShoot, playerSoloShoot, playerBotShoot)
                    
            showTable(tableGame)
            
            if is_player_win(tableGame, playerSoloShoot):
                if playerSolo == "Antoine":
                    print(playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                else:
                    print(playerBot +  " à gagné la partie ! :) \n")
                game = False
                break

            if is_tableGame_filled(tableGame):
                if playerSolo == "Antoine":
                    print(playerSolo +  ", notre maître à tous à gagné la partie ! :) \n")
                else:
                    print("Egalité ! :/ \n")
                game = False
                break

#définir la fonction pour lancer le Jeu
def menu():
    house = True
    while house == True:
        home = input("Bienvenue dans le célèbre jeu du Morpion ! Affrontez-vous en 1vs1 ou confrontez-vous à notre bot à vos risques et périls :) \nVoulez-vous un rappel des règles ? oui ou non : \n")
        if home == "oui":
            print("Le jeu du Morpion se joue sur un tableau de 3 par 3. Le but du jeu est d'aligner avant son adversaire 3 symboles identiques (les X ou les O) horizontalement, verticalement ou en diagonale.")
            startGame = input("Voulez-vous jouer ? oui ou non : \n")
        elif home == "non":
            startGame = input("Voulez-vous jouer ? oui ou non : \n")
        else:
            print("Erreur, entrez 'oui' ou 'non' \n")
        
        if startGame == "oui":
            modeGame = input("Choissiez un mode de jeu : 1vs1 = 1 / 1vsBot = 2 \n")
            if modeGame == "2":
                playerSolo = input("Choisissez votre pseudo : \n")
                soloMode(playerSolo)   
            elif modeGame =="1":
                playerOne = input("Joueur X choisissez votre pseudo : \n")
                playerTwo = input("Joueur O choisissez votre pseudo : \n")
                duoMode(playerOne, playerTwo)
            else:
                print("Erreur, entrez '1' ou '2' \n")
       
        elif startGame == "non":
            print("Tant pis, à bientôt !")
            house = False
        else:
            print("Erreur, entrez 'oui' ou 'non' \n")

#définir la fonction du mode 1 vs Bot
def soloMode(playerSolo):
    global tableGame, playerBot
    playerBot = 'Abdel.exe'
    playerSoloShoot = 'X'
    playerBotShoot = 'O'
    
    choiceTurn = input("Qui commence ? " + playerSolo + " = 1 / Bot = 2 \n")

    if choiceTurn == "1":
        playerTurn = playerSolo
        playerShoot = playerSoloShoot
    elif choiceTurn == "2":
        playerTurn = playerBot
        playerShoot = playerSoloShoot
    else:
        print("Erreur, entrez '1' ou '2' \n")
        choiceTurn = input("Qui commence ? " + playerSolo + " = 1 / Bot = 2 \n")

    showTable(tableGame)
    coup(playerTurn, playerShoot, playerSoloShoot, playerBotShoot, playerSolo)

    rejouer = True
    while rejouer == True:
        otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
        if otherGame == "oui":
            print("C'est reparti !")
            tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
            soloMode(playerSolo)
        elif otherGame == "non":
            print("A bientôt !")
            rejouer = False
        else:
            print("Erreur, entrez 'oui' ou 'non' \n")

#définir la fonction du mode 1 vs 1
def duoMode(playerOne, playerTwo):
    tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
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
        while correctShoot == False :
            choiceX = int(input("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n"))
            choiceY = int(input("Choisissez la ligne à modifier (ligne 1 = 0 / ligne 2 = 1 / ligne 3 = 2) : \n"))
            if caseFilled(tableGame, choiceX, choiceY) != True:
                tableGame[choiceX][choiceY] = playerShoot
                correctShoot = True 
        showTable(tableGame)

        if is_player_win(tableGame, playerOneShoot):
            print("Le joueur " + playerOne +  " à gagné la partie ! :) ")
            break
        
        if is_player_win(tableGame, playerTwoShoot):
            print("Le joueur " + playerTwo +  " à gagné la partie ! :) ")
            break

        if is_tableGame_filled(tableGame):
            print("Egalité ! :/")
            break

        if playerShoot == playerOneShoot:
            playerShoot = playerTwoShoot
            playerTurn = playerTwo
        else : 
            playerShoot = playerOneShoot
            playerTurn = playerOne

        correctShoot = False
    
    rejouer = True
    while rejouer == True:
        otherGame = input("Voulez-vous rejouer ? oui ou non : \n")
        if otherGame == "oui":
            print("C'est reparti !")
            tableGame = [['-','-','-'],['-','-','-'],['-','-','-']]
            duoMode(playerOne, playerTwo)
        elif otherGame == "non":
            print("A bientôt !")
            rejouer = False
        else:
            print("Erreur, entrez 'oui' ou 'non' \n")

menu()

#FIN