try:
    import Tkinter as tk
    import ttk
except:
    import tkinter as tk
    import tkinter.ttk as ttk

from PIL import ImageTk,Image
import estilos

class Ventana:
    'Ventana base del GUI'

    def __init__(self):
        # Se crea la ventana
        self.__root = tk.Tk()
        self.__style = estilos.getStyle()
        self.setfullscreen()
        self.settoolbar()
        self.setnotebook()
        self.drawactual()

    def setfullscreen(self):
        self.__w, self.__h = self.__root.winfo_screenwidth(), self.__root.winfo_screenheight()
        self.__root.overrideredirect(1)
        self.__root.geometry("%dx%d+0+0" % (self.__w, self.__h))

    def settoolbar(self):
        self.__tb = tk.Frame(self.__root, bg=estilos.dark_blue, relief=tk.RAISED, bd=1)
        self.__closeimg = Image.open('./close.png')
        self.__closephoto = ImageTk.PhotoImage(self.__closeimg)
        self.__btnsalir = ttk.Button(self.__tb,image=self.__closephoto,command=self.quit)
        self.__btnsalir.pack(side=tk.RIGHT,padx=2,pady=2)
        self.__tb.pack(side=tk.TOP,fill=tk.X)

    def setnotebook(self):
        self.__note = ttk.Notebook(self.__root)
        self.__factual = ttk.Frame(self.__note)
        self.__fhistorico = ttk.Frame(self.__note)
        self.__fsettings = ttk.Frame(self.__note)
        self.__note.add(self.__factual,text="Actual")
        self.__note.add(self.__fhistorico,text="Historico")
        self.__note.add(self.__fsettings,text="Settings")
        self.__note.pack(side=tk.TOP,fill=tk.BOTH,expand=1)

    def drawactual(self):
        self.__areaactual = tk.Canvas(self.__factual,width=(self.__w*3/4),height=(self.__h*3/4))
        self.__areaactual.place(x=10,y=10)
        self.__runimg = Image.open('./run.png')
        self.__runphoto = ImageTk.PhotoImage(self.__runimg)
        self.__run = ttk.Button(self.__factual,image=self.__runphoto)
        self.__run.place(x=100,y=(self.__h*3/4)+40)

    def visualizar(self):
        self.__root.mainloop()

    def quit(self):
        self.__root.quit()
        self.__root.destroy()

v1 = Ventana()
v1.visualizar()
