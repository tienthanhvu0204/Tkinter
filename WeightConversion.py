# Chuyển đổi cân nặng từ Kg sang Gram, Pounds, Ounce
from tkinter import *

# Hàm chuyển đổi, lấy giá trị weight, chuyển đổi và gán cho 3 label hiển thị
def convert ():
    global weight
    gram['text'] = round (float (weight.get ()) * 1000, 2)
    pounds['text'] = round (float (weight.get ()) * 2.20462, 2)
    ounce['text'] = round (float (weight.get ()) * 35.274, 2)

# Khởi tạo GUI
root = Tk ()
root.title ("Weight Conversion")

# Biến cân nặng
weight = StringVar ()

# Label, entry nhập giá trị KG, button convert
lbl0 = Label (root, text="Enter the weight in KG", width=25)
weight_entry = Entry (root, textvariable=weight, width=25)
btn = Button (root, text="Convert", width=10, command=convert)

# Label đơn vị
lbl1 = Label (root, text="Gram", width=25)
lbl2 = Label (root, text="Pounds", width=25)
lbl3 = Label (root, text="Ounce", width=25)

# Label hiển thị giá trị chuyển đổi
gram = Label (root, text=" ", width=25)
pounds = Label (root, text=" ", width=25)
ounce = Label (root, text=" ", width=25)

# Sắp xếp các widget
lbl0.grid (row=0, column=0, padx=5, pady=15)
weight_entry.grid (row=0, column=1, padx=5, pady=15)
btn.grid (row=0, column=2, padx=5, pady=15)

lbl1.grid (row=1, column=0, padx=5, pady=15)
lbl2.grid (row=1, column=1, padx=5, pady=15)
lbl3.grid (row=1, column=2, padx=5, pady=15)

gram.grid (row=2, column=0, sticky="w", padx=5, pady=15)
pounds.grid (row=2, column=1, sticky="w", padx=5, pady=15)
ounce.grid (row=2, column=2, sticky="w", padx=5, pady=15)

# Execute Tkinter
root.mainloop ()