import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

def add_app():

    for widget in frame.winfo_children():
        if widget == open_file or widget == run_apps: 
            continue
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title="Select File", filetypes=(("executalbes", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def run_app():
    for app in apps:
        os.startfile(app)

#CANVAS
canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

#FRAME
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#BUTTONS
open_file = tk.Button(frame, text="Open File", padx=10, pady=5, fg="black", bg="white", command=add_app)
open_file.pack(side="bottom")
run_apps = tk.Button(frame, text="Run Apps", padx=10, pady=5, fg="black", bg="white", command=run_app)
run_apps.pack(side="top")

#RUN
root.mainloop()


