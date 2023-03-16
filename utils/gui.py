import tkinter as tk
from tkinter import Label, X, PhotoImage, LabelFrame, Button


# FUNCTION THAT TAKES ARGS AND DISPLAY IMAGES IN OUR MAIN FRAME
def set_image(filename, row, column):
    open_image = PhotoImage(file=filename)
    image = Label(mainframe, image=open_image)
    image.img = open_image
    image.grid(row=row, column=column)

# FUNCTION THAT TAKES ARGS AND DISPLAT BUTTONS IN OUR MAIN FRAME
def set_button(text, row, column, command):
    set_btn = Button(mainframe, text=text, width=15, command=command)
    set_btn.grid(row=row, column=column)

# INITIALIZE TKINTER
root = tk.Tk()

# ROOT DESIGNING
root.geometry('900x300')
root.resizable(height=False,width=False)
root.title("Flash LED")

# CONTENT DESIGNING
# MAIN FRAME
mainframe = LabelFrame(root, padx = 30, pady = 30)
mainframe.pack(padx=10, pady=10)

# IMAGE FOR RED LED
RED_ON = 'images\\on_red_led.png'
RED_OFF = 'images\\off_red_led.png'

# IMAGE FOR GREEN LED
GREEN_ON = 'images\\on_green_led.png'
GREEN_OFF = 'images\\off_green_led.png'

# IMAGE FOR YELLOW
YELLOW_ON = 'images\\on_yellow_led.png'
YELLOW_OFF = 'images\\off_yellow_led.png'

# SET DEFAULT IMAGE IN EACH LED
set_image(RED_OFF, 0, 0)
set_image(GREEN_OFF, 0, 1)
set_image(YELLOW_OFF, 0, 2)

from utils.app import flash_green, flash_red, flash_yellow
# BUTTON FOR RED
set_button("RED", 1, 0, flash_red)
# BUTTON FOR GREEN
set_button("GREEN", 1, 1, flash_green)
# BUTTON FOR YELLOW
set_button("YELLOW", 1, 2, flash_yellow)


