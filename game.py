#_________________________________________Imports_______________________________________________________________________

from tkinter import *
from PIL import ImageTk, Image

#________________Variables_________________

screenWidth = 700
screenHeight = 600
playerX = 30
playerY = 50

#________________Functions_________________

def displayGrid():
    canvas.moveto(player, playerX, playerY)




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
    canvas.create_image()




#_______________________Create Window____________________

root = Tk()
root.geometry(str(screenWidth) + "x" + str(screenHeight))
root.title('Pro-Developer')
root.resizable(False, False)
canvas = Canvas(root)
canvas.pack(expand=True, fill="both")

#________________To display background image and player__________________

bgImage = PhotoImage(file='bg.gif')
bullet = PhotoImage(file='bullet.gif')
img = PhotoImage(file='shooter.gif')

background = canvas.create_image(700, 600, anchor=SE, image=bgImage)
player = canvas.create_image(playerX, playerY, anchor=CENTER, image=img)


displayGrid()

#____Arrow keys to move__________________________________

root.bind('<a>', onKeyleft)
root.bind('<f>', onKeyRight)
root.bind('<e>', onKeyUp)
root.bind('<d>', onKeyDown)
root.bind('<Return>', onKeyDown)

root.mainloop()

