import tkinter as tk
import GameLogic as gm
gameRatio = 0.85

class Vars:
    pass

class ConwayTabel:

    def __init__(self):
        global game
        self.dim = round(gm.getWidth()/gm.getHeight(),6)
        self.canvas = tk.Canvas(game, bg="#000000", border=0, highlightthickness=0, highlightbackground="#EBF400")

    def resize(self, wd, hg):
        if self.dim == round((wd/hg),6):
            self.canvas.config(width= wd, height= hg)
            return

        wd = wd - 10
        hg = hg - 10

        if (wd/self.dim) < hg:
            hg = wd/self.dim
        else:
            wd = hg*self.dim

        self.cnWidth = wd
        self.cnHeight = hg
        self.canvas.config(width=wd, height=hg)

    def drawTabel(self, tabel : list):
        # TODO: Wenigstens die rechtecke speichern und nicht immer alles neu Erschaffen
        # TODO: Im Algemeinen einfach nur besser machen...
        self.canvas.delete("all")
        cellHeight = self.cnHeight / gm.getHeight()
        cellWidth = self.cnWidth / gm.getWidth()
        # cellHeight = 20
        for y in range(len(tabel)):
            for x in range(len(tabel[0])):
                if tabel[y][x]:
                    self.canvas.create_rectangle(cellWidth* x, cellHeight * y, cellWidth*(x+1), cellHeight*(y+1), fill = "#F72798", outline="")
                    continue
                # self.canvas.create_rectangle(cellHeight * x, cellHeight * y, cellHeight * (x + 1), cellHeight * (y + 1), fill= )

# End of ConwayTabel


def masterConfigChange(event=None):
    global master
    global table

    if master == event.widget:
        height = event.height * (1-gameRatio)
        if height < 25:
            height = 25
        if height > 50:
            height = 50

        table.resize(event.width, event.height - height)
        table.drawTabel(gm.getGameState())

        menu.config(height= height)
        menu.config(width=event.width)



if __name__ == "__main__":
    master = tk.Tk()
    master.geometry("600x800")

    menu = tk.Frame(master)
    game = tk.Frame(master)
    li = [[((i + ((n + 1) % 2)) % 2) for n in range(10)] for i in range(10)]
    gm.initGame(li)
    table = ConwayTabel()



    menu["background"] = "#F57D1F"
    game["background"] = "#00224D"
    master.update()
    var = Vars()
    var.widget = master
    var.width = master.winfo_width()
    var.height = master.winfo_height()

    masterConfigChange(var)

    menu.pack(side=tk.TOP)
    game.pack(expand= 1, fill = tk.BOTH, side= "bottom")
    table.canvas.pack(expand= 1)

    master.bind("<Configure>", masterConfigChange)

    # table.drawTabel(gm.getGameState())
    # gm.printGameState()


    master.mainloop()
