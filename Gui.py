import tkinter as tk
from tkinter import ttk
import os

#code untuk tampilan GUI
window = tk.Tk()
window.geometry("500x500") #ukuran window
window.resizable(False, False) #window tidak bisa diresize
big_frame = ttk.Frame(window) #frame untuk tombol
big_frame.pack(padx=20, pady=20, fill='x',expand=True) #padding frame

#load theme
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

#fungsi dari semua tombol
def click():
    os.system ("python capture_face.py") #memanggil file capture_face.py
def click1():
    os.system ("python training.py")
def click2():
    os.system ("python face_recognition.py")
def click3():
    os.system ("python presensi.py")


#code untuk memasukkan tombol
tombol = ttk.Button(big_frame,text="Capture",style='Accent.TButton', command= click)
tombol.pack(padx=10, pady=30,anchor='center')
tombol1 = ttk.Button(big_frame, text="Training",style='Accent.TButton', command= click1)
tombol1.pack(padx=10, pady=30,anchor='center')
tombol2 = ttk.Button(big_frame,text="Scan Your Face",style='Accent.TButton', command= click2)
tombol2.pack(padx=10, pady=30,anchor='center')
tombol3 = ttk.Button(big_frame,text="Data Presensi",style='Accent.TButton', command= click3)
tombol3.pack(padx=10, pady=30,anchor='center')


window.title("Face Recognition System")
window.mainloop()