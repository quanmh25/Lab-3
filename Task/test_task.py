
import tkinter as tk
 

root=tk.Tk()
root.geometry("600x400")
 
name_var=tk.StringVar()
passw_var=tk.StringVar()

 
def submit():
    # Lấy dữ liệu khi người dùng nhập vào
    name=name_var.get()
    password=passw_var.get()
    # In ra terminal
    print("The name is : ",name)
    print("The password is : ",password)
    # Xóa dữ liệu
    name_var.set("")
    passw_var.set("")
    
    
# Creating a label for username and password
name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
name_label.grid(row=0, column=0)
passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
passw_label.grid(row=1, column=0)

# Creating a entry for password and username
name_entry = tk.Entry(root, text=name_var, font=('calibre', 10, 'normal'))
name_entry.grid(row=0,column=1)
passw_entry=tk.Entry(root, text=passw_var, font=('calibre', 10, 'normal'), show='*')
passw_entry.grid(row=1, column=1)

# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root, text='Submit', command=submit)
sub_btn.grid(row=2, column=1)


root.mainloop()


'''
1. Entry
    Mục đích: Dùng để nhập dữ liệu từ người dùng (input).
    Đặc điểm:
        Người dùng có thể chỉnh sửa nội dung.
        Thường được dùng trong các form nhập liệu, ví dụ: nhập tên, mật khẩu, số điện thoại,...
        Có thể liên kết với các biến kiểu StringVar để lấy hoặc cập nhật dữ liệu.
2. Label
    Mục đích: Dùng để hiển thị văn bản hoặc hình ảnh (output).
    Đặc điểm:
        Không cho phép người dùng chỉnh sửa nội dung.
        Chỉ hiển thị thông tin mà chương trình cung cấp.
        Thường được dùng để cung cấp thông báo, tiêu đề, hoặc dữ liệu kết quả.
'''
