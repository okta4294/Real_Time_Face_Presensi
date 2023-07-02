import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)
input_frame = ttk.Frame(window)

input_frame.pack(padx=20, pady=20, fill='x', expand=True)
def click():
    import capture_face.py
def click1():
    import training.py
def click2():
    import face_recognition.py
tombol = ttk.Button( input_frame, text="Capture", command= click)
tombol.pack(fill='y', expand=True, padx=10, pady=10)
tombol1 = ttk.Button( input_frame, text="Training", command= click1)
tombol1.pack(fill='y', expand=True, padx=10, pady=10)
tombol2 = ttk.Button( input_frame, text="Scan Your Face", command= click1)
tombol2.pack(fill='y', expand=True, padx=10, pady=10)


window.title("ANJAY")
window.mainloop()