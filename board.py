import tkinter as tk
import json as j

class Board():
    def __init__(self, root, dim, pos, world, blocks):
        self.root = root
        D = __file__.replace(__file__.split('\\')[-1], '')
        self.wid = dim[0]
        self.hei = dim[1]

        with open(D + world, 'r') as f:
            cont = f.read().split('\n')
            self.size = int(cont[0])
            self.stuff = cont[1].split(' ')
            self.ores = cont[2].split(' ')
        self.stuff = [list(i) for i in self.stuff]
        self.ores = [list(i) for i in self.ores]
        self.placement = -1

        self.scrollx = dim[0] // 2
        self.scrolly = 64
        self.csx = 0
        self.csy = 0

        self.c = tk.Canvas(
            self.root, width=dim[0], height=dim[1], bg='#8B9098',
            highlightthickness=1, highlightbackground='#686C73')
        self.c.place(x=pos[0], y=pos[1])

        self.imgs = [None]
        with open(D + blocks, 'r') as f:
            self.all = j.load(f)
        for i in self.all:
            self.imgs.append((tk.PhotoImage(file=D + '\\txr\\' + self.all[i]['image'])))
        self.bg = tk.PhotoImage(file=D + 'txr\\bg.png')
        self.parcel = tk.PhotoImage(file=__file__.replace(__file__.split('\\')[-1], 'txr\\parcel.png'))
        self.OCols = {
            'C' : '#FF7F27', 'I' : '#4F332E', 'P' : '#7092BE',
            'G' : '#FFC90E', 'A' : '#B5E61D'}
        self._render()
        self.c.bind('<Button-3>', self._moves)
        self.c.bind('<B3-Motion>', self._move)
        self.c.bind('<Button-1>', self._place)

    def _render(self):
        self.c.delete('board')
        self.c.create_polygon(self.scrollx, self.scrolly,
                            self.scrollx - self.size * 32, self.scrolly + self.size * 16,
                            self.scrollx, self.scrolly + self.size * 32,
                            self.scrollx + self.size * 32, self.scrolly + self.size * 16,
                            fill='#C3C3C3', tags='board')
        for l in range(max(0, (self.scrollx + self.scrolly * 2) // -64),\
                min(self.size, ((self.scrollx - self.wid) + (self.scrolly - self.hei) * 2) // -64) + 1):
            gx1 = l * 32 + self.scrollx
            gy1 = l * 16 + self.scrolly
            gx2 = (l - self.size) * 32 + self.scrollx
            gy2 = (l + self.size) * 16 + self.scrolly
            self.c.create_line(gx1, gy1, gx2, gy2,
                            width=2, tags='board', fill='#646464')
        for l in range(max(0, ((self.scrollx - self.wid) - self.scrolly * 2) // 64),\
                min(self.size, (self.scrollx - (self.scrolly - self.hei) * 2) // 64) + 1):
            gx1 = -l * 32 + self.scrollx
            gy1 = l * 16 + self.scrolly
            gx2 = (self.size - l) * 32 + self.scrollx
            gy2 = (l + self.size) * 16 + self.scrolly
            self.c.create_line(gx1, gy1, gx2, gy2,
                            width=2, tags='board', fill='#646464')
        for l in range(min((self.scrolly // -16) + 4 + self.hei // 16, self.size - 1),\
                max(self.scrolly // -16 - 2, -1), -1):
            self.c.create_image(l * 32 + self.scrollx + 1, l * 16 + self.scrolly - 15,
                                image=self.bg, tags='board')
            self.c.create_image(l * -32 + self.scrollx + 1, l * 16 + self.scrolly - 15,
                                image=self.bg, tags='board')
        
        for i in range(len(self.ores)):
            for j in range(len(self.ores[i])):
                if self.ores[i][j] != '0':
                    x = (i - j) * 32 + self.scrollx
                    y = (i + j) * 16 + self.scrolly
                    self.c.create_polygon(x, y, x - 32, y + 16,
                                    x, y + 32, x + 32, y + 16,
                                    tags='board', fill=self.OCols[self.ores[i][j]])
        
        for i in range(len(self.stuff)):
            for j in range(len(self.stuff[i])):
                if self.stuff[i][j] != 0:
                    xi = (i - j) * 32 + self.scrollx
                    yi = (i + j) * 16 + self.scrolly
                    self.c.create_image(xi, yi, image=self.imgs[int(self.stuff[i][j])], tags='board')
    
    def _moves(self, i):
        self.csx = i.x
        self.csy = i.y

    def _move(self, i):
        if self.size * 64 > self.wid or self.size * 36 > self.hei:
            self.scrollx -= self.csx - i.x
            if self.scrollx > self.size * 32: self.scrollx = self.size * 32
            elif self.scrollx < self.wid - self.size * 32: self.scrollx = self.wid - self.size * 32

            self.scrolly -= self.csy - i.y
            if self.scrolly < self.hei - self.size * 32: self.scrolly = self.hei - self.size * 32
            elif self.scrolly > 64: self.scrolly = 64

            self._render()
            self.csx, self.csy = i.x, i.y
    
    def _place(self, i):
        if self.placement != -1:
            x = ((i.y - self.scrolly) * 2 + (i.x - self.scrollx)) // 64
            y = ((i.y - self.scrolly) * 2 - (i.x - self.scrollx)) // 64
            if self.stuff[x][y] == '0' or self.placement == 0: self.stuff[x][y] = str(self.placement)
            self._render()
    
if __name__ == '__main__':
    import block as bl

    r = tk.Tk()
    c = tk.Canvas(r, width=1500, height=900,
                bg='#8B9098', highlightthickness=0)
    c.pack()

    boa = Board(c, (650, 400), (450, 225), 'world.txt', 'blocks.json')
    blo = bl.Blocks(c, 'blocks.json', (775, 689), 4)

    def click(i):
        boa.placement = blo.click(i)

    c.bind('<Button-1>', click)

    r.mainloop()