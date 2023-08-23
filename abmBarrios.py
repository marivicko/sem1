import tkinter as tk
from tkinter import ttk


def limpiar():
    entrada_patente.delete(0, tk.END)
    entrada_marca.delete(0, tk.END)
    entrada_modelo.delete(0, tk. END)
    entrada_tipo4.set('0') # ESTO PUSE PARA Q DEJE DE ESTAR CHECHEADO. Y SE BORRE 
    entrada_tipo5.set('0')
    entrada_color.delete(0, tk.END)
    entrada_uso.delete(0, tk.END)
    l.config(text='') # cambia el texto de la etiqueta
    
    
    
def agregar():
    global auto
    auto.insert(0,entrada_patente.get())
    auto.insert(1,entrada_marca.get())
    auto.insert(2,entrada_modelo.get())
    auto.insert(3,entrada_color.get())
    auto.insert(4, entrada_uso.get())
    #auto.insert(5, entrada_tipo5.get())
    #auto.insert(5, entrada_tipo5.get())
    mi_lista.insert(tk.END, auto)
    auto=[]
    limpiar()

    


def mostrar():
    
    cadena = ""
    if (entrada_tipo4.get() == 1):
        cadena = cadena + "4 puertas "
    if (entrada_tipo5.get() == 1):
        cadena = cadena + "5 puertas "
    l.config(text=cadena)
    
    
    
    
    
def obtenerIndice(event):
    limpiar()
    global indice
    global lista
    indice = mi_lista.curselection()[0]
    
    lista = list(mi_lista.get(indice))
    obtenerCampos(lista)
    
def obtenerCampos(list):
    
    entrada_patente.insert(0,list[0])
    entrada_marca.insert(0,list[1])
    entrada_modelo.insert(0,list[2])
    entrada_color.insert(0,list[3])
    entrada_uso.insert(0,list[4])
    if list[4] == 'Público':
         entrada_uso.current(1)
    elif list[4] == 'Privado':
        entrada_uso.current(2)


def modificar():
    global lista
    global indice
    lista[0]=entrada_patente.get()
    lista[1]=entrada_marca.get()
    lista[2]=entrada_modelo.get()
    lista[3]=entrada_color.get()
    lista[4]=entrada_uso.get()
   
    mi_lista.delete(indice)
    mi_lista.insert(indice,tuple(lista))
    

    
def eliminar():
    mi_lista.delete(mi_lista.curselection())
    

    
def llamada():
    limpiar
    agregar
    eliminar

        

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('ABM BARRIOS')

auto=[]
lista=[]
indice= 0
opciones= ('', 'Publico', 'Privado')
cadena = ""

entrada_patente= tk.StringVar()
entrada_marca= tk.StringVar()
entrada_modelo=tk.StringVar()
entrada_tipo4= tk.IntVar()
entrada_tipo5 = tk.IntVar()
entrada_color= tk.StringVar()
entrada_uso= tk.StringVar()
#lista= tk.Listbox()

etiqueta1=tk.Label(ventana,text="Patente")
etiqueta1.grid(row=0,column=0, sticky='W', pady=4)
entrada_patente= tk.Entry(ventana, textvariable=entrada_patente)
entrada_patente.grid(row=0, column=1)

etiqueta2=tk.Label(ventana, text="Marca")
etiqueta2.grid(row=1,column=0, sticky='W', pady=4)
entrada_marca= tk.Entry(ventana,textvariable=entrada_marca, )
entrada_marca.grid(row=1, column=1)

etiqueta3=tk.Label(ventana, text="Modelo")
etiqueta3.grid(row=2, column=0, sticky='W', pady=4)
entrada_modelo= tk.Entry(ventana, textvariable=entrada_modelo)
entrada_modelo.grid(row=2, column=1)

etiqueta4=tk.Label(ventana, text="Tipo")
etiqueta4.grid(row=3, column=0, sticky='W', pady=4)
ttk.Checkbutton(ventana, text= '4 Puertas', variable=entrada_tipo4).grid(row=3, column=2)
ttk.Checkbutton(ventana, text='5 Puetas', variable=entrada_tipo5). grid(row=3, column=1)

l = tk.Label(ventana, text= "")
l.grid(row=4, column=1)

etiqueta5=tk.Label(ventana, text="Color")
etiqueta5.grid(row=5, column=0, sticky='W', pady=4)
entrada_color= tk.Entry(ventana, textvariable=entrada_color)
entrada_color.grid(row=5, column=1)

etiqueta6=tk.Label(ventana, text="Uso")
etiqueta6.grid(row=6, column=0, sticky='W', pady=4)
entrada_uso= ttk.Combobox (ventana, values=opciones, textvariable=entrada_uso)
entrada_uso.grid(row=6, column=1)

mi_lista= tk.Listbox(ventana, width=50)
mi_lista.bind('<Double-1>',obtenerIndice)
mi_lista.grid(row=8, column=0, columnspan=4)

b0=tk.Button(ventana,text="Mostrar",command=mostrar)
b0.grid(row=3, column=3)

b1=tk.Button(ventana,text="Agregar",command=agregar)
b1.grid(row=7, column=0)

b2=tk.Button(ventana, text="Modificar", command=modificar)
b2.grid(row=7, column=1)

b3=tk.Button(ventana,text="Eliminar",command=eliminar)
b3.grid(row=7, column=2)



ventana.mainloop()