try:
    import Tkinter as tk
    import ttk
except:
    import tkinter as tk
    import tkinter.ttk as ttk

dark_blue = "#022B62"
light_blue = "#034FB6"
celeste = "2793EB"
white = "#ffffff"
myred = "#dd0202"

def getStyle():
    style = ttk.Style()
    style.theme_create("db_style",parent="alt",settings={
        "TFrame": {
            "configure": {
                "background": dark_blue
            }
        },
        "TNotebook": {
            "configure": {
                "tabmargins": [0, 0, 0, 0],
                "background": dark_blue
            }
        },
        "TNotebook.Tab": {
            "configure": {
                "padding": [5, 5],
                "background": dark_blue,
                "foreground": white,
                "font": 'helvetica 10 bold'
            },
            "map": {
                "background": [("selected", light_blue)]
            }
        },
        "TLabel": {
            "configure": {

                "background":light_blue,
                "foreground":white
            }
        },
        "TButton": {
            "configure": {
                "padding": 0,
                "relief": tk.FLAT,
                "font": "helvetica 10 bold",
                "background":dark_blue

            },
            "map": {
                "foreground":[('pressed',white),('active',white)],
                "background": [('pressed',light_blue),('active','black')]
            }
        }
    })
    style.theme_use("db_style")
    return style