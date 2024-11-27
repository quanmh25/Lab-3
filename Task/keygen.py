import tkinter as tk
import random
import string
import pygame
import os


RED = "#c6260d"
WHITE = "#ffffff"
BLACK = "#000000"
GREEN = "#22e11f"
YELLOW = "#fef65b"
BLUE = "#2a7cc1"


def setWindow(window):
    window.title("Keygen")
    window.geometry("{}x{}+{}+{}".format(800, 500, 600, 300))
    # Set icon
    path_directory = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()
    path_icon = os.path.join(path_directory, 'icon.ico')
    window.iconbitmap(path_icon)
    # Set background
    window.bg_img = tk.PhotoImage(file="bg_game.png")
    bg_window = tk.Label(window, image=window.bg_img)
    bg_window.place(x=0, y=0, relwidth=1, relheight=1)

    window.resizable(False, False)


def close(music, window):
    music.stop()
    window.destroy()


def keyGenerate():
    lst = []
    for i in range(4):
        letters = "".join(random.choice(string.ascii_uppercase) for _ in range(3)) 
        digit = random.choice(string.digits)
        part = "".join(random.sample(letters + digit, 4))
        lst.append(part)
    key = "-".join(lst)

    show_key.delete(0, "end")
    show_key.insert(0, key)


def clear(show_key):
    show_key.delete(0, tk.END)  # Clear the Entry widget
   
# Create window
window = tk.Tk()

setWindow(window)

root = tk.Frame(window, bg=BLUE, width=300, height=100)
root.place(relx=0.5, rely=1, anchor='s', y=-20)

show_key = tk.Entry(root, width=25, font=("Cambria", 15), bg=GREEN, justify="center")
show_key.place(relx=0.5, rely=0.2, anchor="n")

gen_btn = tk.Button(root, text="Generate Key", width=12, bg=BLACK, fg=WHITE, command=keyGenerate)
gen_btn.place(relx=0.2, rely=0.7, anchor="center")

btn_clear = tk.Button(root, text='Clear',width=8, command=lambda: clear(show_key))
btn_clear.place(relx=0.55, rely=0.7, anchor="center")

close_btn = tk.Button(root, text="Close", width=8, bg=RED, command=lambda: close(pygame.mixer.music, window))
close_btn.place(relx=0.85, rely=0.7, anchor="center")


# Initialize Pygame mixer
pygame.mixer.init()
# Load and play background music 
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)  # -1 means loop indefinitely


window.mainloop()
