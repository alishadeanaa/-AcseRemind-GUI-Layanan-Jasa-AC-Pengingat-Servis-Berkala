from tkinter import *
import customtkinter as ct

window = Tk()
window.title("AC seRemind")
window.state('zoomed')
window.resizable(0,0)

thisframe = LabelFrame(window)
thisframe.grid()

imagebg = PhotoImage(file="loginn2.jpg")
lbl = Label(thisframe, image=imagebg)
lbl.grid()

logo = PhotoImage(file=".png")
lbl_lpgo = ct.CTkLabel(thisframe, image=logo, corner_radius=10, bg_color= 'white' )
lbl_lpgo.place(x=450, y= 600)

window.mainloop()