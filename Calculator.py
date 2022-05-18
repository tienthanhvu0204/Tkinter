# Máy tính đơn giản
from tkinter import *

# Tạo biến lưu biểu thức và kết quả
expression = ""
result = ""

# Hàm xóa biểu thức
def clear_expression ():
    text.delete ("1.0", "end")

# Hàm nhập số
def press_num (num):
    global expression
    text.insert ("end", num)
    expression = text.get("1.0", "end")

# Hàm tính kết quả
def calculate ():
    global expression, result
    expression = text.get("1.0", "end")
    try:
        result = str (eval (expression))
    except:
        result = "Biểu thức sai"
    text.insert ("end","\n---------\n={}".format(result))
    # print (result)

# Khởi tạo GUI
root = Tk ()
root.title ("Simple Calculator")
root.config (background="#AFEEEE")

# Tạo widget text hiển thị biểu thức và kết quả
text = Text (root, font=("arial", 13), height=3, width=40)

# Tạo frame chứa các button số và phép tính
frame = Frame (root)

# Các button số
btn1 = Button (frame, text="1", command=lambda: press_num (1), width=5)
btn2 = Button (frame, text="2", command=lambda: press_num (2), width=5)
btn3 = Button (frame, text="3", command=lambda: press_num (3), width=5)
btn4 = Button (frame, text="4", command=lambda: press_num (4), width=5)
btn5 = Button (frame, text="5", command=lambda: press_num (5), width=5)
btn6 = Button (frame, text="6", command=lambda: press_num (6), width=5)
btn7 = Button (frame, text="7", command=lambda: press_num (7), width=5)
btn8 = Button (frame, text="8", command=lambda: press_num (8), width=5)
btn9 = Button (frame, text="9", command=lambda: press_num (9), width=5)
btn0 = Button (frame, text="0", command=lambda: press_num (0), width=5)

# Các button chức năng
btn_plus = Button (frame, text="+", command=lambda: press_num ("+"), width=5)
btn_minus = Button (frame, text="-", command=lambda: press_num ("-"), width=5)
btn_multiply = Button (frame, text="*", command=lambda: press_num ("*"), width=5)
btn_divide = Button (frame, text="/", command=lambda: press_num ("/"), width=5)
btn_point = Button (frame, text=".", command=lambda: press_num ("."), width=5)
btn_clear = Button (frame, text="clear", command= clear_expression, width=5)
btn_result = Button (frame, text="=", command=calculate, width=5)

# Sắp xếp các widget con của root
text.grid (row=0, padx=10, pady=10)
frame.grid (row=1, padx=10, pady=10)

# Sắp xếp các button số con của frame
btn1.grid (row=0 , column=0)
btn2.grid (row=0 , column=1)
btn3.grid (row=0 , column=2)
btn4.grid (row=1 , column=0)
btn5.grid (row=1 , column=1)
btn6.grid (row=1 , column=2)
btn7.grid (row=2 , column=0)
btn8.grid (row=2 , column=1)
btn9.grid (row=2 , column=2) 
btn0.grid (row=3 , column=0)

# Sắp xếp các button chức năng con của frame
btn_plus.grid (row=0 , column=3)
btn_minus.grid (row=1 , column=3)
btn_multiply.grid (row=2 , column=3)
btn_divide.grid (row=3 , column=3)
btn_clear.grid (row=3 , column=1)
btn_result.grid (row=3 , column=2)
btn_point.grid (row=4 , column=0)

# Excecute TK 
root.mainloop ()