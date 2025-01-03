from turtle import *
import tkinter

#setup
penup()
hideturtle()
speed(0)
bgcolor('#bbc0c8')
worldsize = 8

scriptdir = __file__.replace(__file__.split('\\')[-1], '') #get the directory of the running script

#window setup
title('Automania')
Screen().setup(width=1500, height=900) #set size of window
Screen().cv._rootwindow.resizable(False, False) #lock size of window
Screen()._root.iconphoto(True, tkinter.PhotoImage(file = scriptdir + 'icon.png')) #make icon for window

#textures
block = scriptdir + 'block.gif'
addshape(block)
bg = scriptdir + 'bg.gif'
addshape(bg)
maintitle = scriptdir + 'maintitle.gif'
addshape(maintitle)
settingsmenu = scriptdir + 'settingsmenu.gif'
addshape(settingsmenu)
tick = scriptdir + 'tick.gif'
addshape(tick)
exitcircle = scriptdir + 'exitcircle.gif'
addshape(exitcircle)
settingscircle = scriptdir + 'settingscircle.gif'
addshape(settingscircle)
treecircle = scriptdir + 'treecircle.gif'
addshape(treecircle)
drill = scriptdir + 'drill.gif'
addshape(drill)

#make world as list
grid = []
for x in range(worldsize):
    grid.insert(x, []) #make lists
    for y in range(worldsize):
        grid[x].insert(y, 0) #0 is blank

#bg
def renbg():
    shape(bg)
    for h in range(2):
        for x in range(worldsize + 1):
            for y in range(worldsize + 1):
                if (h == 0 and (x != worldsize and y != worldsize)): #render only seen tiles
                    continue
                gx = (x - y) * 32 #convert cartesian coords into iso coords
                gy = (y + x) * 16 - (h * 32) #shift board down
                goto(gx, gy - worldsize * 16)
                stamp()
    shape(maintitle) #menu / buttons
    goto(0, window_height() // 2 - 96)
    stamp()
    shape(exitcircle)
    goto(-window_width() // 2 + 72, window_height() // 2 - 72)
    stamp()
    shape(settingscircle)
    goto(window_width() // 2 - 72, window_height() // 2 - 72)
    stamp()
    shape(treecircle)
    goto(window_width() // 2 - 72, -window_height() // 2 + 80)
    stamp()
renbg()
tracer(0)

#fg
def render():
    shape(block)
    for y in range(worldsize - 1, - 1, - 1): #render in reverse
        for x in range(worldsize - 1, - 1, - 1):
            if grid[x][y] == 0:
                continue
            gx = (x - y) * 32 #convert cartesian coords into iso coords
            gy = (y + x) * 16 #shift board down
            goto(gx, gy - worldsize * 16)
            stamp()

#place
def place(mx, my): #changes blocks
    ix = int((mx // 32) + (my // 16) + worldsize) // 2 #convert to grid and adjust for board shift
    iy = int((my // 16) - (mx // 32) + worldsize) // 2
    if ix < 0 or iy < 0: #stop negatives
        return
    try: #avoid useless error messages
        grid[ix][iy] = 1
    except:
        IndexError
    render()

settingsopen = False
def hitboxcheck(mx, my): #define hitboxes
    global settingsopen
    goto(mx, my)
    if distance(window_width() // 2 - 72, window_height() // 2 - 72) <= 64:
        settingsopen = not settingsopen
        if settingsopen:
            shape(settingsmenu)
            goto(0, 0)
            stamp()
            if distance(-214, -116) <= 32:
                print(grid) #export grid
            elif distance(-142, -116) <= 32:
                () #import grid
        if not settingsopen:
            clear()
            renbg()
            render()
    elif distance(window_width() // 2 - 72, -window_height() // 2 + 80) <= 64:
        () #open skill tree
    elif distance(-window_width() // 2 + 72, window_height() // 2 - 72) <= 64:
        bye() #close window
    else:
        place(mx, my)

Screen().onscreenclick(hitboxcheck)

#continue to run (temporary)
mainloop()