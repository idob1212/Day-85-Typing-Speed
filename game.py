import time
import urllib.request
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Game:
    def __init__(self):

        self.root = tk.Tk()
        word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = urllib.request.urlopen(word_url)
        long_txt = response.read().decode()
        words = long_txt.splitlines()
        self.words = words
        self.score = 0
        label1 = Label(self.root, text=random.sample(words, 1)[0])
        label2 = Label(self.root, text=random.sample(words, 1)[0])
        label3 = Label(self.root, text=random.sample(words, 1)[0])
        label4 = Label(self.root, text=random.sample(words, 1)[0])
        label5 = Label(self.root, text=random.sample(words, 1)[0])
        label6 = Label(self.root, text="score: 0")
        label1.grid(row=1, column=1)
        label1.config(bg="yellow")
        label2.grid(row=1, column=2)
        label3.grid(row=1, column=3)
        label4.grid(row=1, column=4)
        label5.grid(row=1, column=5)
        label6.grid(row=2, column = 6)
        self.labels = [label1, label2, label3, label4, label5, label6]
        self.entry = tk.Entry(self.root, font=('calibre', 10, 'normal'))
        self.entry.grid(row=2, column=3)
        self.root.bind("<space>", self.next_word, add="+")
        self.list_count = 0
        self.temps = StringVar()
        self.temps.set("60")
        self.temp = int(self.temps.get())
        sec_box = Label(
            self.root,
            width=10,
            font=("Arial", 10, ""),
            textvariable=self.temps)
        sec_box.grid(row=3, column =3)
        sec_box.after(1000, self.timer)


    def next_word(self,e):
        self.list_count += 1
        if self.list_count > 4:
            if self.labels[4]['text'] == self.entry.get().split(" ")[0]:
                self.score += 1
                self.entry.delete(0, 'end')
                self.labels[5]["text"] = f"score: {str(self.score)}"
            for label in self.labels[:-1]:
                label.config(bg="white")
            self.entry.delete(0, 'end')
            self.list_count = 0
        if self.list_count == 0:
            for label in self.labels[:-1]:
                label['text'] = random.sample(self.words, 1)[0]
            self.labels[0].config(bg="yellow")
            current_word = self.labels[0]["text"]
        else:
            if self.labels[self.list_count - 1]['text'] == self.entry.get().split(" ")[0]:
                self.score += 1
                self.entry.delete(0, 'end')
                self.labels[5]["text"] = f"Score: {str(self.score)}"
                self.labels[self.list_count - 1].config(bg="green")
            else:
                self.labels[self.list_count - 1].config(bg="white")
                self.entry.delete(0, 'end')
            self.labels[self.list_count].config(bg="yellow")
            current_word = self.labels[self.list_count]["text"]




    def timer(self,*args, **kwargs):
        if self.temp <= 0:
            self.root.unbind("<space>")
            self.entry.grid_forget()
            self.labels[5]["text"] = f"Final Score: {str(self.score)}"
            self.labels[5].grid(row=2, column =3)
            self.temps.set("Time is Up!")
            self.root.update()
        if self.temp > 0:
            self.root.update()
            self.temp = self.temp-1
            self.temps.set(str(self.temp))
            self.root.after(1000, self.timer)

