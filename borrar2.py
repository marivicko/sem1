from tkinter import *
def estados():
    cadena = ""
    if (var1.get() == 1):
        cadena = cadena + "Masculino "
    if (var2.get() == 1):
        cadena = cadena + "Femenino "
    if (var3.get() == 1):
        cadena = cadena + "Otro "
    l.config(text=cadena)
    
    
inicio = Tk()
var1 = IntVar()
Checkbutton(inicio, text="Masculino", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(inicio, text="Femenino", variable=var2).grid(row=1, sticky=W)
var3 = IntVar()
Checkbutton(inicio, text="Otro", variable=var3).grid(row=2, sticky=W)
l = Label(inicio, text= "")
l.grid(row=3)
Button(inicio, text='Valor', command=estados).grid(row=4, sticky=W)
Button(inicio, text='Salir', command=quit).grid(row=5, sticky=W)
mainloop()
