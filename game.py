from tkinter import *
import random

#________________Variables_________________
times = 0
screenWidth = 700
screenHeight = 600
playerX = 310
playerY = 510
listOfPlayerBullets = []
listOfEnemies = []
listOfEnemyBullets = []

#____________________________________Functions__________________________________________________________________________________________________

###############___Global Process_____############################################################################################
def globalProcess():
    global times

    times += 1

    toDelete = []
    isMeet = False
    for playerBulletIndex in range(len(listOfPlayerBullets)):
        positionOfBulletPlayer = canvas.coords(listOfPlayerBullets[playerBulletIndex])
        for enBulletIndex in range(len(listOfEnemyBullets)):
            positionOfBulletEn = canvas.coords(listOfEnemyBullets[enBulletIndex])
            if (positionOfBulletPlayer[1] == positionOfBulletEn[1]+15) and (((positionOfBulletEn[0] >= positionOfBulletPlayer[0]) and (positionOfBulletEn[0] <= positionOfBulletPlayer[0]+15)) or ((positionOfBulletEn[0]+10 >= positionOfBulletPlayer[0]) and (positionOfBulletEn[0]+10 <= positionOfBulletPlayer[0]+15))):
                isMeet = True
                toDelete.append(listOfPlayerBullets[playerBulletIndex])
                toDelete.append(listOfEnemyBullets[enBulletIndex])

        if not isMeet:
            for enIndex in range(len(listOfEnemies)):
                positionOfEn = canvas.coords(listOfEnemies[enIndex])
                if (positionOfBulletPlayer[1] == positionOfEn[1]+70) and (((positionOfBulletPlayer[0] >= positionOfEn[0]) and (positionOfBulletPlayer[0] <= positionOfEn[0]+55)) or ((positionOfBulletPlayer[0]+15 >= positionOfEn[0]) and (positionOfBulletPlayer[0]+15 <= positionOfEn[0]+55))):
                    toDelete.append(listOfPlayerBullets[playerBulletIndex])
                    toDelete.append(listOfEnemies[enIndex])
    if len(toDelete) > 0 and isMeet:
        listOfPlayerBullets.remove(toDelete[0])
        listOfEnemyBullets.remove(toDelete[1])
        canvas.delete(toDelete[0])
        canvas.delete(toDelete[1])
    elif len(toDelete) > 0:
        listOfPlayerBullets.remove(toDelete[0])
        listOfEnemies.remove(toDelete[1])
        canvas.delete(toDelete[0])
        canvas.delete(toDelete[1])
    
    #___Move the bullets of the enemies_________________________________________________________________
    if times % 10 == 0:
        toPopEnBullet = []
        for i in range(len(listOfEnemyBullets)):
            bullet = listOfEnemyBullets[i]
            bulletPosition = canvas.coords(bullet)
            if bulletPosition[1] >= 550:
                canvas.delete(bullet)
                toPopEnBullet.append(i)
        for index in toPopEnBullet:
            listOfEnemyBullets.pop(index)
        for bullet in listOfEnemyBullets:
            canvas.move(bullet, 0, 5)

    #___Move all the bullets of player________________________
        toPopPlayerBullet = []
        for i in range(len(listOfPlayerBullets)):
            oneBullet = listOfPlayerBullets[i]
            bulletPosition = canvas.coords(oneBullet)
            if bulletPosition[1] <= -40:
                canvas.delete(oneBullet)
                toPopPlayerBullet.append(i)
        for index in toPopPlayerBullet:
            listOfPlayerBullets.pop(index)
        for bullet in listOfPlayerBullets:
            canvas.move(bullet, 0, -5)

    #___Move enemies________________________________________________________________________________
    if times % 100 == 0:
        toPopEn = []
        for index in range(len(listOfEnemies)):
            eachEnemy = listOfEnemies[index]
            position = canvas.coords(eachEnemy)
            if position[1] > 550:
                canvas.delete(listOfEnemies[index])
                toPopEn.append(index)
            canvas.move(eachEnemy, 0, 5)
    
        for i in toPopEn:
            listOfEnemies.pop(i)

    #___Create an enemy_____________________________________________________________________________
    if times % 1500 == 0:
        enemy = canvas.create_image(random.randrange(10, 630), -60, anchor=NW, image=enemyImage)
        listOfEnemies.append(enemy)

    #___Enemies create the bullets_____________________________________________________________________
    if times % 4000 == 0:
        creator = random.choice(listOfEnemies)
        position = canvas.coords(creator)
        enGun = canvas.create_image(position[0] + 22.5, position[1] + 70, anchor=NW, image = enemyBullet)
        listOfEnemyBullets.append(enGun)
    
    canvas.after(1, globalProcess)

###########################################################################################################################

#___Move left by key______________________________
def onKeyleft(event):
    global playerX
    if playerX > 10:
        playerX -= 10
    canvas.moveto(player, playerX, playerY)

#___Move right by key_____________________________
def onKeyRight(event):
    global playerX
    if playerX < 610:
        playerX += 10
    canvas.moveto(player, playerX, playerY)

#___Move up by key________________________________
def onKeyUp(event):
    global playerY
    if playerY > 10:
        playerY -= 10
    canvas.moveto(player, playerX, playerY)

#___Move down by key______________________________
def onKeyDown(event):
    global playerY
    if playerY < 510:
        playerY += 10
    canvas.moveto(player, playerX, playerY)

#___Player creates a bullet_______________________
def createBullet(event):
    global listOfPlayerBullets, toKill
    playerPosition = canvas.coords(player)
    toKill = canvas.create_image(playerPosition[0] + 32.5, playerPosition[1] - 15, anchor=NW, image = gun)

    listOfPlayerBullets.append(toKill)

#_______________________Create Window____________________
root = Tk()
root.geometry(str(screenWidth) + "x" + str(screenHeight))
root.title('Pro-Developer')
root.resizable(False, False)
canvas = Canvas(root)
canvas.pack(expand=True, fill="both")

#________________To display background image and player_______________________________
bgImage = PhotoImage(file='pictures/bg.gif')
gun = PhotoImage(file='pictures/playerBullet.gif')        # size of the bullet (15x30)
enemyBullet = PhotoImage(file='pictures/enBullet.gif')    # size of the bullet (10x15)
playerImage = PhotoImage(file='pictures/player.gif')      # size of the player (80x80)
enemyImage = PhotoImage(file='pictures/enemy.gif')        # size of the player (55x70)

background = canvas.create_image(700, 600, anchor=SE, image=bgImage)
player = canvas.create_image(playerX, playerY, anchor=NW, image=playerImage)

globalProcess()

#___Arrow keys to move______________
root.bind('<s>', onKeyleft)
root.bind('<d>', onKeyRight)
root.bind('<a>', onKeyUp)
root.bind('<f>', onKeyDown)
root.bind('<\>', createBullet)

root.mainloop()

