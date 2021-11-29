from tkinter import *

from parrot import Parrot
from woodpecker import WoodPecker


class GUI:
    def __init__(self):
        self.tk = Tk()
        self.tk.title = "SnooCODE Locality Data Generator"

        self.p = Parrot()
        self.wp = WoodPecker()

    def open_window(self):
        Label(self.tk, text=self.wp.print_ascii_art()).pack()
        Button(self.tk, text="Start Program", command=self.p.chirp).pack()
        self.tk.mainloop()
