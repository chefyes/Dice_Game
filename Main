import random
import math
from tkinter import *
import tkinter as tk
from Player import Player

print("******Welcome to my program!*****")
#Menu
running = True
while running:
    print("What would you like to do?\n\t1.)Play dice\n\t2.)Play Minecraft\
            \n\t3.)End program")
    choice = int(input(">> "))
    #Dice game
    if choice == 1:
        #Initial Values
        temp = (0, 0, 0)
        listOfPlayers = []
        totalDiceRolls = []
        
        master = Tk()
        master.title("Main Menu")

        w = 200
        h = 120
        screenW = 300
        screenH = 144
        
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        playerNumber = 1
        tempPlayer = 0
        roundNum = 1
        #timesPlayed = 1
        
        def playGame():

            def addPlayer():
                dicePerPlayer = int(int(numOfStartDice.get()) / int(numOfPlayers.get()))
                
                def add():
                    diceRolls = []
                    player = Player(playerName.get(), dicePerPlayer, diceRolls)
                    player.setDice()
                    for rolls in player.getDiceRolls():
                        totalDiceRolls.append(rolls)
                    listOfPlayers.append(player)
                    playerName.delete(0, END)
                    top.destroy()
                    
                for label in screen.pack_slaves():
                    label.pack_forget()
                for players in range(int(numOfPlayers.get())):
                    top = Toplevel(screen)
                    top.geometry('%dx%d+%d+%d' % (210, 75, x, y))
                    Label(top, text = "Player name: ").grid(row = 0)

                    playerName = Entry(top)
                    playerName.grid(row = 0, column = 2)

                    addButton = Button(top, text = "Add", command = add)
                    addButton.grid(row = 1, column = 1)
                    screen.wait_window(top)

                start()
            
            def start():
                global playerNumber
                global tempPlayer
                def startOver():
                    screen.destroy()
                    allBets.destroy()
                    master.destroy()

                def checkRolls():
                    rollWind = Toplevel()

                    Label(rollWind, text = listOfPlayers[playerNumber - 1].getDiceRolls()).grid(row = 0)
                    rollWind.geometry('%dx%d+%d+%d' % (210, 75, x, y))
                    
                def betNope():
                    global temp
                    global roundNum
                    tempamount = int(temp[0])
                    tempvalue = int(temp[2])

                    cnt = 0

                    for value in totalDiceRolls:
                        if value == tempvalue or value == 1:
                            cnt += 1

                    if cnt < tempamount:
                        #print(listOfPlayers[tempPlayer - 1].getName() + " lost!")
                        listOfPlayers[tempPlayer - 1].decNumOfDice()
                
                        Label(allBets, text = "Round over! " + str(totalDiceRolls)).pack()
                        Label(allBets, text = str(listOfPlayers[tempPlayer - 1].getName()) + " loses one die." + \
                              " End of round " + str(roundNum)).pack()
                        listOfPlayers[tempPlayer - 1].incDiceLost()
                        roundNum += 1
                        temp = (0, 0, 0)
                        totalDiceRolls.clear()
                        for players in listOfPlayers:
                            if players.getDiceLost() == int(int(numOfStartDice.get()) / int(numOfPlayers.get())):
                                Label(allBets, text = "Game over! " + players.getName() + " lost!").pack()
                                newGame = Button(allBets, text = "New Game", command = startOver).pack()
                            players.setDice()
                            for rolls in players.getDiceRolls():
                                totalDiceRolls.append(rolls)
                        start()

                    else:
                        #print(listOfPlayers[playerNumber - 1].getName() + " lost!")
                        listOfPlayers[playerNumber - 1].decNumOfDice()

                        Label(allBets, text = "Round over! " + str(totalDiceRolls)).pack()
                        Label(allBets, text = str(listOfPlayers[playerNumber - 1].getName()) + " loses one die." + \
                              " End of round " + str(roundNum)).pack()
                        listOfPlayers[playerNumber - 1].incDiceLost()
                        roundNum += 1
                        temp = (0, 0, 0)
                        totalDiceRolls.clear()
                        for players in listOfPlayers:
                            if players.getDiceLost() == int(int(numOfStartDice.get()) / int(numOfPlayers.get())):
                                Label(allBets, text = "Game over! " + players.getName() + " lost!").pack()
                                newGame = Button(allBets, text = "New Game", command = startOver).pack()
                            players.setDice()
                            for rolls in players.getDiceRolls():
                                totalDiceRolls.append(rolls)
                        start()

                def betRightOn():
                    global temp
                    global roundNum
                    tempamount = int(temp[0])
                    tempvalue = int(temp[2])
                    
                    cnt = 0

                    for value in totalDiceRolls:
                        if value == tempvalue or value == 1:
                            cnt += 1
                            
                    if cnt == tempamount:
                        #print(listOfPlayers[tempPlayer - 1].getName() + " lost!")
                        listOfPlayers[tempPlayer - 1].decNumOfDice()

                        Label(allBets, text = "Round over! " + str(totalDiceRolls)).pack()
                        Label(allBets, text = str(listOfPlayers[tempPlayer - 1].getName()) + " loses one die." + \
                              " End of round " + str(roundNum)).pack()
                        listOfPlayers[tempPlayer - 1].incDiceLost()
                        roundNum += 1
                        temp = (0, 0, 0)
                        totalDiceRolls.clear()
                        for players in listOfPlayers:
                            if players.getDiceLost() == int(int(numOfStartDice.get()) / int(numOfPlayers.get())):
                                Label(allBets, text = "Game over! " + players.getName() + " lost!").pack()
                                newGame = Button(allBets, text = "New Game", command = startOver).pack()
                            players.setDice()
                            for rolls in players.getDiceRolls():
                                totalDiceRolls.append(rolls)
                        start()

                    else:
                        #print(listOfPlayers[playerNumber - 1].getName() + " lost!")
                        listOfPlayers[playerNumber - 1].decNumOfDice()

                        Label(allBets, text = "Round over! " + str(totalDiceRolls)).pack()
                        Label(allBets, text = str(listOfPlayers[playerNumber - 1].getName()) + " loses one die." + \
                              " End of round " + str(roundNum)).pack()
                        listOfPlayers[playerNumber - 1].incDiceLost()
                        roundNum += 1
                        temp = (0, 0, 0)
                        totalDiceRolls.clear()
                        for players in listOfPlayers:
                            if players.getDiceLost() == int(int(numOfStartDice.get()) / int(numOfPlayers.get())):
                                Label(allBets, text = "Game over! " + players.getName() + " lost!").pack()
                                newGame = Button(allBets, text = "New Game", command = startOver).pack()
                            players.setDice()
                            for rolls in players.getDiceRolls():
                                totalDiceRolls.append(rolls)
                        
                        start()

                def enterBet():
                    global playerNumber
                    global tempPlayer
                    global temp
                    
                    string = "Current bet: "
                    cnt = 0

                    betAmount = bet.get().partition(":")
                    
                    amount = int(betAmount[0])
                    value = int(betAmount[2])

                    tempamount = int(temp[0])
                    tempvalue = int(temp[2])
                    
                    if amount < 0 or value <= 1 or value > 6:
                        errorPopup = Toplevel()
                        Label(errorPopup, text = "Improper bet, Try again").pack()
                    elif amount < tempamount or (amount == tempamount and value <= tempvalue):
                        errorPopup = Toplevel()
                        Label(errorPopup, text = "Betting error, Try again").pack()
                        Label(errorPopup, text = "Current bet: " + str(tempamount) + " " + str(tempvalue) + "'s").pack()
                    else:
                        Label(allBets, text = "Current bet: " + str(amount) + " " + str(value) + "'s").pack()

                        temp = betAmount
                        if playerNumber ==  math.trunc(int(numOfPlayers.get())):
                            tempPlayer = playerNumber
                            playerNumber = 1
                            start()
                        else:
                            tempPlayer = playerNumber
                            playerNumber += 1
                            start()
                        mainloop()
                
                for label in screen.pack_slaves():
                    label.pack_forget()

                screen.geometry('%dx%d+%d+%d' % (screenW, screenH, screenX, screenY))
                
                Label(screen, text = "Player " + str(playerNumber) + ", " + listOfPlayers[playerNumber - 1].getName()).pack(anchor = "w")
                bet = Entry(screen)
                
                bet.insert(10, "Q:V")

                checkDice = Button(screen, text = "Check Dice", command = checkRolls)
                nope = Button(screen, text = "Nope", command = betNope)
                righton = Button(screen, text = "Right On", command = betRightOn)
                enterBet = Button(screen, text = "Bet", command = enterBet)
                
                enterBet.pack()
                bet.pack()
                checkDice.pack(anchor = "w")
                nope.pack()
                righton.pack(anchor = "e")  
             
            screen = Tk()
            screen.title("Dice")
            
            screenWS = screen.winfo_screenwidth()
            screenHS = screen.winfo_screenheight()
            screenX = (screenWS/2) - (screenW/2)
            screenY = (screenHS/2) - (screenH/2)

            screen.geometry('%dx%d+%d+%d' % (w, h, screenX, screenY))
            
            allBets = Tk()
            allBets.title("Game progress")
            allBets.geometry('%dx%d+%d+%d' % (300, 600, x + 300, y - 200))

            numOfStartDice = Entry(screen)            
            numOfPlayers = Entry(screen)
            
            Label(screen, text = "Number of total dice").pack(anchor = "w")
            numOfStartDice.pack(fill = "x")
            Label(screen, text = "Number of players").pack(anchor = "w")
            numOfPlayers.pack(fill = "x")

            begin = Button(screen, text = "Next", command = addPlayer)
            begin.pack()
            
            mainloop()

        def showInstructions():
            instructMenu = Tk()
            instructMenu.title("Instructions")
            instructMenu.geometry('%dx%d+%d+%d' % (500, 100, x, y))
            Label(instructMenu, text = "1.)Enter a bet with the quantity followed by the value. (ex. \"8:6\")\n"
                "2.)After a bet, the next may call/type \"Nope\" or \"Right On\" at any time\n"
                "3.)The quantity must be greater than or equal to the previous bet's quantity\n"
                "4.)If the quantity is equal then the value must be greater than the previous bet's value").pack(side = 'top')
                        
        Label(master, text = "Welcome to the dice game!").pack()
            
        startGame = Button(master, text = "Play", command = playGame)
        instructions = Button(master, text = "Instructions", command = showInstructions)
        
        startGame.pack()
        instructions.pack()

        mainloop()
        
    elif choice == 2:
        print("Just kidding lol go buy the game.\n")
    elif choice == 3:
        print("Good bye!")
        running = False

            
        
        
        
        
    
