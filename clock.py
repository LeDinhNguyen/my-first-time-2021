from tkinter import *
from tkinter.ttk import *
from time import strftime

class App():
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap(r'clock.ico')
        self.label = Label(self.window, font= ('Digital-7', 100), background='black', foreground='green')
        self.label.pack(anchor='center')
        self.label.after(1000, self.clock)

class Clock(App):
    def clock(self):
        self.string = strftime('%H:%M:%S:%p')
        self.label.configure(text= self.string)
        self.label.after(1000, self.clock)
        self.window.mainloop()
a = Clock('nguyen')
a.clock()