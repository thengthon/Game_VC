from tkinter import *
import random

#---Variables-----------------
times = 0
score = 0
toConfig = 0
numOfSucceedEn = 0
numOFBullets = 100            # The index of live to configure
screenWidth = 700
screenHeight = 650
playerX = 310
playerY = 510
listOfPlayerBullets = []
listOfEnemies = []
listOfEnemyBullets = []
listOfLives = []
result = 'Game Over!!!'

#===================================FUNCTIONS===================================#

#------------------Global Process------------------#
def globalProcess():
    global times, numOFBullets, toConfig, score, result

    times += 1

    bulletMeetBullet()
    bulletMeetEn()

    #____To check if the player win with the score limited_______________________
    if score == 50:
        result = 'Congratulation'
        finishGame()
        return None
    
    bulletMeetPlayer()
    enemyMeetPlayer()

    #___# Finish the game when player has no bullet, or has no live, or enemies passed 20 times____
    if (numOFBullets == -1):
        result += '\nYou have no bullets.\nScores: ' + str(score)
        finishGame()
        return None
    elif (toConfig == -6):
        result += '\nYou have no LIVE.\nScores: ' + str(score)
        finishGame()
        return None
    elif (numOfSucceedEn == 20):
        result += '\nEnemies passed 20 times.\nScores: ' + str(score)
        finishGame()
        return None

    #___Move bullets__________
    moveBulletsOfEn()
    moveBulletsOfPlayer()

    #___Move enemies__________
    if times % 5 == 0:
        moveEnemies()

    #___Create an enemy_______
    if times % 75 == 0:
        createEnemy()

    #___Enemies create the bullets___
    if times % 150 == 0:
        enCreateBullet()
    
    canvas.after(15, globalProcess)

#------------------------------------------------------#

#___Create Enemy__________________________________
def createEnemy():
    enemy = canvas.create_image(random.randrange(10, 630), -60, anchor=NW, image=enemyImage)
    listOfEnemies.append(enemy)

#___Move Enemies__________________________________
def moveEnemies():
    global numOfSucceedEn
    toPopEn = []
    for index in range(len(listOfEnemies)):
        eachEnemy = listOfEnemies[index]
        position = canvas.coords(eachEnemy)
        if position[1] > 520:
            numOfSucceedEn += 1
            canvas.itemconfig(succeededEn, text=str(numOfSucceedEn))
            canvas.delete(listOfEnemies[index])
            toPopEn.append(index)
        canvas.move(eachEnemy, 0, 5)

    for i in toPopEn:
        listOfEnemies.pop(i)

#___Enemies create bullets________________________
def enCreateBullet():
    if len(listOfEnemies) > 0:
        creator = random.choice(listOfEnemies)
        position = canvas.coords(creator)
        enGun = canvas.create_image(position[0] + 22.5, position[1] + 70, anchor=NW, image = enemyBullet)
        listOfEnemyBullets.append(enGun)

#___Move bullets of enemies_______________________
def moveBulletsOfEn():
    toPopEnBullet = []
    for i in range(len(listOfEnemyBullets)):
        bullet = listOfEnemyBullets[i]
        bulletPosition = canvas.coords(bullet)
        if bulletPosition[1] >= 575:
            canvas.delete(bullet)
            toPopEnBullet.append(i)
    for index in toPopEnBullet:
        listOfEnemyBullets.pop(index)
    for bullet in listOfEnemyBullets:
        canvas.move(bullet, 0, 5)

#___Player creates a bullet_______________________
def createBullet(event):
    global numOFBullets
    if (numOFBullets > 0) and (toConfig != -6) and (score < 50):
        numOFBullets -= 1
        canvas.itemconfig(showBullets, text=("Bullets: " + str(numOFBullets)))

        playerPosition = canvas.coords(player)
        toKill = canvas.create_image(playerPosition[0] + 32.5, playerPosition[1] - 15, anchor=NW, image = gun)
        listOfPlayerBullets.append(toKill)
    else:
        numOFBullets -= 1

#___Move bullets of player________________________
def moveBulletsOfPlayer():
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

#___To check if bullets of player meet with bullets of enemy_____
def isMeetBullet(listOfPlayerBullets, listOfEnemyBullets):
    toDelete = []
    for playerBullet in listOfPlayerBullets:
        positionOfBulletPlayer = canvas.coords(playerBullet)

        for enBullet in listOfEnemyBullets:
            positionOfBulletEn = canvas.coords(enBullet)
            if (positionOfBulletPlayer[1] <= positionOfBulletEn[1]+15) and (((positionOfBulletEn[0] >= positionOfBulletPlayer[0]) and (positionOfBulletEn[0] <= positionOfBulletPlayer[0]+15)) or ((positionOfBulletEn[0]+10 >= positionOfBulletPlayer[0]) and (positionOfBulletEn[0]+10 <= positionOfBulletPlayer[0]+15))):
                toDelete.append(playerBullet)
                toDelete.append(enBullet)
    return toDelete

#___To check if bullets of player meet with enemy________________
def isMeetEnemy(listOfPlayerBullets, listOfEnemies):
    toDelete = []
    for playerBullet in listOfPlayerBullets:
        positionOfBulletPlayer = canvas.coords(playerBullet)

        for enemy in listOfEnemies:
            positionOfEn = canvas.coords(enemy)
            if (positionOfBulletPlayer[1] <= positionOfEn[1]+70) and (((positionOfBulletPlayer[0] >= positionOfEn[0]) and (positionOfBulletPlayer[0] <= positionOfEn[0]+55)) or ((positionOfBulletPlayer[0]+15 >= positionOfEn[0]) and (positionOfBulletPlayer[0]+15 <= positionOfEn[0]+55))):
                toDelete.append(playerBullet)
                toDelete.append(enemy)
    return toDelete

#___To check if bullets of enemies meet the player or not_______
def isBulletMeetPlayer(bullets, player):
    toDelete = None
    positionPlayer = canvas.coords(player)
    for bullet in bullets:
        positionBullet = canvas.coords(bullet)
        if (positionBullet[1]+20 >= positionPlayer[1]) and (((positionBullet[0] >= positionPlayer[0]) and (positionBullet[0] <= positionPlayer[0]+80)) or ((positionBullet[0]+15 >= positionPlayer[0]) and (positionBullet[0]+15 <= positionPlayer[0]+80))):
            toDelete = bullet
    return toDelete

def isEnemyMeetPlayer(enemies, player):
    toDelete = None
    positionPlayer = canvas.coords(player)
    for enemy in enemies:
        positionEn = canvas.coords(enemy)
        if (positionEn[1]+40 >= positionPlayer[1]) and (((positionEn[0] >= positionPlayer[0]) and (positionEn[0] <= positionPlayer[0]+80)) or ((positionEn[0]+55 >= positionPlayer[0]) and (positionEn[0]+55 <= positionPlayer[0]+80))):
            toDelete = enemy
    return toDelete

#___To check the bullets of player meet bullets of enemy or nor______________
def bulletMeetBullet():
    global numOFBullets
    meetBullet = isMeetBullet(listOfPlayerBullets, listOfEnemyBullets)
    if len(meetBullet) > 0:
        listOfPlayerBullets.remove(meetBullet[0])
        listOfEnemyBullets.remove(meetBullet[1])
        canvas.delete(meetBullet[0])
        canvas.delete(meetBullet[1])
        numOFBullets += 5
        canvas.itemconfig(showBullets, text=("Bullets: " + str(numOFBullets)))

#____To check the bullets of player meet the enemies or not__________________
def bulletMeetEn():
    global score
    meetEnemy = isMeetEnemy(listOfPlayerBullets, listOfEnemies)
    if len(meetEnemy) > 0:
        listOfPlayerBullets.remove(meetEnemy[0])
        listOfEnemies.remove(meetEnemy[1])
        canvas.delete(meetEnemy[0])
        canvas.delete(meetEnemy[1])
        score += 1
        canvas.itemconfig(showScore, text=("Score: " + str(score)))

#____To check the bullets of enemies meet the player or not___________________
def bulletMeetPlayer():
    global toConfig
    bulletMeetPlayer = isBulletMeetPlayer(listOfEnemyBullets, player)
    if bulletMeetPlayer != None:
        listOfEnemyBullets.remove(bulletMeetPlayer)
        canvas.delete(bulletMeetPlayer)
        toConfig -= 1
        canvas.itemconfig(listOfLives[toConfig], fill='white', outline='')

#_____To check enemy meets the player or not___________________________________
def enemyMeetPlayer():
    global toConfig
    enemyMeetPlayer = isEnemyMeetPlayer(listOfEnemies, player)
    if enemyMeetPlayer != None:
        listOfEnemies.remove(enemyMeetPlayer)
        canvas.delete(enemyMeetPlayer)
        toConfig -= 1
        canvas.itemconfig(listOfLives[toConfig], fill='white', outline='')

#___Show result________________________________________________
def finishGame():
    canvas.delete('all')
    canvas.create_text(350, 300, text = result, font=("Comic Sans", 30), fill='black')

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

#======================================================================#

#------------------------Create Window---------------------------
root = Tk()
root.geometry(str(screenWidth) + "x" + str(screenHeight))
root.title('Pro-Developer')
root.resizable(False, False)
canvas = Canvas(root)
canvas.pack(expand=True, fill="both")

#--------------To display background image and player--------------------------------
bgImage = PhotoImage(file='pictures/bg.gif')
gun = PhotoImage(file='pictures/playerBullet.gif')        # size of the bullet (15x30)
enemyBullet = PhotoImage(file='pictures/enBullet.gif')    # size of the bullet (10x15)
playerImage = PhotoImage(file='pictures/player.gif')      # size of the player (80x80)
enemyImage = PhotoImage(file='pictures/enemy.gif')        # size of the player (55x70)

background = canvas.create_image(700, 650, anchor=SE, image=bgImage)
player = canvas.create_image(playerX, playerY, anchor=NW, image=playerImage)

#--------------To display at the bottom-----------------------------------------------------------------------
showScore = canvas.create_text(583, 625, text=("Scores: " + str(score)), font=("Comic Sans", 15), fill='blue')
showBullets = canvas.create_text(350, 625, text=("Bullets: " + str(numOFBullets)), font=("Comic Sans", 15), fill='blue')
succeededEn = canvas.create_text(35, 625, text=str(numOfSucceedEn), font=("Comic Sans", 15), fill='red')

line = canvas.create_line(0, 600, 700, 600, fill='white')
lineL = canvas.create_line(233, 600, 233, 650, fill='white')
lineR = canvas.create_line(466, 600, 466, 650, fill='white')
live = canvas.create_text(90, 625, text=("HP : "), font=("Comic Sans", 15), fill='blue')

for i in range(6):
    lives = canvas.create_rectangle(130 + (10*i)+1, 614, 130 + (10*(i+1)), 635, outline='', fill='red')
    listOfLives.append(lives)

globalProcess()

#---Arrow keys to move-----------
root.bind('<s>', onKeyleft)
root.bind('<d>', onKeyRight)
root.bind('<a>', onKeyUp)
root.bind('<f>', onKeyDown)
root.bind('<Return>', createBullet)

root.mainloop()

