#_________________________________________Imports_______________________________________________________________________

from tkinter import *

#________________Variables_________________

screenWidth = 700
screenHeight = 600
playerX = 300
playerY = 500
listOfBullets = []

#________________Functions_________________

def displayGrid():
    canvas.moveto(player, playerX, playerY)

def move_bullets():
    global listOfBullets
    toPop = []

    #___To check the bullet can move or not______
    for i in range(len(listOfBullets)):
        if listOfBullets[i][2] > -40:
            listOfBullets[i][2] -= 5
        else:
            toPop.append(i)

    #___To delete bullets which is useless_______
    for index in toPop:
        listOfBullets.pop(index)

    #___To move bullets up________________________
    for bullet in listOfBullets:
        canvas.moveto(bullet[0], bullet[1], bullet[2])


    canvas.after(10, move_bullets)




#____To move left by key__________________

def onKeyleft(event):
    global playerX
    if playerX > 10:
        playerX -= 10
    displayGrid()

#____To move right by key_________________

def onKeyRight(event):
    global playerX
    if playerX < 620:
        playerX += 10
    displayGrid()

#___To move up by key_____________________

def onKeyUp(event):
    global playerY
    if playerY > 10:
        playerY -= 10
    displayGrid()

#___To move down by key___________________

def onKeyDown(event):
    global playerY
    if playerY <= 500:
        playerY += 10
    displayGrid()

#___To shoot_______________________________

def creat_bullet(event):
    global listOfBullets, toKill
    playerPosition = canvas.coords(player)
    
    x = playerPosition[0] - 10
    y = playerPosition[1] - 60
    toKill = canvas.create_image(x, y, anchor=NW, image = bullet)

    listOfBullets.append([toKill, x, y])






#_______________________Create Window____________________

root = Tk()
root.geometry(str(screenWidth) + "x" + str(screenHeight))
root.title('Pro-Developer')
root.resizable(False, False)
canvas = Canvas(root)
canvas.pack(expand=True, fill="both")

#________________To display background image and player__________________

bgImage = PhotoImage(file='pictures/bg.gif')
bullet = PhotoImage(file='pictures/bullet.gif')
img = PhotoImage(file='pictures/shooter.gif')

background = canvas.create_image(700, 600, anchor=SE, image=bgImage)
player = canvas.create_image(playerX, playerY, anchor=CENTER, image=img)


displayGrid()
move_bullets()

#____Arrow keys to move__________________________________

root.bind('<a>', onKeyleft)
root.bind('<f>', onKeyRight)
root.bind('<s>', onKeyUp)
root.bind('<d>', onKeyDown)
root.bind('<Return>', creat_bullet)

root.mainloop()

