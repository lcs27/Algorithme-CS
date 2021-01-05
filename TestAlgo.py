try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np
import time
from random import *

root = tk.Tk()



def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def drawcells(g, d, t):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 1:
                d.create_rectangle(j * t, i * t, (j + 1) * t, (i + 1) * t, fill="black")
            else:
                d.create_rectangle(j * t, i * t, (j + 1) * t, (i + 1) * t, fill="lightgrey")
    d.pack()


def updatecells(g, g2, d, t):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g2[i][j] == 1 and g[i][j] == 0:
                d.create_rectangle(j * t, i * t, (j + 1) * t, (i + 1) * t, fill="black")
            if g2[i][j] == 0 and g[i][j] == 1:
                d.create_rectangle(j * t, i * t, (j + 1) * t, (i + 1) * t, fill="lightgrey")
    d.pack()


def count(g, x, y):
    resultat = -g[x][y]
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            xx = x + i
            yy = y + j
            if xx >= len(g):
                xx = xx - len(g)
            if yy >= len(g[x]):
                yy = yy - len(g[x])
            resultat = resultat + g[xx][yy]
    return resultat


def run1(g):
    grille2 = np.zeros(g.shape)
    for i in range(len(g)):
        for j in range(len(g[i])):
            c = count(g, i, j)
            if c == 3:
                grille2[i][j] = 1
            if g[i][j] == 1 and c == 2:
                grille2[i][j] = 1
    return grille2


def count_living_cells():
    c = 0
    for i in range(len(root.grid)):
        for j in range(len(root.grid[i])):
            if root.grid[i][j] == 1:
                c += 1
    return c

def run_all():
    #drawcells(g, dessin, t)
    g2 = run1(root.grid)
    updatecells(root.grid, g2, root.gof_canvas, root.size)
    root.grid = g2
    root.living_cells.append(count_living_cells())
    root.steps.append(len(root.steps))
    root.after(root.delai, run_all)
    root.line1.set_ydata(root.living_cells)
    root.line1.set_xdata(root.steps)
    root.ax.set_xlim(0, len(root.steps))
    root.ax.set_ylim(0, root.living_cells[0])
    root.fig.canvas.draw()
    if root.steps[-1] % 10 == 0:
        s = int(1000*(time.time()-root.start_time))
        root.label["text"] = "Execution Time : {} milliseconds".format(s)


def init_cells(width, height):
    g = np.random.randint(2, size=(height, width))
    return g


def init_all():
    root.wm_title("Game of Life")

    root.label = tk.Label(master=root, text="Execution Time : {} milliseconds".format(int(1000*(time.time()-root.start_time))))
    root.label.pack(side=tk.TOP)

    button = tk.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tk.BOTTOM)

    root.width = len(root.grid[0]) * root.size
    root.height = len(root.grid) * root.size
    root.gof_canvas = tk.Canvas(root, width=root.width, height=root.height)
    root.gof_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    drawcells(root.grid, root.gof_canvas, root.size)

    plt.ion()
    root.fig = Figure(figsize=(5, 4), dpi=100)
    root.living_cells = [count_living_cells()]
    root.steps = [0]
    root.ax = root.fig.add_subplot(111)
    root.line1, = root.ax.plot(root.living_cells)

    root.plt_canvas = FigureCanvasTkAgg(root.fig, master=root)  # A tk.DrawingArea.
    root.plt_canvas.draw()
    root.plt_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def vie():
    root.size = 20
    root.delai = 200 #millisecondes
    root.grid = init_cells(30, 20)
    root.start_time = time.time()
    root.again = True

    init_all()
    root.after(root.delai, run_all)

    tk.mainloop()

vie()

