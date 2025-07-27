import json as j

class Items():
    def __init__(self, b):
        self.b = b
        D = __file__.replace(__file__.split('\\')[-1], '')
        self.parcel = tk.PhotoImage(file=D + 'txr\\parcel.png')
        self.objs = [[], [], [], []]
        for i in b.all:
            if b.all[i]['type'] == 'c': s = 0
            elif b.all[i]['type'] == 'm': s = 1
            elif b.all[i]['type'] == 'p': s = 2
            else: s = -1
            self.objs[s].append(b.all[i]['key'])
        self.plate = b.cont[3].split(' ')
        self.plate = [list(i) for i in self.plate]

    def pcheck(self, i):
        for m in range(self.b.size):
            for n in range(self.b.size):
                if self.b.ores[m][n] != '0':
                    if int(self.b.stuff[m][n]) in self.objs[0]:
                        self.plate[m][n] = '1'
                else: self.plate[m][n] = '0'
                for i in self.b.all:
                    if self.b.all[i]['key'] in self.objs[1]:
                        if int(self.b.stuff[m][n]) == self.b.all[i]['key']:
                            for o in self.b.all[i]['pass']:
                                try:
                                    if self.plate[m + o[0]][n + o[1]] != '0':
                                            self.plate[m][n] = '1'
                                except Exception: pass
    
        for m in range(self.b.size):
            for n in range(self.b.size):
                if self.plate[m][n] != '0':
                    x = (m - n) * 32 + self.b.scrollx
                    y = (m + n) * 16 + self.b.scrolly
                    self.b.c.create_image(x, y, image=self.parcel, tags='board')

if __name__ == '__main__':
    import tkinter as tk
    import board as bo
    import block as bl
    
    r = tk.Tk()
    c = tk.Canvas(width=1500, height=900, bg='#8B9098', highlightthickness=0)
    c.pack()

    boa = bo.Board(c, (650, 400), (450, 225), 'world.txt', 'blocks.json')
    blo = bl.Blocks(c, 'blocks.json', (775, 689), 4)
    ite = Items(boa)

    def cmd(i):
        boa.placement = blo.click(i)
    boa.c.bind('<Button-5>', ite.pcheck)
    c.bind('<Button-1>', cmd)

    r.mainloop()