from tkinter import *
from tkinter.ttk import *

def fahrenheit_to_celsius (): # Ham chuyen doi F => C
    fahrenheit = ent_temperature_fahrenheit.get ()
    celsius = (float (fahrenheit) - 32) * 5 / 9
    lbl_result_celcius["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

def celsius_to_fahrenheit (): # Ham chuyen doi C => F
    celsius = ent_temperature_celsius.get ()
    fahrenheit = float (celsius) * 9 / 5 + 32
    lbl_result_fahrenheit["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"

window = Tk () # Tao cua so chinh
window.title ("Temperature converter") # Dat tieu de cho cua so chinh
window.resizable (width=False, height=False) # Dat lai kich thuoc cho cua so chinh

# Tao frame nhap F, button chuyen doi, label hien thi ket qua:
frm_entry_fahrenheit = Frame (master = window) # Frame entry nhap gia tri F
ent_temperature_fahrenheit = Entry (master=frm_entry_fahrenheit, width=10) # Widget entry
lbl_temp_fahrenheit = Label (master=frm_entry_fahrenheit, text="\N{DEGREE FAHRENHEIT}") # Label F

ent_temperature_fahrenheit.grid (row=0, column=0, sticky="e") # Sap xep entry trong frame entry nhap F
lbl_temp_fahrenheit.grid (row=0, column=1, sticky="w") # Sap xep label F sau entry trong frame entry nhap F


# Button chuyen doi F sang C la con cua window, text la mui ten sang phai, command goi ham chuyen doi F
btn_convert_fahrenheit = Button (master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)

lbl_result_celcius = Label (master=window, text="\N{DEGREE CELSIUS}") # Label vung ket qua la gia tri do C nhan duoc

frm_entry_fahrenheit.grid (row=0, column=0, padx=10) # Sap xep frame entry, button, label ket qua padx la 10???
btn_convert_fahrenheit.grid (row=0, column=1, pady=10) # pady=10 ???
lbl_result_celcius.grid (row=0, column=2, padx=10)

# Tao frame nhap C, button chuyen doi, label hien thi ket qua:
frm_entry_celcius = Frame (master=window) # Frame entry nhap gia tri C
ent_temperature_celsius = Entry (master=frm_entry_celcius,width=10) # Widget entry nhap C nam trong frame nhap C
lbl_temp_celcius = Label (master=frm_entry_celcius, text="\N{DEGREE CELSIUS}") # Label C hien thi don vi nhap la oC

ent_temperature_celsius.grid (row=0, column=0, sticky="e") # Sap xep entry trong frame nhap C
lbl_temp_celcius.grid(row=0, column=1, sticky="w")

btn_convert_celcius = Button (master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=celsius_to_fahrenheit) # Button chuyen doi

lbl_result_fahrenheit = Label (master=window, text="\N{DEGREE FAHRENHEIT}") # Label hien thi ket qua

frm_entry_celcius.grid(row=1, column=0, padx=10) # Sap xep o dong thu 2
btn_convert_celcius.grid(row=1, column=1, pady=10)
lbl_result_fahrenheit.grid(row=1, column=2, padx=10)

window.mainloop () # Goi vong lap su kien chinh, de cac su kien dien ra tren window





