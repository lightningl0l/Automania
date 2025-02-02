import tkinter as tk
from PIL import Image, ImageTk

scriptdir = __file__.replace(__file__.split('\\')[-1], '') #get the directory of the running script

root = tk.Tk()
root.resizable(False, False)
root.title('Automania')
root.iconbitmap(scriptdir + 'icon.ico')

canvas = tk.Canvas(root, width = 1500, height = 900, bg = '#8b9098')
canvas.pack()

bg = ImageTk.PhotoImage(Image.open(scriptdir + 'bg.png'))
lining = ImageTk.PhotoImage(Image.open(scriptdir + 'lining.png'))
drill = ImageTk.PhotoImage(Image.open(scriptdir + 'drill.png'))
pump = ImageTk.PhotoImage(Image.open(scriptdir + 'pump.png'))
smelter = ImageTk.PhotoImage(Image.open(scriptdir + 'smelter.png'))
conveyor1 = ImageTk.PhotoImage(Image.open(scriptdir + 'conveyor1.png'))
arm1 = ImageTk.PhotoImage(Image.open(scriptdir + 'arm1.png'))
pipe = ImageTk.PhotoImage(Image.open(scriptdir + 'pipe.png'))
sell = ImageTk.PhotoImage(Image.open(scriptdir + 'sell.png'))
maintitle = ImageTk.PhotoImage(Image.open(scriptdir + 'maintitle.png'))
settingscircle = ImageTk.PhotoImage(Image.open(scriptdir + 'settingscircle.png'))
treecircle = ImageTk.PhotoImage(Image.open(scriptdir + 'treecircle.png'))
exitcircle = ImageTk.PhotoImage(Image.open(scriptdir + 'exitcircle.png'))
settingsmenu = ImageTk.PhotoImage(Image.open(scriptdir + 'settingsmenu.png'))

blocks = {1 : drill, 2 : pump, 3 : smelter, 4 : 'press', 5 : conveyor1, 6 : arm1, 7 : pipe, 8 : sell} #full of placeholders until animations and such are made
worldsize = 8

#make world as list
grid = []
for x in range(worldsize):
    grid.insert(x, []) #make lists
    for y in range(worldsize):
        grid[x].insert(y, 0) #0 is blank

#bg
for h in range(1, -1, -1):
    for x in range(worldsize + 1):
        for y in range(worldsize + 1):
            if (h == 1 and x != worldsize and y != worldsize): #render only seen tiles
                continue
            gx = 750 + (x - y) * 32 #convert cartesian coords into iso coords
            gy = 700 - (y + x) * 16 - (h * 32) #shift board down
            canvas.create_image(gx, gy - worldsize * 16, image = bg)

#buttons
menuopen = 0
placement = 0
def settingscmd():
    global menuopen
    if menuopen == 0:
        menuopen = 1
    else:
        menuopen = 0
    if menuopen == 1:
        canvas.create_image(750, 450, image = settingsmenu, tags = 'menu')
    else:
        canvas.delete('menu')
def treecmd():
    global menuopen
    if menuopen == 0:
        menuopen = 2
    else:
        menuopen = 0
    print('treebutton')
def exitcmd():
    root.destroy()
def drillbuttoncmd():
    global placement
    placement = 1
    canvas.delete('bganim')
    canvas.create_image(600, 710, image = lining, tags = 'bganim')
def pumpbuttoncmd():
    global placement
    placement = 2
    canvas.delete('bganim')
    canvas.create_image(700, 710, image = lining, tags = 'bganim')
def smelterbuttoncmd():
    global placement
    placement = 3
    canvas.delete('bganim')
    canvas.create_image(800, 710, image = lining, tags = 'bganim')
def pressbuttoncmd():
    global placement
    placement = 1
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
def sellbuttoncmd():
    global placement
    placement = 8
    canvas.delete('bganim')
    canvas.create_image(900, 790, image = lining, tags = 'bganim')

canvas.create_window(1400, 800, window = tk.Button(root, image = settingscircle, command = settingscmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(100, 800, window = tk.Button(root, image = treecircle, command = treecmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(100, 100, window = tk.Button(root, image = exitcircle, command = exitcmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(600, 710, window = tk.Button(root, image = drill, command = drillbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(700, 710, window = tk.Button(root, image = pump, command = pumpbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(800, 710, window = tk.Button(root, image = smelter, command = smelterbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(900, 710, window = tk.Button(root, image = drill, command = pressbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(600, 790, window = tk.Button(root, image = conveyor1, command = conveyorbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(700, 790, window = tk.Button(root, image = arm1, command = armbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(800, 790, window = tk.Button(root, image = pipe, command = pipebuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(900, 790, window = tk.Button(root, image = sell, command = sellbuttoncmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_image(750, 100, image = maintitle)

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
        grid[ix][iy] = placement
        render()
    else:
        if menuopen == 1: #check if settings are open, pythagoras will be used to check distance from a point
            if ((mpos.x - 537) * (mpos.x - 537)) + ((mpos.y - 567) * (mpos.y - 567)) <= 1048: #export button
                print('export button not done yet')
            elif ((mpos.x - 609) * (mpos.x - 609)) + ((mpos.y - 567) * (mpos.y - 567)) <= 1048: #import button
                print('import button not done yet')
            elif 506 <= mpos.x <= 553 and 325 <= mpos.y <= 372: #toggle recipes
                print('toggle recipe not done yet')
            elif 506 <= mpos.x <= 553 and 397 <= mpos.y <= 444: #toggle leaderboard
                print('toggle leaderboard not done yet')
root.bind('<Button-1>', hitbox)

root.mainloop()
