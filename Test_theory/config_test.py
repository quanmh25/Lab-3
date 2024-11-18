# File const for project

WINDOW_LENGTH = 600
WINDOW_HIGHT = 400
WINDOW_POSITION_RIGHT = 200
WINDOW_POSITION_DOWN = 200

COLOR_WHITE = "#ffffff"
COLOR_BLACK = "#000000"
COLOR_BG = "#fef65b"
COLOR_BLUE = "#0000ff"
COLOR_ORANGE = "#d85235"
COLOR_GREEN = "#22e11f"



FONT_TEXT = "Times New Roman"
SIZE_TEXT = 14


# Các giá trị hợp lệ của anchor="": 
#     "s", "n", "e", "w", "center"
#     "nw", "ne", "sw", "se"

# Trong Tkinter, side chỉ có thể nhận một trong các giá trị sau:
#     "top", "bottom", "right", "left"

# Có 3 phương thức trong label:
#     pack(): Có các tham số: side, fill, padx, pady, anchor để điều chỉnh vị trí và kích thước.
#     place(): Đặt widget vào một vị trí cụ thể theo tọa độ. Các tham số như x, y, relx, rely, anchor để điều chỉnh vị trí.
                    # x, y: tọa độ.   0 < relx, rely < 1: tỉ lệ tọa độ
#     grid(): Cho phép định vị widget bằng hàng và cột.