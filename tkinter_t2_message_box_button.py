import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Add Message Box
print("Message Box")
messagebox.showinfo("Python","Python with Tkinter")

def clicked():
    messagebox.showinfo("Python","Python with Tkinter")
    btn=Button(window,text='Enter',command=clicked)
    
