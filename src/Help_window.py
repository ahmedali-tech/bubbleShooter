# *********** HELP AND CONTROL WINDOW **********
import tkinter as tk
from game import Game

def help_win():


    def game_opener():
        help_window.destroy()
        Game()


    help_window = tk.Tk()
    height = help_window.winfo_screenheight()
    width = help_window.winfo_screenwidth()
    help_window.geometry("800x400+{}+{}".format((width - 100) // 4, height - height+200))
    help_window.maxsize(1400, 1080)
    help_window.minsize(550, 200)
    help_window.title("BUBBLE SHOOTER--HELP")
    help_window.config(background='#047E97')
    help_window.columnconfigure(0,weight=3)
    help_window.columnconfigure(2,weight=3)


    # --------------------------------------CONTENT ----------------------------
    def load_text():
        """
        loads an about-text from specific file
        """
        with open("../docs/Help_Controls.txt") as file:
            return file.read()


    text = load_text()
    label = tk.Label(help_window,text=text,font="verdana 10 bold",background='#047E97')
    label.grid(column=0,padx=20)
    return_but = tk.Button(help_window, text="CONTINUE", bg="#ED2C5C", height=2, width=14, font="verdana 13 bold",command=lambda:game_opener()).grid(row=3, column=0,padx=20)

    help_window.mainloop()
