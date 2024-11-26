import tkinter as tk
import random

LENGTH, HEIGHT = 400, 300
RIGHT, DOWN = 200, 100
RED = "#c6260d"
WHITE = "#ffffff"
BLACK = "#000000"
GREEN = "#22e11f"
YELLOW = "#fef65b"
BLUE = "#2a7cc1"


# Tạo cửa sổ
root = tk.Tk()
    # Trong 1 root chỉ được sử dụng 1 trong 3 (pack, place, grid), nếu không sẽ bị xung đột

def setupWindow():
    root.geometry("{}x{}+{}+{}".format(LENGTH, HEIGHT, RIGHT, DOWN))
    root.title("New App")
    photo = tk.PhotoImage(file="bg_pic.png")
    root.iconphoto(False, photo)

    # Cấu hình root để căn giữa
    root.grid_rowconfigure(0, weight=1)  # Cho phép hàng 0 co dãn
    root.grid_columnconfigure(0, weight=1)  # Cho phép cột 0 co dãn

    label_1 = tk.Label(root, image=photo)
    label_1.photo = photo                    # Keep a reference to avoid garbage collection
    label_1.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="nsew")    # Ảnh nền bao phủ toàn bộ lưới

    root.resizable(False, False)


def randomColor():
    r = lambda: random.randint(0, 255)
    return "#%02X%02X%02X" % (r(), r(), r())                # 2 là số lượng ký tự sau khi chuyển sang hệ 16
                                                            # print("%03X" % r)  # Kết quả là "0FF" với r=255

def changeColor(bg_color):
    label_title['bg'] = bg_color

def showInfo(name):
    print("There is a", name)

def create_button(name, bg_color, index, res):
    tmp = tk.Button(root, text=name, font=("Cambria", 15), fg=YELLOW, bg=bg_color,command=lambda: [changeColor(bg_color), showInfo(res)])
    tmp.grid(row=1, column=index, sticky="we", padx=30, pady=20)

def mainWindow():
    global label_title
    label_title = tk.Label(root, text="Hello", font=("Cambria", 20), fg=WHITE, bg=randomColor(), padx=20, pady=20)
    # label_title.place(relx=0.5, rely=0, anchor="n")   
    label_title.grid(row=0, column=0, columnspan=3, sticky="we", padx=30)

    create_button("Door 1", GREEN, 0, "Car")
    create_button("Door 2", BLACK, 1, "Snake")
    create_button("Door 3", RED, 2, "Tiger")

    # Cấu hình chiều cao và chiều rộng các dòng và cột
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    

setupWindow()
mainWindow()
root.mainloop()

