import sys
if sys.version_info[0]==2:  #Se revisa la version de python
    import Tkinter as tk  #v2.
else:
    import tkinter as tk  #v3.


root = tk.Tk()
#se consigue las medidas de la pantalla
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#se elimina la barra de titulo
root.overrideredirect(1)
#se pone a pantalla completa
root.geometry("%dx%d+0+0" % (w, h))

background_image = tk.PhotoImage(file = './background.gif')
background_label = tk.Label(root,image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.mainloop()
