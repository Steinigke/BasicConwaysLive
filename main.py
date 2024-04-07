import tkinter as tk
import GameLogic as gm
gameRatio = 0.85

class Vars:
    pass

class ConwayTabel:

    width = 10
    height = 10

    def __init__(self, wd, hg):
        global master
        self.dim = round(self.width/self.height,2)
        self.canvas = tk.Canvas(master, bg="#000000")
        self.resize(wd, hg)

    def resize(self, wd, hg):
        if self.dim == round((wd/hg),2):
            self.canvas.config(width= wd, height= hg)
            return

        wd = wd - 10
        hg = hg - 10

        if (wd/self.dim) < hg:
            hg = wd/self.dim
        else:
            wd = hg*self.dim

        self.canvas.config(width=wd, height=hg)

    def drawTabel(self, tabel : list):
        for y in range(len(tabel)):
            for x in range(len(tabel[0])):
                if(tabel[y][x])



# End of ConwayTabel


def masterConfigChange(event=None):
    global game
    global master
    if master == event.widget:
        height = event.height * (1-gameRatio)
        if height < 25:
            height = 25
        if height > 50:
            height = 50

        menu.config(height= height)
        menu.config(width=event.width)

if __name__ == "__main__":
    master = tk.Tk()
    master.geometry("600x800")
    menu = tk.Frame(master)
    game = tk.Frame(master)

    menu["background"] = "#F57D1F"
    game["background"] = "#000000"
    master.update()
    var = Vars()
    var.widget = master
    var.width = master.winfo_width()
    var.height = master.winfo_height()
    masterConfigChange(var)

    menu.pack(side=tk.TOP)
    game.pack(expand= 1, fill = tk.BOTH, side= "bottom")

    master.bind("<Configure>", masterConfigChange)

    gm.initGame(10,10)
    gm.addCell(1,0)
    gm.printGameState()

    master.mainloop()
