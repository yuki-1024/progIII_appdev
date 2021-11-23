from pathlib import Path
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import cv2
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
file = ''
file_name= " "
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Circuit Converter App")

window.geometry("1152x700")
window.configure(bg = "#FFF4DF")

def raise_frame(frame):
    frame.tkraise()

def createNewWindow():
    newWindow = tk.Toplevel(window)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def btn_event():
    tmp = 0
    while tmp < 1:
        tmp += 1
        btn_event.file_name = openfn()
        print(btn_event.file_name)
        
def info():
    messagebox.showinfo("List", "対応している素子:\n抵抗\nコンデンサ\n電源\n導線")

canvas = Canvas(
    window,
    bg = "#FFF4DF",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    595,
    270,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    572.0,
    74.0,
    image=image_image_2
)



button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_event,
    relief="flat"
)
button_2.place(
    x=425.0,
    y=426.0,
    width=303.0,
    height=75.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=info,
    relief="flat"
)
button_3.place(
    x=425.0,
    y=549.0,
    width=303.0,
    height=75.0
)

window.resizable(False, False)
window.mainloop()
