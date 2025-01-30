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
fg = ImageTk.PhotoImage(Image.open(scriptdir + 'block.png'))
maintitle = ImageTk.PhotoImage(Image.open(scriptdir + 'maintitle.png'))
settingscircle = ImageTk.PhotoImage(Image.open(scriptdir + 'settingscircle.png'))
treecircle = ImageTk.PhotoImage(Image.open(scriptdir + 'treecircle.png'))
settingsmenu = ImageTk.PhotoImage(Image.open(scriptdir + 'settingsmenu.png'))

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
            gy = 750 - (y + x) * 16 - (h * 32) #shift board down
            canvas.create_image(gx, gy - worldsize * 16, image = bg)

#buttons
menuopen = False
def settingscmd():
    global menuopen
    menuopen = not menuopen
    if menuopen:
        canvas.create_image(750, 450, image = settingsmenu, tags = 'menu')
    else:
        canvas.delete('menu')
def treecmd():
    global menuopen
    menuopen = True
    print('treebutton')

canvas.create_window(1400, 800, window = tk.Button(root, image = settingscircle, command = settingscmd, bg = '#8b9098', bd = 0, activebackground = '#8b9098'))
canvas.create_window(100, 800, window = tk.Button(root, image = treecircle, command = treecmd, bg = '#8b9098', bd = 0, activebackground = '#8b9090'))
canvas.create_image(750, 100, image = maintitle)

#active block rendering
def render():
    canvas.delete('block')
    for y in range(worldsize - 1, - 1, - 1): #render in reverse
        for x in range(worldsize - 1, - 1, - 1):
            if grid[x][y] == 0:
                continue
            gx = 750 + (x - y) * 32 #convert cartesian coords into iso coords
            gy = 718 - (y + x) * 16 #shift board down
            canvas.create_image(gx, gy - worldsize * 16, image = fg, tag = 'block')

#fg
def hitbox(mpos):
    if not menuopen:
        mpos.x -= 734
        mpos.y = mpos.y - 484
        ix = int((mpos.x // 32) + (-mpos.y // 16) + worldsize) // 2 #convert to grid and adjust for board shift
        iy = int((-mpos.y // 16) - (mpos.x // 32) + worldsize) // 2
        if ix < 0 or iy < 0:
            return
        grid[ix][iy] = 1
        render()
    else:
        if ((mpos.x - 537) * (mpos.x - 537)) + ((mpos.y - 567) * (mpos.y - 567)) <= 1048:
            print('export button not done yet')
        elif ((mpos.x - 609) * (mpos.x - 609)) + ((mpos.y - 567) * (mpos.y - 567)) <= 1048:
            print('import button not done yet')
root.bind('<Button-1>', hitbox)

root.mainloop()
