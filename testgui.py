import tkinter as tk
import pythonping
import time

def startping():
    while True:
        pythonping.ping('8.8.8.8', verbose=True, count=4 , interval=1)
        time.sleep(5)

root = tk.Tk()
root.title("Ping")
root.geometry("66x66")
root.resizable(False, False)

start = tk.Button(root, text="Start", command=startping)
start.pack()

stop = tk.Button(root, text="Stop", command=root.destroy)
stop.pack()

root.mainloop()
