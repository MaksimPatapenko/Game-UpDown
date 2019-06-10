# Game
# Genre: UpDown


import os
import random

def clear(): #FUNCTION CLEANING CONSOLE 
  os.system('clear')
clear()

#1.Create a random map
#Create a map where " " is the floor and "#" is the wall
sizeI = 20
sizeJ = 20

def Map():
    m = []
    map = [] # Map for the game
    
    for i in range(sizeI):
        for j in range(sizeJ):
                m += [random.randrange(0,101)]
                # Change all the numbers to " " or "#". Fill in such a way that 70% will be " ", and 30% - "#"
                if m[j] > 70:
                    m[j] = '#' 
                elif m[j] <= 70:
                    m[j] = ' '
        map += [m]
        m = []
        
    #Create walls around the map.
    for i in range(sizeJ):
        map[i].insert(0, '#') #added a wall to the right of the map
        map[i].insert(sizeI + 2, '#') #added a wall to the left of the map
    upBoarder = []
    
    for i in range(sizeI + 2): 
        upBoarder += '#'
        
    map.insert(0, upBoarder) #added a wall on top of the map
    map.insert(sizeJ + 1, upBoarder) #added a wall at the bottom of the map
    return map


#2.Place a room with an exit under lock
cordI = random.randrange(1, sizeI - 4) #Let's create the origin of the place from which we will change part of the map to our room with the exit.
cordJ = random.randrange(1, sizeJ - 4)

def Room(map): #THE FUNCTION OF ACCOMMODATION OF THE RANDOM ROOM ON THE MAP
    # 2.1.Created the blanks of rooms 3 by 3, where "D" is the DOOR to the room, and $ is the EXIT. "D" - DOOR, "$" - FINISH
    myRooms = [
               [['#', 'D', '#' ], ['#', '$', '#' ], ['#', '#', '#' ]], 
               [['#', '#', '#' ], ['#', '$', 'D' ], ['#', '#', '#' ]],
               [['#', '#', '#' ], ['#', '$', '#' ], ['#', 'D', '#' ]], 
               [['#', '#', '#' ], ['D', '$', '#' ], ['#', '#', '#' ]]
               ] 
    myRoom = random.choice(myRooms) #Choose one random room from the list of all rooms (1 of 4)
    for i in range(3):
        for j in range(3):
            map[cordI + i][cordJ + j] = myRoom[i][j]


#3.Place the door key ("K") on the map
def Key(map): #THE FUNCTION OF PLACEMENT OF RANDOM COORDINATES KEY ("K") ON THE MAP
    keyI = random.randrange(1, sizeI + 1) #Create the coordinates of the place where the key will be.
    keyJ = random.randrange(1, sizeJ + 1)
    map[keyI][keyJ] = 'K'
    return map


#4.Creating a starting point ("P")
def Player(map): #FUNCTION OF RANDOM START PLACEMENT
    global playerI
    global playerJ
    playerI = random.randrange(1, sizeI + 1) #Create coordinates START ("P").
    playerJ = random.randrange(1, sizeJ + 1)
    map[playerI][playerJ] = 'P'
    return map


#5.Check passability of map
def Passability(map): #THE FUNCTION OF PASSABILITY OF THE MAP FROM START("P") TO KEY("K") AND UP TO FINISH("$")
    findKey = False
    findDoor = False
    keyInRoom = False
    playerInRoom = False
    
    while not(findKey and findDoor):
        map = Map()
        Room(map)
        Key(map)
        
        #Check "Key in the room?"
        for i in range(3):
            for j in range(3):
                if map[cordI + i][cordJ + j] == 'K':
                    keyInRoom = True
        if keyInRoom:
            #Debugging print ('Has protection worked "key in the room?"')
            keyInRoom = False
            continue
            
        Player(map)
        #Check "player in the room?"
        for i in range(3):
            for j in range(3):
                if map[cordI + i][cordJ + j] == map[playerI][playerJ]:
                    playerInRoom = True
                    
        if playerInRoom:
            #Debugging print ('Has protection worked for the player in the room? "')
            playerInRoom = False
            continue
            
        #Replace passable places around the start with "W"
        if map[playerI + 1][playerJ] == ' ': 
            map[playerI + 1][playerJ] = 'W'
            
        if map[playerI - 1][playerJ] == ' ':
            map[playerI - 1][playerJ] = 'W'
            
        if map[playerI][playerJ - 1] == ' ':
            map[playerI][playerJ - 1] = 'W'
            
        if map[playerI][playerJ + 1] == ' ':
            map[playerI][playerJ + 1] = 'W'
            
        #Replace all passable places with "W" and "X"
        while True: 
            countW = 0
            
            for i in range(sizeI + 1):
                for j in range(sizeJ + 1):
                
                    if map[i][j] == 'W':
                    
                        if map[i + 1][j] == ' ':
                            map[i + 1][j] = 'W'
                            countW += 1
                            
                        elif map[i + 1][j] == 'W':
                            map[i + 1][j] = 'X'
                    
                        if map[i - 1][j] == ' ':
                            map[i - 1][j] = 'W'
                            countW += 1
                            
                        elif map[i - 1][j] == 'W':
                            map[i - 1][j] = 'X'

                        if map[i][j + 1] == ' ':
                            map[i][j + 1] = 'W'
                            countW += 1
                            
                        elif map[i][j + 1] == 'W':
                            map[i][j + 1] = 'X'

                        if map[i][j - 1] == ' ':
                            map[i][j - 1] = 'W'
                            countW += 1
                            
                        elif map[i][j - 1] == 'W':
                            map[i][j - 1] = 'X'
            if countW == 0:
                #Debugging print ('Verification of the "While True" is over ")
                break
                
        #5.1. There is a way from start ("P") to key ("K")
        for i in range(sizeI + 2):
            for j in range(sizeJ + 2):
                if map[i][j] == 'K':
                
                    if map[i + 1][j] == 'W' or map[i + 1][j] == 'X':
                        findKey = True
                        
                    elif map[i - 1][j] == 'W' or map[i - 1][j] == 'X':
                        findKey = True
                        
                    elif map[i][j + 1] == 'W' or map[i][j + 1] == 'X':
                        findKey = True
                        
                    elif map[i][j - 1] == 'W' or map[i][j - 1] == 'X':
                        findKey = True
                        
                #5.2.There is a way from start("P") to door ("D")
                elif map[i][j] == 'D':
                
                    if map[i + 1][j] == 'W' or map[i + 1][j] == 'X':
                        findDoor = True
                        
                    elif map[i - 1][j] == 'W' or map[i - 1][j] == 'X':
                        findDoor = True
                        
                    elif map[i][j + 1] == 'W' or map[i][j + 1] == 'X':
                        findDoor = True
                        
                    elif map[i][j - 1] == 'W' or map[i][j - 1] == 'X':
                        findDoor = True
                        
    for i in range(sizeI + 2):
        for j in range(sizeJ + 2):
        
            if map[i][j] == 'W' or map[i][j] == 'X':
                map[i][j] = ' '
    return map
    
#Create a map if it is passable from start("P") to key("K") and from key("K") to door("D")
map = Passability(map)

for i in range(sizeI + 2): #ВЫВОД КАРТЫ
    for j in range(len(map[i])):
    
        if j < len(map[i]) - 1:
            print(map[i][j], end = ' ')
            
        else:
            print(map[i][j])


#6.Player Movement
#6.1Add input(), to the direction of movement
#6.2 Add protection: abutment into the wall, going beyond the border of the map, into the room without a key
key = False
finish = False

while True:
    print()
    direction = input('Введите направление движения (Up, Down, Left, Right): ').lower()
    
    if direction == 'down':
    
        if map[playerI + 1][playerJ] == '#' or map[playerI + 1][playerJ] == '#':
            continue
            
        elif map[playerI + 1][playerJ] == 'K':
            key = True
            
        elif map[playerI + 1][playerJ] == 'D' and key == False:
            continue
            
        elif map[playerI + 1][playerJ] == '$':
            break
            
        map[playerI + 1][playerJ] = 'P'
        map[playerI][playerJ] = ' '
        playerI += 1

    elif direction == 'up':
    
        if map[playerI - 1][playerJ] == '#' or map[playerI - 1][playerJ] == '#':
            continue
            
        elif map[playerI - 1][playerJ] == 'K':
            key = True
            
        elif map[playerI - 1][playerJ] == 'D' and key == False:
            continue
            
        elif map[playerI - 1][playerJ] == '$':
            finish = True
            
        map[playerI - 1][playerJ] = 'P'
        map[playerI][playerJ] = ' '
        playerI -= 1

    elif direction == 'left':
    
        if map[playerI][playerJ - 1] == '#' or map[playerI][playerJ - 1] == '#':
            continue
            
        elif map[playerI][playerJ - 1] == 'K':
            key = True
            
        elif map[playerI][playerJ - 1] == 'D' and key == False:
            continue
            
        elif map[playerI][playerJ - 1] == '$':
            finish = True
            
        map[playerI][playerJ - 1] = 'P'
        map[playerI][playerJ] = ' '
        playerJ -= 1

    elif direction == 'right':
    
        if map[playerI][playerJ + 1] == '#' or map[playerI][playerJ + 1] == '#':
            continue
            
        elif map[playerI][playerJ + 1] == 'K':
            key = True
            
        elif map[playerI][playerJ + 1] == 'D' and key == False:
            continue
            
        elif map[playerI][playerJ + 1] == '$':
            finish = True
            
        map[playerI][playerJ + 1] = 'P'
        map[playerI][playerJ] = ' '
        playerJ += 1
        
    clear()
    
    for i in range(sizeI + 2): #OUTPUT MAP
        for j in range(len(map[i])):
            if j < len(map[i]) - 1:
                print(map[i][j], end = ' ')
            else:
                print(map[i][j])
    if finish == True:
        break
print()
print('VICTORY!!!! You found a treasure! Congratulations!')
print('Support the project by transferring money to VISA card :)')
print('Card number: 4496 5501 1217 9996')
print('Valid thru: 02/21')
