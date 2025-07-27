import json as j
import time as t
import threading as th

class Items():
    def __init__(self, root, size):
        D = __file__.replace(__file__.split('\\')[-1], '')
        self.root = root
        self.size = size

        self.board = []
        for x in range(self.size):
            self.board.append([])
            for y in range(self.size):
                self.board[x].append('')

        self.objs = [[], [], []]
        self.locs = [[], [], []]
        with open(D + 'blocks.json', 'r') as f:
            all = j.load(f)
        for i in all:
            if all[i]['type'] == 'c': s = 0
            elif all[i]['type'] == 'm': s = 1
            elif all[i]['type'] == 'p': s = 2
            self.objs[s].append(all[i]['key'])
        
        self.Tick = th.Thread(target=self.tick, daemon=True)
        self.Tick.start()
        
    def check_blocks(self, board, size):
        for x in range(size):
            for y in range(size):
                for i in range(len(self.objs)):
                    if int(board[x][y]) in self.objs[i]:
                        self.locs[i].append((x, y))
    
    def tick(self):
        t.sleep(0.5)
        for i in self.locs[0]:
            self.board[i[0]][i[1]] = 'P'
        for i in self.locs[1]:
            if self.board[i[0]][i[1] - 1] != 0:
                self.board[i[0]][i[1]] = self.board[i[0]][i[1] - 1]

if __name__ == '__main__':
    import tkinter as tk
    import board as bo
    import block as bl

    r = tk.Tk()
    c = tk.Canvas(r, width=1500, height=900, bg='#8B9098')
    c.pack()

    boa = bo.Board(c, (650, 400), (450, 225), 'world.txt', 'blocks.json')
    blo = bl.Blocks(c, 'blocks.json', (775, 689), 4)

    def click(i):
        boa.placement = blo.click(i)
    c.bind('<Button-1>', click)

    r.mainloop()