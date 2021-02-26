#_________________________________________Imports_______________________________________________________________________

from tkinter import *
import random

#________________Variables_________________

screenWidth = 700
screenHeight = 600
playerX = 310
playerY = 510
listOfPlayerBullets = []
listOfEnemies = []
listOfEnemyBullets = []

#____________________________________Functions__________________________________________________________________________________________________

#___To delete bullets or enemies when they meet each other_______

def delete():
    global listOfPlayerBullets, listOfEnemyBullets, listOfEnemies
    playerPop = -1
    enBulletPop = -1
    enemyPop = -1
    isMeet = False
    for playerBulletIndex in range(len(listOfPlayerBullets)):
        positionOfBulletPlayer = canvas.coords(listOfPlayerBullets[playerBulletIndex])
        for enBulletIndex in range(len(listOfEnemyBullets)):
            positionOfBulletEn = canvas.coords(listOfEnemyBullets[enBulletIndex])
            if (positionOfBulletPlayer[1] == positionOfBulletEn[1]+15) and (((positionOfBulletEn[0] >= positionOfBulletPlayer[0]) and (positionOfBulletEn[0] <= positionOfBulletPlayer[0]+15)) or ((positionOfBulletEn[0]+10 >= positionOfBulletPlayer[0]) and (positionOfBulletEn[0]+10 <= positionOfBulletPlayer[0]+15))):
                isMeet = True
                canvas.delete(listOfPlayerBullets[playerBulletIndex])
                canvas.delete(listOfEnemyBullets[enBulletIndex])
                playerPop.append(playerBulletIndex)
                playerPop.append(enBulletIndex)

        if not isMeet:
            for enIndex in range(len(listOfEnemies)):
                positionOfEn = canvas.coords(listOfEnemies[enIndex])
                if (positionOfBulletPlayer[1] == positionOfEn[1]+70) and (((positionOfBulletPlayer[0] >= positionOfEn[0]) and (positionOfBulletPlayer[0] <= positionOfEn[0]+55)) or ((positionOfBulletPlayer[0]+15 >= positionOfEn[0]) and (positionOfBulletPlayer[0]+15 <= positionOfEn[0]+55))):
                    canvas.delete(listOfPlayerBullets[playerBulletIndex])
                    canvas.delete(listOfEnemies[enIndex])
                    playerPop.append(playerBulletIndex)
                    playerPop.append(enIndex)
            
    
    if playerPop != -1:
        listOfPlayerBullets.pop(playerPop)
        if isMeet:
            listOfEnemyBullets.pop(enBulletPop)
        else:
            listOfEnemies.pop(enemyPop)

    canvas.after(1, delete)

#___To move all the bullets of player________________________

def movePlayerBullets():
    global listOfPlayerBullets
    toPop = []

    #___To check the bullet can move or not______

    for i in range(len(listOfPlayerBullets)):
        oneBullet = listOfPlayerBullets[i]
        bulletPosition = canvas.coords(oneBullet)
        if bulletPosition[1] <= -40:
            canvas.delete(oneBullet)
            toPop.append(i)

    #___To delete bullets which is useless_______

    for index in toPop:
        listOfPlayerBullets.pop(index)

    #___To move bullets up________________________

    for bullet in listOfPlayerBullets:
        canvas.move(bullet, 0, -5)


    canvas.after(10, movePlayerBullets)

#___ToTo display the enemies___________________________

def moveEnemies():
    global listOfEnemies
    toPop = []
    for index in range(len(listOfEnemies)):
        eachEnemy = listOfEnemies[index]
        position = canvas.coords(eachEnemy)
        if position[1] > 550:
            canvas.delete(listOfEnemies[index])
            toPop.append(index)
        canvas.move(eachEnemy, 0, 5)
  
    for i in toPop:
        listOfEnemies.pop(i)

    canvas.after(100, moveEnemies)

#___To move all bullets of enemies___________________

def moveEnemyBullets():
    global listOfEnemyBullets
    toPop = []

    #___To check the bullet can move or not______

    for i in range(len(listOfEnemyBullets)):
        bullet = listOfEnemyBullets[i]
        bulletPosition = canvas.coords(bullet)
        if bulletPosition[1] >= 550:
            canvas.delete(bullet)
            toPop.append(i)

    #___To delete bullets which is useless_______

    for index in toPop:
        listOfEnemyBullets.pop(index)

    #___To move bullets up________________________

    for bullet in listOfEnemyBullets:
        canvas.move(bullet, 0, 5)

    canvas.after(10, moveEnemyBullets)

#___To move left by key______________________________

def onKeyleft(event):
    global playerX
    if playerX > 10:
        playerX -= 10
    canvas.moveto(player, playerX, playerY)

#___To move right by key_____________________________

def onKeyRight(event):
    global playerX
    if playerX < 610:
        playerX += 10
    canvas.moveto(player, playerX, playerY)

#___To move up by key________________________________

def onKeyUp(event):
    global playerY
    if playerY > 10:
        playerY -= 10
    canvas.moveto(player, playerX, playerY)

#___To move down by key______________________________

def onKeyDown(event):
    global playerY
    if playerY < 510:
        playerY += 10
    canvas.moveto(player, playerX, playerY)

#___Player creates a bullet__________________________________

def createBullet(event):
    global listOfPlayerBullets, toKill
    playerPosition = canvas.coords(player)
    toKill = canvas.create_image(playerPosition[0] + 32.5, playerPosition[1] - 15, anchor=NW, image = gun)

    listOfPlayerBullets.append(toKill)

#___Enemies create a bullet_______________________________

def enemyCreateBullet():
    creator = random.choice(listOfEnemies)
    position = canvas.coords(creator)
    enGun = canvas.create_image(position[0] + 22.5, position[1] + 70, anchor=NW, image = enemyBullet)
    listOfEnemyBullets.append(enGun)
    canvas.after(4000, enemyCreateBullet)

#___Create an enemy________________________________________

def createEnemy():
    global listOfEnemies
    enemy = canvas.create_image(random.randrange(10, 630), -60, anchor=NW, image=enemyImage)
    listOfEnemies.append(enemy)
    canvas.after(3000, createEnemy)

#_______________________Create Window____________________

root = Tk()
root.geometry(str(screenWidth) + "x" + str(screenHeight))
root.title('Pro-Developer')
root.resizable(False, False)
canvas = Canvas(root)
canvas.pack(expand=True, fill="both")

#________________To display background image and player__________________

bgImage = PhotoImage(file='pictures/bg.gif')
gun = PhotoImage(file='pictures/playerBullet.gif')        # size of the bullet (15x30)
enemyBullet = PhotoImage(file='pictures/enBullet.gif')    # size of the bullet (10x15)
playerImage = PhotoImage(file='pictures/player.gif')      # size of the player (80x80)
enemyImage = PhotoImage(file='pictures/enemy.gif')        # size of the player (55x70)

background = canvas.create_image(700, 600, anchor=SE, image=bgImage)
player = canvas.create_image(playerX, playerY, anchor=NW, image=playerImage)

#___Calling functions_______________

createEnemy()
moveEnemies()
enemyCreateBullet()
moveEnemyBullets()
movePlayerBullets()
delete()

#___Arrow keys to move______________

root.bind('<s>', onKeyleft)
root.bind('<d>', onKeyRight)
root.bind('<a>', onKeyUp)
root.bind('<f>', onKeyDown)
root.bind('<\>', createBullet)

root.mainloop()

