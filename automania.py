import tkinter as tk

#variables
scriptdir = __file__.replace(__file__.split('\\')[-1], '') #get the directory of the file
worldsize = 8
recipeson = False
skills = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #skill tree
grid = [] #make world as list
for x in range(worldsize):
    grid.insert(x, []) #make x line lists
    for y in range(worldsize):
        grid[x].insert(y, 0) #0 is blank

#make the window
root = tk.Tk()
root.resizable(False, False)
root.title('Automania')
root.iconbitmap(scriptdir + 'txr\\icon.ico')
root.geometry('1500x900+' + str(root.winfo_screenwidth() // 2 - 750) + '+' + str(root.winfo_screenheight() // 2 - 481)) #centres the screen
canvas = tk.Canvas(root, width = 1500, height = 900, bg = '#8b9098', highlightthickness = 1)
canvas.pack()

#region images

#title
maintitle = tk.PhotoImage(file = scriptdir + 'txr\\maintitle.png')
canvas.create_image(750, 100, image = maintitle)

#background
bg = tk.PhotoImage(file = scriptdir + 'txr\\bg.png')
for h in range(1, -1, -1):
    for x in range(worldsize + 1):
        for y in range(worldsize + 1):
            if (h == 1 and x != worldsize and y != worldsize): #render only "seen" tiles
                continue
            gx = 750 + (x - y) * 32 #convert cartesian coords into iso coords
            gy = 700 - (y + x) * 16 - (h * 32) #shift board down
            canvas.create_image(gx, gy - worldsize * 16, image = bg)

#blocks
drill = tk.PhotoImage(file = scriptdir + 'txr\\drill.png')
pump = tk.PhotoImage(file = scriptdir + 'txr\\pump.png')
smelter = tk.PhotoImage(file = scriptdir + 'txr\\smelter.png')
press = tk.PhotoImage(file = scriptdir + 'txr\\press.png')
conveyor1 = tk.PhotoImage(file = scriptdir + 'txr\\conveyor1.png')
arm1 = tk.PhotoImage(file = scriptdir + 'txr\\arm1.png')
pipe = tk.PhotoImage(file = scriptdir + 'txr\\pipe.png')
sell = tk.PhotoImage(file = scriptdir + 'txr\\sell.png')
blocks = {0 : 0, 1 : drill, 2 : smelter, 3 : press, 4 : sell, 5 : conveyor1, 6 : arm1, 7 : pipe, 8 : pump} #dict for blocks
delete = tk.PhotoImage(file = scriptdir + 'txr\\delete.png')
lining = tk.PhotoImage(file = scriptdir + 'txr\\lining.png')
parcel = tk.PhotoImage(file = scriptdir + 'txr\\parcel.png')

#meuns
treemenu = tk.PhotoImage(file = scriptdir + 'txr\\treemenu.png')
recipes1 = tk.PhotoImage(file = scriptdir + 'txr\\recipes1.png')
sqrlight = tk.PhotoImage(file = scriptdir + 'txr\\sqrlight.png')
sqrtall = tk.PhotoImage(file = scriptdir + 'txr\\sqrtall.png')
sqrcoolant = tk.PhotoImage(file = scriptdir + 'txr\\sqrcoolant.png')
tick = tk.PhotoImage(file = scriptdir + 'txr\\tick.png')
treeimgs = {0 : ((342, 571), (sqrlight, smelter)), 1 : ((576, 223), (sqrtall,)), 2 : ((576, 571), (sqrlight, press)), 3 : ((750, 416), (sqrcoolant,)), 4 : ((954, 107), (sqrlight, arm1)), 5 : ((954, 339), (sqrlight,)), 6 : ((954, 571), (sqrlight,)), 7 : ((1100, 107), (sqrlight,)), 8 : ((1100, 223), (sqrlight,)), 9 : ((1100, 339), (sqrlight,)), 10 : ((1100, 451), (sqrlight,)), 11 : ((1100, 571), (sqrlight,))}
treeButtons = {0 : ((294, 385, 519, 615), ()), 1 : ((528, 619, 134, 304), ()), 2 : ((528, 619, 519, 615), (0,)), 3 : ((702, 788, 364, 460), (1, 2)), 4 : ((906, 997, 55, 151), (3,)), 5 : ((906, 997, 287, 383), (3,)), 6 : ((906, 997, 519, 615), (3,)), 7 : ((1052, 1143, 55, 151), (4,)), 8 : ((1052, 1143, 171, 267), (4, 5)), 9 : ((1052, 1143, 287, 383), (5,)), 10 : ((1052, 1143, 403, 499), (11,)), 11 : ((1052, 1143, 519, 615), (6,))}

#buttons
settingscircle = tk.PhotoImage(file = scriptdir + 'txr\\settingscircle.png')
treecircle = tk.PhotoImage(file = scriptdir + 'txr\\treecircle.png')
exitcircle = tk.PhotoImage(file = scriptdir + 'txr\\exitcircle.png')
settingsmenu = tk.PhotoImage(file = scriptdir + 'txr\\settingsmenu.png')
blockButtons = {delete : (1000, 750, 0), drill : (600, 710, 1), smelter : (700, 710, 2), press : (800, 710, 3), sell : (900, 710, 4), conveyor1 : (600, 790, 5), arm1 : (700, 790, 6), pipe : (800, 790, 7), pump : (900, 790, 8)}
#endregion

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
        canvas.create_image(530, 421, image = delete, tags = ('menu'))
        canvas.create_image(537, 567, image = delete, tags = ('menu'))
        canvas.create_image(609, 567, image = delete, tags = ('menu'))
        if recipeson == True:
            canvas.create_image(530, 349, image = tick, tags = ('tick', 'menu'))
    else:
        canvas.delete('menu')
def treecmd():
    global menuopen, skills, treeimgs
    if menuopen == 0:
        menuopen = 2
    else:
        menuopen = 0
    if menuopen == 2:
        canvas.create_image(750, 338, image = treemenu, tags = 'menu')
        for i in range(len(treeimgs)):
            if skills[i] == 1:
                for n in range(len(treeimgs[i][1])):
                    canvas.create_image(treeimgs[i][0][0], treeimgs[i][0][1], image = treeimgs[i][1][n], tags = 'menu')
    else:
        canvas.delete('menu')
def buttoncmd(i):
    global placement
    canvas.delete('bganim')
    placement = blockButtons[i][2]
    canvas.create_image(blockButtons[i][0], blockButtons[i][1], image = lining, tags = 'bganim')
for i in blockButtons:
    canvas.create_window(blockButtons[i][0], blockButtons[i][1], window = tk.Button(root, image = i, command = lambda i=i: buttoncmd(i), bg = '#8b9098', bd = 0, activebackground = '#8b9098'))

canvas.create_window(1400, 800, window = tk.Button(root, image = settingscircle, command = settingscmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(100, 800, window = tk.Button(root, image = treecircle, command = treecmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(100, 100, window = tk.Button(root, image = exitcircle, command = root.destroy, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
#endregion

#fg
def render():
    canvas.delete('block')
    for y in range(worldsize - 1, - 1, - 1): #render in reverse
        for x in range(worldsize - 1, - 1, - 1):
            if grid[x][y] == 0:
                continue
            gx = 750 + (x - y) * 32 #convert cartesian coords into iso coords
            gy = 668 - (y + x) * 16 #shift board down
            canvas.create_image(gx, gy - worldsize * 16, image = blocks[grid[x][y]], tag = 'block')
            
#clickreg
def hitbox(mpos):
    if menuopen == 0:
        mpos.x -= 734 #adjust for board shift
        mpos.y -= 434
        ix = int((mpos.x // 32) + (-mpos.y // 16) + worldsize) // 2 #convert to grid
        iy = int((-mpos.y // 16) - (mpos.x // 32) + worldsize) // 2
        if ix < 0 or iy < 0:
            return
        try:
            if placement != 0 and grid[ix][iy] != 0: #prevent blocks from being placed on top of eachother
                return
            grid[ix][iy] = placement
            render()
        except IndexError:
            () #used to shut up meaningless errors
    else: #pythagoras will be used to check distance from a point (buttons in menus)
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
            treeButtonReqFlag = False
            for i in range(len(treeButtons)):
                if treeButtons[i][0][0] <= mpos.x <= treeButtons[i][0][1] and treeButtons[i][0][2] <= mpos.y <= treeButtons[i][0][3]:
                    for n in treeButtons[i][1]:
                        if skills[n] != 1:
                            treeButtonReqFlag = True
                            break
                    if treeButtonReqFlag:
                        break
                    skills[i] = 1
                    treecmd()
                    treecmd()
                    
root.bind('<Button-1>', hitbox)
root.mainloop()
