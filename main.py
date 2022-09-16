import urllib.request
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from game import Game


game = Game()
if game.temps == "0":
    game.root.unbind('<space>', game.next_word)
    game.root.quit()
game.root.mainloop()