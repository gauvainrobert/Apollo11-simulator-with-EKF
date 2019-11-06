import utils.constants as constants
#---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter as Tk
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



class InterfaceGraphique:
    fig = Figure()
    affichageDonnees = None
    coordonneePoint = None



    def __init__(self, win):
        self.win = win
        self.creation()

    def creation(self):
        self.creationFormulaireTrajectoire()
        self.creationAffichageDonneesPoint()
        self.creationVisualisation3d()



    def creationAffichageDonneesPoint(self):
        self.affichageDonnees = Tk.Frame(self.win)
        self.coordonneePoint = Tk.Label(self.affichageDonnees, text = "vide pour l'instant")
        self.coordonneePoint.pack()
        self.affichageDonnees.pack(side = Tk.RIGHT)




    def creationFormulaireTrajectoire(self):
        formulaireTrajectoire = Tk.Frame()
        label = Tk.Label(formulaireTrajectoire, text = "Formulaire Trajectoire")
        label.grid(row = 0, column = 0)
        labelXTrajectoire = Tk.Label(formulaireTrajectoire, text = "X:")
        labelXTrajectoire.grid(row = 1, column = 0)
        xTrajectoire = Tk.Entry(formulaireTrajectoire)
        xTrajectoire.grid(row = 1, column = 1)
        labelYTrajectoire = Tk.Label(formulaireTrajectoire, text = "Y:")
        labelYTrajectoire.grid(row = 2, column = 0)
        yTrajectoire = Tk.Entry(formulaireTrajectoire)
        yTrajectoire.grid(row = 2, column = 1)
        labelZTrajectoire = Tk.Label(formulaireTrajectoire, text = "Z:")
        labelZTrajectoire.grid(row = 3, column = 0)
        zTrajectoire = Tk.Entry(formulaireTrajectoire)
        zTrajectoire.grid(row = 3, column = 1)
        labelATrajectoire = Tk.Label(formulaireTrajectoire, text = "a:")
        labelATrajectoire.grid(row = 4, column = 0)
        aTrajectoire = Tk.Entry(formulaireTrajectoire)
        aTrajectoire.grid(row = 4, column = 1)
        bFormulaireTrajectoire = Tk.Button(formulaireTrajectoire, text = "Lancer la simulation")
        bFormulaireTrajectoire.grid(row = 5, column = 1)
        formulaireTrajectoire.pack(side = Tk.TOP)







    def creationVisualisation3d(self):
        def onpick(event):
            ind = event.ind[0]
            x, y, z = event.artist._offsets3d

            ## actualiser données de droite

            self.coordonneePoint.config(text = str(x[ind]) + " " + str(y[ind]) + " " + str(z[ind]))








        canvas = FigureCanvasTkAgg(self.fig, master=self.win)
        canvas.draw()

        self.fig.canvas.mpl_connect('pick_event', onpick)



        ax = p3.Axes3D(self.fig)
        t = np.arange(0, 3, .01)
        ax.scatter(t, 2 * np.sin(2 * np.pi * t), picker = 5)

        toolbar = NavigationToolbar2Tk(canvas, self.win)
        toolbar.update()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        # ax = fig.add_subplot(111)
        # line, = ax.plot(x, np.sin(x))
        # ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)
        #

        data = [Gen_RandLine(25, 3) for index in range(50)]
        lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1], picker=5)[0] for dat in data]

        # Setting the axes properties
        ax.set_xlim3d([-constants.intervaleVisualisationTerreLune, constants.intervaleVisualisationTerreLune])
        ax.set_xlabel('X')

        ax.set_ylim3d([-constants.intervaleVisualisationTerreLune, constants.intervaleVisualisationTerreLune])
        ax.set_ylabel('Y')

        ax.set_zlim3d([-constants.intervaleVisualisationTerreLune, constants.intervaleVisualisationTerreLune])
        ax.set_zlabel('Z')

        ax.scatter([1], [0], [0], c='r', marker='^', picker=5)
        ax.scatter([0], [1], [0], c='g', marker='^', picker=5)
        ax.scatter([0], [0], [1], c='b', marker='^', picker=5)
        stride = 2
        N = 50
        u = np.linspace(0, 2 * np.pi, N)
        v = np.linspace(0, np.pi, N)
        x = constants.TerreRayonEquatorial * np.outer(np.cos(u), np.sin(v))
        y = constants.TerreRayonEquatorial * np.outer(np.sin(u), np.sin(v))
        z = constants.TerreRayonPolaire * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x, y, z, linewidth=0.0, cstride=stride, rstride=stride)


        self.line_ani = animation.FuncAnimation(self.fig, update_lines, 25, fargs=(data, lines),
                                           interval=50, blit=False)


if __name__ == "__main__":
    root = Tk.Tk()

    f = InterfaceGraphique(root)
    Tk.mainloop()
