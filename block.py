import tkinter as tk
import json as j

class Blocks():
    def __init__(self, root, data, off, cutoff):
        D = __file__.replace(__file__.split('\\')[-1], '')
        self.root = root
        self.imgs = []
        self.xoff = off[0]
        self.yoff = off[1]
        self.cutoff = cutoff

        with open(D + data, 'r') as f:
            self.all = j.load(f)
            for i in self.all:
                self.imgs.append((tk.PhotoImage(file=D + '\\txr\\' + self.all[i]['image'])))
            for i in range(len(self.imgs)):
                root.create_image(self.xoff + (i % cutoff - min(len(self.imgs), cutoff) / 2) * 96 + 48,
                            self.yoff + 96 * (i // cutoff), image=self.imgs[i])
        self.delete = tk.PhotoImage(file=D + 'txr\\' + 'delete.png')
        self.root.create_image(self.xoff + min(len(self.imgs) + 1, self.cutoff + 1) * 48,
                            self.yoff + ((len(self.imgs) - 1) // self.cutoff * 48),
                            image=self.delete)
        
    def click(self, i):
        x = (i.x - self.xoff + min(len(self.imgs), self.cutoff) * 48) // 96
        y = (i.y - self.yoff + 48) // 96
        if self.xoff - min(len(self.imgs), self.cutoff) * 48 < i.x < self.xoff + min(len(self.imgs), self.cutoff) * 48:
            sift = 0
            for i in self.all:
                if sift == x + (y * min(self.cutoff, len(self.imgs))):
                    self.root.delete('lining')
                    self.root.create_rectangle(self.xoff + x * 96 - 96, self.yoff + y * 96 + 48,
                                            self.xoff + x * 96 - 192, self.yoff + y * 96 - 48,
                                            width=5, outline='#474747', tags='lining')
                    return self.all[i]['key']
                sift += 1
        self.root.delete('lining')
        dx = self.xoff + min(len(self.imgs) + 1, self.cutoff + 1) * 48
        dy = self.yoff + ((len(self.imgs) - 1) // self.cutoff * 48)
        self.root.create_rectangle(dx - 48, dy - 48, dx + 48, dy + 48,
                                width=5, outline='#474747', tags='lining')
        return 0
    
if __name__ == '__main__':
    import board as bo
    
    r = tk.Tk()
    c = tk.Canvas(r, width=1500, height=900,
                bg='#8B9098', highlightthickness=0)
    c.pack()

    boa = bo.Board(c, (650, 400), (450, 225), 'world.txt', 'blocks.json')
    blo = Blocks(c, 'blocks.json', (775, 689), 4)

    def click(i):
        boa.placement = blo.click(i)

    c.bind('<Button-1>', click)

    r.mainloop()