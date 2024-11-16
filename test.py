
from config_test import *
from tkinter import font

import tkinter as tk
import os


# Create a Tk root window
root = tk.Tk()

def setupWindow():
    # Set up position and size
    root.geometry("{}x{}+{}+{}".format(WINDOW_LENGTH, WINDOW_HIGHT, WINDOW_POSITION_RIGHT, WINDOW_POSITION_DOWN))

    # Change title
    root.title("Test")                     

    # Cách set icon với file png
    photo = tk.PhotoImage(file = "bg_pic.png")
    root.iconphoto(False, photo)

    # Cách set icon với file ico
    # Xem địa chỉ của file 
    path_directory = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()
    print(path_directory)
    path_icon = os.path.join(path_directory, 'icon.ico')
    print(path_icon)

    root.iconbitmap(path_icon)

    # Set background color (Dùng mã HEX)
    root.configure(bg=COLOR_BG)
    # root['bg'] = '#856ff8'

    root.resizable(False, False)     # Disiable resize 

setupWindow()


def inside():
    # print(tk.font.families())          Show fonts

    # Layout pack()
    def layout_pack():
        font_title = font.Font(family="Times New Roman", size=14, weight="bold")

        label = tk.Label(root, text="Hello!", font=font_title, bg="#5fe9e2", fg=COLOR_BLACK)
        label.pack(ipadx=20, ipady=1)
        label.pack(side="top", fill=tk.X, expand=False)

        new = tk.Label(root, text="***", font=("Cambria", 10, "bold")).pack(side="bottom", anchor="se")


    # Layout place()
    def layout_place():
        wish = tk.Label(root, text="Good luck!", font=("Cambria", 20), fg=COLOR_BLUE, bg=COLOR_WHITE)
        wish.place(relx=0.5, rely=0.5, anchor="center")

        tmp_1 = tk.Label(root, text="1233", font=("Eras Medium ITC", 15), fg="#c124af", bg=COLOR_WHITE)
        tmp_1.place(x=0, rely=0.5, anchor="w")
        
        tmp_2 = tk.Label(root, text="hehehe", font=("Cambria", 15), fg="#B65426", bg=COLOR_BLACK)
        tmp_2.place(relx=0, rely=0.1, anchor="nw")


    def layout_grid():
        # Cấu hình các cột với kích thước tối thiểu
        root.grid_columnconfigure(0, minsize=50, weight=1)
        root.grid_columnconfigure(1, minsize=50, weight=1)
        root.grid_columnconfigure(2, minsize=50, weight=1)

        # root.columnconfigure(0, weight=1)
        # root.columnconfigure(1, weight=1)
        # root.columnconfigure(2, weight=1)

        root.grid_rowconfigure(0, minsize=50, weight=1)


        # Thêm các nhãn vào các cột khác nhau
        res_1 = tk.Label(root, text="Column 1", font=("Cambria", 15), fg=COLOR_BLACK, bg=COLOR_WHITE, padx=10, pady=5)
        res_1.grid(row=0, column=0, sticky="nw")

        res_2 = tk.Label(root, text="Column 2", font=("Cambria", 15), fg=COLOR_BLACK, bg=COLOR_WHITE, padx=10, pady=5)
        res_2.grid(row=0, column=1, sticky="n")

        res_3 = tk.Label(root, text="Column 3", font=("Cambria", 15), fg=COLOR_BLACK, bg=COLOR_WHITE, padx=10, pady=5)
        res_3.grid(row=0, column=2, sticky="ne")
    

    # layout_pack()               # pack() và grid() sẽ xung đột nhau nên không để cùng được
    # layout_place()
    layout_grid()

inside()


def showHello():
    print("Hello")
def showName(name):                 # Truyền tham số để có thể dùng nhiều lần
    print("Hello", name)


# Use .place()
def buttonFirst():         
    font_text = font.Font(family="Cambria", size=20)

    # Nếu ghi showHello() thì sẽ mặc định gọi hàm khi chưa click. Vì thế chỉ nên ghi showHello
    bt_hello = tk.Button(root, text="Click here", font=font_text, fg=COLOR_ORANGE, bg=COLOR_WHITE, activebackground=COLOR_BLUE, padx=10, pady=5, command=showHello)
    bt_hello.place(relx=0.25, rely=0.5, anchor="center")

    # Vì có hàm truyền tham số nên phải thêm  lambda
    bt_name = tk.Button(root, text="Name", font=font_text, fg=COLOR_ORANGE, bg=COLOR_WHITE, activebackground=COLOR_BLUE, padx=10, pady=5, command=lambda: showName("A"))
    bt_name.place(relx=0.75, rely=0.5, anchor="center")    


# Use .grid()
def buttonSecond():       
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

    font_text = font.Font(family="Cambria", size=20)

    bt_one = tk.Button(root, text="One", font=font_text, fg=COLOR_ORANGE, bg=COLOR_WHITE, activebackground=COLOR_BLUE, padx=10, pady=5, command=showHello)
    bt_one.grid(row=1, column=0)

    # Vì có hàm truyền tham số nên phải thêm  lambda
    bt_two = tk.Button(root, text="Two", font=font_text, fg=COLOR_ORANGE, bg=COLOR_WHITE, activebackground=COLOR_BLUE, padx=10, pady=5, command=lambda: showName("A"))
    bt_two.grid(row=1, column=1) 

    bt_three = tk.Button(root, text="Three", font=font_text, fg=COLOR_ORANGE, bg=COLOR_WHITE, activebackground=COLOR_BLUE, padx=10, pady=5, command=lambda: showName("B"))
    bt_three.grid(row=1, column=2) 


buttonFirst()
buttonSecond()

root.mainloop()
