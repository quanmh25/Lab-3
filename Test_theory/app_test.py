import tkinter as tk


LENGTH, HEIGHT = 400, 300
RIGHT, DOWN = 200, 100
RED = "#c6260d"
WHITE = "#ffffff"
BLACK = "#000000"
GREEN = "#22e11f"
YELLOW = "#fef65b"
BLUE = "#2a7cc1"


root = tk.Tk()
def setupWindow():
    root.geometry("{}x{}+{}+{}".format(LENGTH, HEIGHT, RIGHT, DOWN))
    root.title("New App")
    photo = tk.PhotoImage(file="bg_pic.png")
    root.iconphoto(False, photo)

    label_1 = tk.Label(root, image=photo)
    label_1.photo = photo                    # Keep a reference to avoid garbage collection
    label_1.pack()

    root.resizable(False, False)
setupWindow()

def mainWindow():
    label_title = tk.Label(root, text="Hello", font=("Cambria", 15), bg=WHITE, fg=BLACK).place(relx=0.5, rely=0, anchor="n") 

mainWindow()

root.mainloop()

x = ['1', '2', '3']
print(x[1] + x[2])