from tkinter import *
from tkinter.ttk import *

datas = []

def update ():
    show_list.delete (0, END)
    for n, p, a in datas:
        show_list.insert (END, n)

def add ():
    global datas
    datas.append ([name.get(), phone.get(), address_text.get(1.0, "end-1c")])
    update ()
    
def view ():
    name.set (datas [int(show_list.curselection ()[0])][0])
    phone.set(datas[int(show_list.curselection()[0])][1])
    address_text.delete(1.0,"end")
    address_text.insert(1.0, datas[int(show_list.curselection()[0])][2])
   
def delete ():
    del datas[int(show_list.curselection()[0])]
    update ()

def reset ():
    name.set('')
    phone.set('')
    address_text.delete(1.0,"end")

root = Tk (screenName="Address book")
root.title ("Address book")
root.geometry ('600x600')

name = StringVar ()
phone = StringVar ()

# Frame name
name_frame = Frame (master=root)
name_label = Label (master=name_frame, text="Name", width= 10)
name_entry = Entry (master=name_frame,textvariable=name, width=30)

# Sắp xếp frame name
name_label.grid (row=0, column=0, sticky="w")
name_entry.grid (row=0,column=1, sticky="w")
name_frame.grid (row=0, padx=10, pady=5, sticky="w")

# Frame phone
phone_frame = Frame (master=root)
phone_label = Label (master=phone_frame, text="Phone No.", width=10)
phone_entry = Entry (master=phone_frame, textvariable=phone, width=30)

# Grid phone frame
phone_label.grid (row=0, column=0, sticky="w")
phone_entry.grid (row=0, column=1, sticky="w")
phone_frame.grid (row=1, padx=10, pady=5, sticky="w")

# Frame address
address_frame = Frame (master=root)
address_label = Label (master=address_frame, text="Address", width=10)
address_text = Text (master=address_frame, width=60, height=5)

# Grid address frame
address_label.grid (row=0, column=0, sticky="w")
address_text.grid (row=0, column=1, sticky="w")
address_frame.grid (row=2, padx=10, pady=5, sticky= "w")

# Frame show
show_frame = Frame (master=root)

# Button frame
button_frame = Frame (master=show_frame, width=10)
add_bnt = Button (master=button_frame, text="Add", width=5, command=add)
view_bnt = Button (master=button_frame, text="View", width=5, command=view)
delete_bnt = Button (master=button_frame, text="Delete", width=5, command=delete)
reset_bnt = Button (master=button_frame, text="Reset", width=5, command=reset)

# Scroll bar
scroll_bar = Scrollbar(master=show_frame, orient=VERTICAL)
# Show text
show_list = Listbox (master=show_frame, yscrollcommand=scroll_bar.set, height=20, width=50)
# link scroll bar
scroll_bar.config(command=show_list.yview)

# Show grid
add_bnt.grid (row=0, pady=20)
view_bnt.grid (row=1, pady=20)
delete_bnt.grid (row=2, pady=20)
reset_bnt.grid (row=3, pady=20)
button_frame.grid (row=0, column=0)
show_list.grid (row=0, column=1, padx=10, pady=5)
scroll_bar.grid(row=0, column=2)
show_frame.grid (row=3, padx=10, pady=10, sticky="w")

# Execute Tkinter
root.mainloop ()