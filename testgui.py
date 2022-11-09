#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class GuiApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(background="#95a8ff", height=200, width=200)
        toplevel1.geometry("300x300")
        toplevel1.resizable(False, False)
        label1 = ttk.Label(toplevel1)
        label1.configure(
            borderwidth=4,
            font="{Tondu Beta} 14 {}",
            text='InternetActivator')
        label1.place(
            anchor="nw",
            relheight=0.10,
            relwidth=1,
            relx=0,
            rely=0,
            x=0,
            y=0)
        self.start = ttk.Button(toplevel1)
        self.img_icons8spielen100 = tk.PhotoImage(
            file="start.png")
        self.start.configure(image=self.img_icons8spielen100, text='button1')
        self.start.place(
            anchor="nw",
            height=155,
            relheight=0.0,
            relwidth=0.0,
            relx=0,
            rely=0,
            width=155,
            x=-5,
            y=150)
        self.stop = ttk.Button(toplevel1)
        self.img_icons8stop100 = tk.PhotoImage(file="stop.png")
        self.stop.configure(image=self.img_icons8stop100, text='button1')
        self.stop.place(
            anchor="nw",
            height=155,
            relheight=0.0,
            relwidth=0.0,
            relx=0,
            rely=0,
            width=155,
            x=150,
            y=150)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = GuiApp()
    app.run()
