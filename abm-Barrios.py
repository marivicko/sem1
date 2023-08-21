import tkinter as tk
from tkinter import ttk



def limpiar():
    entrada1.delete(0,tk.END) 
    entrada2.delete(0,tk.END) 
    entrada3.delete(0,tk.END) 
    entrada4.delete(0,tk.END) 
    entrada5.delete(0,tk.END) 
    entrada6.delete(0,tk.END) 
    
    
def agregar():
    global auto 
    auto.insert(0,entrada1.get())
    auto.insert(1,entrada2.get())
    auto.insert(2,entrada3.get())
    auto.insert(3,entrada4.get())
    auto.insert(4,entrada5.get())
    auto.insert(5,entrada6.get())
    mi_lista.insert(tk.END, auto)
    auto = [] 
    limpiar()
    
#esta funcion se dispara luego de hacer doble click sobre el registro del listbox
def obtenerIndice(event):
    limpiar()
    global indice
    global lista
    indice = mi_lista.curselection()[0]
    #print("indice: ", indice)
    
    lista = list(mi_lista.get(indice))
    
    #print(lista)#imprimo la lista para saber si los datos estan correctos
    obtenerCampos(lista)

def obtenerCampos(list):
    
    entrada1.insert(0,list[0])
    entrada2.insert(0,list[1])
    entrada3.insert(0,list[2])
    entrada4.insert(0,list[3])
    entrada5.insert(0,list[4])
    if list[5] == 'Público':
        print("publico")
        entrada6.current(1)
    elif list[5] == 'Privado':
        print("privado")
        entrada6.current(2)
    
def eliminar():
    mi_lista.delete(mi_lista.curselection())
    
 
def modificar():
    #esta funcion se ejecuta cuando el usuario haya cambiado los valores de la modificacion
    global lista
    global indice
   # print("indice: ",indice,"Lista: ",lista)
    #cargo en la lista global los nuevos valores
    lista[0]=entrada1.get()
    lista[1]=entrada2.get()
    lista[2]=entrada3.get()
    lista[3]=entrada4.get()
    lista[4]=entrada5.get()
    lista[5]=entrada6.get()
   
    mi_lista.delete(indice)
    mi_lista.insert(indice,tuple(lista))

    
def llamada():
    eliminar()
    agregar()
    limpiar()    
    

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('ABM BARRIOS')

auto=[] #lista vacia
lista = []
indice = 0
opciones=("","Público", "Privado") 


entrada_var=tk.StringVar()
entrada_var2=tk.StringVar()
entrada_var3=tk.StringVar()
entrada_var4=tk.StringVar()
entrada_var5=tk.StringVar()
entrada_var6=tk.StringVar()

etiqueta1=tk.Label(ventana,text="Patente")
etiqueta1.grid(row=0,column=0, sticky='W')
entrada1=tk.Entry(ventana,textvariable=entrada_var)
entrada1.grid(row=0,column=1,)

etiqueta2=tk.Label(ventana,text="Marca")
etiqueta2.grid(row=1, column=0, sticky="w", pady=4)
entrada2=tk.Entry(ventana,textvariable=entrada_var2)
entrada2.grid(row=1,column=1)

etiqueta3=tk.Label(ventana,text="Modelo")
etiqueta3.grid(row=2, column=0, sticky="w", pady=4)
entrada3=tk.Entry(ventana,textvariable=entrada_var3)
entrada3.grid(row=2,column=1)

etiqueta4=tk.Label(ventana,text="tipo")
etiqueta4.grid(row=3, column=0, sticky="w", pady=4)
entrada4=tk.Entry(ventana,textvariable=entrada_var4)
entrada4.grid(row=3,column=1)

etiqueta5=tk.Label(ventana,text="Color")
etiqueta5.grid(row=4, column=0, sticky="w", pady=4)
entrada5=tk.Entry(ventana,textvariable=entrada_var5)
entrada5.grid(row=4,column=1)

etiqueta6=tk.Label(ventana,text="Uso")
etiqueta6.grid(row=5, column=0, sticky="w", pady=4)
entrada_var6 = tk.StringVar()
entrada6 = ttk.Combobox(ventana, justify="center", values=opciones, textvariable=entrada_var6)
entrada6.grid(row=5, column=1)

b1=tk.Button(ventana,text="Agregar",command=agregar)
b1.grid(row=6, column=0)
b2=tk.Button(ventana,text="Eliminar",command=eliminar)
b2.grid(row=6, column=1)

b4=tk.Button(ventana,text="Modificar",command=modificar)
b4.grid(row=6, column=3)

mi_lista=tk.Listbox(ventana,width=40)
mi_lista.bind('<Double-1>',obtenerIndice)
mi_lista.grid(row=7,columnspan=5)


ventana.mainloop()