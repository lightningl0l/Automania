import tkinter as tk
from PIL import Image, ImageTk
from threading import *

scriptdir = __file__.replace(__file__.split('\\')[-1], '') #get the directory of the running script

root = tk.Tk()
root.resizable(False, False)
root.title('Automania')
root.iconbitmap(scriptdir + 'txr\\icon.ico')

canvas = tk.Canvas(root, width = 1500, height = 900, bg = '#8b9098')
canvas.pack()

bg = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\bg.png'))
lining = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\lining.png'))
sqrlight = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\sqrlight.png'))
sqrtall = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\sqrtall.png'))
sqrcoolant = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\sqrcoolant.png'))
tick = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\tick.png'))
delete = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\delete.png'))
drill = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\drill.png'))
pump = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\pump.png'))
smelter = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\smelter.png'))
press = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\press.png'))
conveyor1 = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\conveyor1.png'))
arm1 = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\arm1.png'))
pipe = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\pipe.png'))
sell = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\sell.png'))
maintitle = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\maintitle.png'))
settingscircle = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\settingscircle.png'))
treecircle = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\treecircle.png'))
exitcircle = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\exitcircle.png'))
settingsmenu = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\settingsmenu.png'))
treemenu = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\treemenu.png'))
recipes1 = ImageTk.PhotoImage(Image.open(scriptdir + 'txr\\recipes1.png'))

blocks = {1 : drill, 2 : smelter, 3 : press, 4 : sell, 5 : conveyor1, 6 : arm1, 7 : pipe, 8 : pump}
worldsize = 8
recipeson = False

#make world as list
grid = []
for x in range(worldsize):
    grid.insert(x, []) #make lists
    for y in range(worldsize):
        grid[x].insert(y, 0) #0 is blank

skills = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
inventories = [] #to be filled with inventory coordinates

#bg
for h in range(1, -1, -1):
    for x in range(worldsize + 1):
        for y in range(worldsize + 1):
            if (h == 1 and x != worldsize and y != worldsize): #render only seen tiles
                continue
            gx = 750 + (x - y) * 32 #convert cartesian coords into iso coords
            gy = 700 - (y + x) * 16 - (h * 32) #shift board down
            canvas.create_image(gx, gy - worldsize * 16, image = bg)

#region buttons
menuopen = 0
placement = 0
def settingscmd():
    global menuopen, recipeson
    if menuopen == 0:
        menuopen = 1
    else:
        menuopen = 0
    if menuopen == 1:
        canvas.create_image(750, 450, image = settingsmenu, tags = 'menu')
        if recipeson == True:
            canvas.create_image(530, 349, image = tick, tags = ('tick', 'menu'))
    else:
        canvas.delete('menu')
def treecmd():
    global menuopen, skills
    if menuopen == 0:
        menuopen = 2
    else:
        menuopen = 0
    if menuopen == 2:
        canvas.create_image(750, 338, image = treemenu, tags = 'menu')
        if skills[0] == 1:
            canvas.create_image(342, 571, image = sqrlight, tags = 'menu')
            canvas.create_image(342, 571, image = smelter, tags = 'menu')
        if skills[1] == 1:
            canvas.create_image(576, 223, image = sqrtall, tags = 'menu')
        if skills[2] == 1:
            canvas.create_image(576, 571, image = sqrlight, tags = 'menu')
            canvas.create_image(576, 571, image = press, tags = 'menu')
        if skills[3] == 1:
            canvas.create_image(750, 416, image = sqrcoolant, tags = 'menu')
        if skills[4] == 1:
            canvas.create_image(954, 107, image = sqrlight, tags = 'menu')
            canvas.create_image(954, 107, image = arm1, tags = 'menu')
        if skills[5] == 1:
            canvas.create_image(954, 339, image = sqrlight, tags = 'menu')
        if skills[6] == 1:
            canvas.create_image(954, 571, image = sqrlight, tags = 'menu')
        if skills[7] == 1:
            canvas.create_image(1100, 107, image = sqrlight, tags = 'menu')
        if skills[8] == 1:
            canvas.create_image(1100, 223, image = sqrlight, tags = 'menu')
        if skills[9] == 1:
            canvas.create_image(1100, 339, image = sqrlight, tags = 'menu')
        if skills[10] == 1:
            canvas.create_image(1100, 451, image = sqrlight, tags = 'menu')
        if skills[11] == 1:
            canvas.create_image(1100, 571, image = sqrlight, tags = 'menu')
    else:
        canvas.delete('menu')
def exitcmd():
    root.destroy()
def drillbuttoncmd():
    global placement
    placement = 1
    canvas.delete('bganim')
    canvas.create_image(600, 710, image = lining, tags = 'bganim')
def smelterbuttoncmd():
    global placement
    placement = 2
    canvas.delete('bganim')
    canvas.create_image(700, 710, image = lining, tags = 'bganim')
def pressbuttoncmd():
    global placement
    placement = 3
    canvas.delete('bganim')
    canvas.create_image(800, 710, image = lining, tags = 'bganim')
def sellbuttoncmd():
    global placement
    placement = 4
    canvas.delete('bganim')
    canvas.create_image(900, 710, image = lining, tags = 'bganim')
def conveyorbuttoncmd():
    global placement
    placement = 5
    canvas.delete('bganim')
    canvas.create_image(600, 790, image = lining, tags = 'bganim')
def armbuttoncmd():
    global placement
    placement = 6
    canvas.delete('bganim')
    canvas.create_image(700, 790, image = lining, tags = 'bganim')
def pipebuttoncmd():
    global placement
    placement = 7
    canvas.delete('bganim')
    canvas.create_image(800, 790, image = lining, tags = 'bganim')
def pumpbuttoncmd():
    global placement
    placement = 8
    canvas.delete('bganim')
    canvas.create_image(900, 790, image = lining, tags = 'bganim')
def deletebuttoncmd():
    global placement
    placement = 0
    canvas.delete('bganim')
    canvas.create_image(1000, 750, image = lining, tags = 'bganim')

canvas.create_window(1400, 800, window = tk.Button(root, image = settingscircle, command = settingscmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(100, 800, window = tk.Button(root, image = treecircle, command = treecmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(100, 100, window = tk.Button(root, image = exitcircle, command = exitcmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(600, 710, window = tk.Button(root, image = drill, command = drillbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(700, 710, window = tk.Button(root, image = smelter, command = smelterbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(800, 710, window = tk.Button(root, image = press, command = pressbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(900, 710, window = tk.Button(root, image = sell, command = sellbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(600, 790, window = tk.Button(root, image = conveyor1, command = conveyorbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(700, 790, window = tk.Button(root, image = arm1, command = armbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(800, 790, window = tk.Button(root, image = pipe, command = pipebuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(900, 790, window = tk.Button(root, image = pump, command = pumpbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(1000, 750, window = tk.Button(root, image = delete, command = deletebuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_image(750, 100, image = maintitle)
#endregion

#block rendering
def render():
    canvas.delete('block')
    for y in range(worldsize - 1, - 1, - 1): #render in reverse
        for x in range(worldsize - 1, - 1, - 1):
            if grid[x][y] == 0:
                continue
            gx = 750 + (x - y) * 32 #convert cartesian coords into iso coords
            gy = 668 - (y + x) * 16 #shift board down
            canvas.create_image(gx, gy - worldsize * 16, image = blocks[grid[x][y]], tag = 'block')
    

#fg
def hitbox(mpos):
    if menuopen == 0:
        mpos.x -= 734
        mpos.y = mpos.y - 434
        ix = int((mpos.x // 32) + (-mpos.y // 16) + worldsize) // 2 #convert to grid and adjust for board shift
        iy = int((-mpos.y // 16) - (mpos.x // 32) + worldsize) // 2
        if ix < 0 or iy < 0:
            return
        if placement != 0 and grid[ix][iy] != 0:
            return
        grid[ix][iy] = placement
        render()
    else: #pythagoras will be used to check distance from a point
        if menuopen == 1: #check if settings are open
            if ((mpos.x - 537) * (mpos.x - 537)) + ((mpos.y - 567) * (mpos.y - 567)) <= 1048: #export button
                print('export button not done yet')
            elif ((mpos.x - 609) * (mpos.x - 609)) + ((mpos.y - 567) * (mpos.y - 567)) <= 1048: #import button
                print('import button not done yet')
            elif 506 <= mpos.x <= 553 and 325 <= mpos.y <= 372: #toggle recipes
                global recipeson
                recipeson = not recipeson
                if recipeson == True:
                    canvas.create_image(224, 450, image = recipes1, tags = 'recipes')
                    canvas.create_image(530, 349, image = tick, tags = ('tick', 'menu'))
                else:
                    canvas.delete('recipes')
                    canvas.delete('tick')
            elif 506 <= mpos.x <= 553 and 397 <= mpos.y <= 444: #toggle leaderboard
                print('toggle leaderboard not done yet')
        if menuopen == 2: #skill tree buttons
            if 294 <= mpos.x <= 385 and 519 <= mpos.y <= 615:
                skills[0] = 1
                treecmd()
                treecmd()
            elif 528 <= mpos.x <= 619 and 134 <= mpos.y <= 304:
                skills[1] = 1
                treecmd()
                treecmd()
            elif 528 <= mpos.x <= 619 and 519 <= mpos.y <= 615 and skills[0] == 1:
                skills[2] = 1
                treecmd()
                treecmd()
            elif 702 <= mpos.x <= 788 and 364 <= mpos.y <= 460 and skills[1] == 1 and skills[2] == 1:
                skills[3] = 1
                treecmd()
                treecmd()
            elif 906 <= mpos.x <= 997 and 55 <= mpos.y <= 151 and skills[3] == 1:
                skills[4] = 1
                treecmd()
                treecmd()
            elif 906 <= mpos.x <= 997 and 287 <= mpos.y <= 383 and skills[3] == 1:
                skills[5] = 1
                treecmd()
                treecmd()
            elif 906 <= mpos.x <= 997 and 519 <= mpos.y <= 615 and skills[3] == 1:
                skills[6] = 1
                treecmd()
                treecmd()
            elif 1052 <= mpos.x <= 1143 and 55 <= mpos.y <= 151 and skills[4] == 1:
                skills[7] = 1
                treecmd()
                treecmd()
            elif 1052 <= mpos.x <= 1143 and 171 <= mpos.y <= 267 and skills[4] == 1 and skills[5] == 1:
                skills[8] = 1
                treecmd()
                treecmd()
            elif 1052 <= mpos.x <= 1143 and 287 <= mpos.y <= 383 and skills[5] == 1:
                skills[9] = 1
                treecmd()
                treecmd()
            elif 1052 <= mpos.x <= 1143 and 403 <= mpos.y <= 499 and skills[11] == 1:
                skills[10] = 1
                treecmd()
                treecmd()
            elif 1052 <= mpos.x <= 1143 and 519 <= mpos.y <= 615 and skills[6] == 1:
                skills[11] = 1
                treecmd()
                treecmd()

root.bind('<Button-1>', hitbox)
root.mainloop()
