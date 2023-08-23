from posixpath import split
from tkinter import*
def agregar():
    viajesIn=[]
    viajesIn.insert(0,entrada1.get())
    viajesIn.insert(1,entrada2.get())
    viajesIn.insert(2,entrada3.get())
    viajesIn.insert(3,entrada4.get())
    viajesIn.insert(4,entrada5.get())
    viajesIn.insert(5,entrada6.get())
    viaje.append(viajesIn)
    lista.insert(END,viajesIn)
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    var6.set("")
def eliminar():
    lista.delete(lista.curselection())
def mostrar():
    
    var=lista.get(lista.curselection()) 
   
    print(var)
    origen=var[0]
    destino=var[1]
    salida=var[2]
    empresa=var[3]
    numeroanden=var[4]
    costo=var[5]
    entrada1.insert(END,origen)
    entrada2.insert(END,destino)
    entrada3.insert(END,salida)
    entrada4.insert(END,empresa)
    entrada5.insert(END,numeroanden)
    entrada6.insert(END,costo)
def modificar():
    eliminar()
    agregar()    
    
viaje=[]
root=Tk()
root.title("ABM")
miframe=Frame()
miframe.pack()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
Label(miframe,text="Origen").grid(row=0,column=0,sticky=W)
entrada1=Entry(miframe,textvariable=var1)
entrada1.grid(row=0,column=1,)
Label(miframe,text="Destino").grid(row=1,column=0,sticky=W)
entrada2=Entry(miframe,textvariable=var2)
entrada2.grid(row=1,column=1)
Label(miframe,text="Salida").grid(row=2,column=0,sticky=W)
entrada3=Entry(miframe,textvariable=var3)
entrada3.grid(row=2,column=1)
Label(miframe,text="Empresas").grid(row=3,column=0,sticky=W)
entrada4=Entry(miframe,textvariable=var4)
entrada4.grid(row=3,column=1)
Label(miframe,text="N° Anden").grid(row=4,column=0,sticky=W)
entrada5=Entry(miframe,textvariable=var5)
entrada5.grid(row=4,column=1)
Label(miframe,text="Costo").grid(row=5,column=0,sticky=W)
entrada6=Entry(miframe,textvariable=var6)
entrada6.grid(row=5,column=1)
Button(root,text="agregar",command=agregar).pack(side=LEFT)
Button(root,text="eliminar",command=eliminar).pack(side=LEFT)
Button(root,text="mostrar",command=mostrar).pack(side=LEFT)
Button(root,text="modificar",command=modificar).pack(side=LEFT)
lista=Listbox(miframe,bg="#f7ffde",font="Cosntantia")
lista.grid(row=6,columnspan=2)


mainloop()