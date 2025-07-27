import tkinter as tk
import board as bo
import block as bl

r = tk.Tk()
c = tk.Canvas(r, width=1500, height=900,
            bg='#8B9098', highlightthickness=0)
c.pack()

boa = bo.Board(c, (650, 400), (450, 225), 'world.txt', 'blocks.json')
blo = bl.Blocks(c, 'blocks.json', (775, 689), 4)

def click(i):
    boa.placement = blo.click(i)

c.bind('<Button-1>', click)

r.mainloop()