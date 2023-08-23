from tkinter import *
from tkinter import ttk

def obtener():
    l2.config(text=combo.get())
    
    
inicio = Tk()
inicio.geometry('600x400') # Defino Ventana
inicio.resizable(0, 0) # indico que no pueda cambiar de forma
lenguajes =["Java","Python","C", "C++"]
l1 = Label(inicio, text="Seleccione favorito: ")
l1.grid(column=0, row=0)
combo = ttk.Combobox(inicio, values=lenguajes, width=50)
combo.grid(column=1, row=0)
combo.current(0) # Selecciono elemento del combo
b = Button(inicio, text="Ver seleccionado",command=obtener)
b.grid(column=0, row=1)
l2 = Label(inicio,text="")
l2.grid(column=0, row=2)
mainloop()
