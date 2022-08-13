
#This code is for tic tac toe game and coded by Rolando Garcia
#refers to one human player vs a machine 

import time
import random
import os


#Method to start the game
def start_game():
    print ("Welcome to tic tac toe game")
    time.sleep(2)
    while True:
        symbolType = input ("To start the game please choose X or select O\n:  ")
        symbolType = symbolType.upper()
        if symbolType=="X":
            player="X"
            machine="O"
            break

        elif symbolType=="O":
            player="O"
            machine="X"
            break
        else:
            print("Please enter a valid symbol") #in case of entering different than "O" or "X"
    return(player,machine)
        
# Creating table to show on the screen
def table():
    print ("Game TIC TAC TOE")
    print()
    print("     |       |       ")
    print("1 {}  |2 {}   |3        ".format(matriz[0],matriz[1],matriz[2]))
    print("     |       |       ")
    print("-------------------")
    print("4 {}  |5 {}   |6        ".format(matriz[3],matriz[4],matriz[5]))
    print("     |       |       ")
    print("-------------------")
    print("     |       |       ")
    print("7 {}  |8 {}   |9        ".format(matriz[6],matriz[7],matriz[8]))
    print("     |       |       ")

# Defining game results, either win or tie for player and the machine
def tie(matriz):
    tie=True
    i=0
    while (tie==True and i <9):
        if matriz[i]==" ":
            tie=False
        i=i+1
    return tie

def win(matriz):
    if (matriz[0]==matriz[1]==matriz[2]!= " " or matriz[3]==matriz[4]==matriz[5]!= " " or matriz[6]==matriz[7]==matriz[8]!= " " or
       matriz[0]==matriz[3]==matriz[6]!= " " or  matriz[1]==matriz[4]==matriz[7]!= " " or matriz[2]==matriz[5]==matriz[8]!= " " or 
       matriz[0]==matriz[4]==matriz[8]!= " " or matriz[2]==matriz[4]==matriz[6]!= " "): 
       return True
    else:
       return False

#Catching movements "player and machine"

def player_movement(): #when player is selecting a box
    while True:
        positions = [1,2,3,4,5,6,7,8,9]
        box = int(input("Please choose a box"))
        if box not in positions:
            print ("This box is not available")
#continue
        else:
            if matriz[box-1]== " ":
                matriz[box-1]== player 
                break 
            else:
                print("Box not available")

def machine_movement(): #when machine randoms selects an available box
    positions=[0,2,3,4,5,6,7,8]
    box=9
    stop= False

    for i in positions:
        copy=list(matriz)
        if copy[i] == " ":
            copy[i]=machine
            if win(copy)==True:
                box=i
    if box==9:
        for j in positions:
            copy=list(matriz)
            if copy[j]==" ":
                copy[j]=player
                if win(copy)==True:
                    box=j
    if box==9:
        while(not stop):
            box=random.randint(0,8)
            if matriz[box]==" ":
                stop=True
    matriz[box]=machine


#Playing now....
while True:
    matriz=[" "]*9
    os.system("cls") #cleaning to start the game
    player,machine=start_game()
    game=True
    winner=0

    while game:
        winner=winner+1
        os.system("cls")
        table()


        if win(matriz):
            if winner%2==0:
                print("Player wins '\U0001F601' ")
                print ("Game over")
                print("Restarting game now...")
                time.sleep(5)
                game=False
            else:
                print("Machine wins")
                print("Game over")
                print("Restarting game now...")
                time.sleep(5)
                game=False
        elif tie(matriz):
            print("Tie '\U0001F910' ")
            print("Game over ")
            print("Restarting game now...")
            time.sleep(5)
            game=False
    
        elif winner%2==0:
            print("Machine thinking to choose an option '\U0001F910' ") #Codenumber refers to emoji smiling face 
            time.sleep(2)
            machine_movement()
    
        else:
            player_movement()








    
    



