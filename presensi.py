import tkinter as tk
from tkinter import ttk
import openpyxl

window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)

def load_data():
    path = 'data_pengenalan_wajah.xlsx'
    wb = openpyxl.load_workbook(path)
    sheet = wb.active

    list_values = list(sheet.values)
    print(list_values)
    for cols in list_values[0]:
        treeview.heading(cols, text=cols)
    
    for value_tuple in list_values[1:]:
        treeview.insert('', tk.END, values=value_tuple)


frame = ttk.Frame(window)
frame.pack()

treeframe = ttk.Frame(frame)
treeframe.grid(row=0, column=0, padx=10, pady=10)
treescroll = ttk.Scrollbar(treeframe)
treescroll.pack(side='right', fill='y')

cols = ('No', 'Nama', 'Waktu')
treeview = ttk.Treeview(treeframe, columns=cols, show='headings',yscrollcommand=treescroll.set, height=31)
treeview.column("No", width=50)
treeview.column("Nama", width=200)
treeview.column("Waktu", width=200)
treeview.pack()
treescroll.config(command=treeview.yview)
load_data()

window.title("Data Presensi")
window.mainloop()