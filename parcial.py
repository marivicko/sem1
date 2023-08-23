from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

contador = 0
empresas = {}
uso = ("Pública", "Privada", "Mixta")
noimoirrta = ("Presencial", "Virtual", "Híbrida")

def limpieza() -> None:
    c1.config(text="")
    c2.config(text="")
    c3.config(text="")
    c4.config(text="")
    c5.config(text="")
    c6.config(text="")

def reinicio() -> None:
    cuilvar.set()
    marcavar.set("")
    modelovar.set()
    p4.set(False)
    p5.set(False)
    suuso.set("")
    nomeiporrrta.set("")







def rs_invalido() -> bool:
    if marcavar.get() == "":
        c2.config(text="Está vacío")
        return True
    return False

def cantidad_invalida() -> bool:
    valor: int
    try:
        valor = modelovar.get()
    except:
        c3.config(text="No es un número")
        return True
    if valor <= 0:
        c3.config(text="Cantidad inválida")
        return True
    return False

def margen_puerta() -> bool:
    if p4.get() == False and p5.get() == False:
        c4.config(text="¿No vende nada?")
        return True
    return False

def procedencia_invalida() -> bool:
    if suuso.get() not in uso:
        c5.config(text="Opción inválida")
        return True
    return False



def indice(elemento: str, tupla: tuple) -> int:
    for ind, elem in enumerate(tupla):
        if elemento == elem:
            return ind

def es_valido() -> bool:
    limpieza()
    
    b2 = rs_invalido()
    b3 = cantidad_invalida()
    b4 = margen_puerta()
    b5 = procedencia_invalida()
    
    if b1 or b2 or b3 or b4 or b5:
        return False
    return True

def es_validable(cuit: int) -> bool:
    limpieza()
   
    b2 = rs_invalido()
    b3 = cantidad_invalida()
    b4 = margen_puerta()
    b5 = procedencia_invalida()
    
    if b1 or b2 or b3 or b4 or b5:
        return False
    return True

def agregar() -> None:
    global contador, empresas
    if es_valido():
        contador += 1
        vende = 0
        vende += 1 if p4.get() == True else 0
        vende += 2 if p5.get() == True else 0
        procedencia = indice(suuso.get(), uso)
        esquema = indice(nomeiporrrta.get(), noimoirrta)
        empresas[contador] = (cuilvar.get(), marcavar.get(), modelovar.get(), vende, procedencia, esquema)
        caja.insert("end", str(contador)+"-"+str(cuilvar.get()))
        reinicio()

def al_seleccionar(evento) -> None:
    elemento = evento.widget
    ind: int = caja.curselection()[0]
    elemento: str = caja.get(ind)
    contador = int(elemento[0])
    cuilvar.set(empresas[contador][0])
    marcavar.set(empresas[contador][1])
    modelovar.set(empresas[contador][2])
    p4.set(empresas[contador][3] % 2 == 1)
    p5.set(empresas[contador][3] // 2 == 1)
    suuso.set(uso[empresas[contador][4]])
    nomeiporrrta.set(noimoirrta[empresas[contador][5]])

def modificar() -> None:
    global empresas
    limpieza()
    if caja.curselection():
        ind: int = caja.curselection()[0]
        elemento: str = caja.get(ind)
        cuit = int(elemento[2:len(elemento)])
        if es_validable(cuit):
            contador = int(elemento[0])
            vende = 0
            vende += 1 if p4.get() == True else 0
            vende += 2 if p5.get() == True else 0
            procedencia = indice(suuso.get(), uso)
            esquema = indice(nomeiporrrta.get(), noimoirrta)
            empresas[contador] = (cuilvar.get(), marcavar.get(), modelovar.get(), vende, procedencia, esquema)
            caja.delete("active", "active")
            caja.selection_clear(0, "end")
            caja.insert(ind, str(contador)+"-"+str(cuilvar.get()))
            reinicio()
    else:
        showinfo("Modificación", "Para modificar, primero debe seleccionar un elemento")   

def quitar():
    global empresas
    limpieza()
    if caja.curselection():
        elemento: str = caja.get(caja.curselection()[0])
        empresas.pop(int(elemento[0]))
        caja.delete("active", "active")
        caja.selection_clear(0, "end")
        reinicio()
    else:
        showinfo("Baja", "Para borrar, primero debe seleccionar un elemento")

inicio = Tk()
inicio.resizable(0, 0)
inicio.title("abm")
Label(inicio, text="Registro de autos", font=("Times New Roman", 28, "bold")).grid(row=0, column=0, columnspan=5)
barra = Scrollbar(inicio)
barra.grid(row=1, column=1, rowspan=7)
caja = Listbox(inicio)
caja.bind('<<ListboxSelect>>', al_seleccionar)
caja.grid(row=1, column=0, rowspan=7)
caja.config(yscrollcommand=barra.set)
barra.config(command=caja.yview)
Label(inicio, text="PATENTE", font=("Arial", 12, "italic")).grid(row=1, column=2)
Label(inicio, text="MARCA", font=("Arial", 12, "italic")).grid(row=1, column=3)
Label(inicio, text="MODELO", font=("Arial", 12, "italic")).grid(row=1, column=4)
cuilvar = IntVar(inicio)
marcavar = StringVar(inicio)
modelovar = IntVar(inicio)
entrada1 = Entry(inicio, highlightthickness=1, highlightbackground="black", highlightcolor="black", justify="center", textvariable=cuilvar)
entrada2 = Entry(inicio, highlightthickness=1, highlightbackground="black", highlightcolor="black", justify="center", textvariable=marcavar)
entrada3 = Entry(inicio, highlightthickness=1, highlightbackground="black", highlightcolor="black", justify="center", textvariable=modelovar)
entrada1.grid(row=2, column=2)
entrada2.grid(row=2, column=3)
entrada3.grid(row=2, column=4)
c1 = Label(inicio, text="", font=("Helvetica", 10), foreground="#ff0000")
c2 = Label(inicio, text="", font=("Helvetica", 10), foreground="#ff0000")
c3 = Label(inicio, text="", font=("Helvetica", 10), foreground="#ff0000")
c1.grid(row=3, column=2)
c2.grid(row=3, column=3)
c3.grid(row=3, column=4)
p4 = BooleanVar(inicio, False)
ppuertita = Checkbutton(inicio, text="5 PUERTAS", font=("Arial", 12), variable=p4)
'''
El parámetro sticky alinea el elemento a la dirección indicada
Recibe un string como valor válido, indicando un punto cardinal;
    esto es norte(n), sur(s), este(e) y oeste(w).
Se admiten puntos ordinales también (ne, nw, se, sw)
'''
ppuertita.grid(row=4, column=2, sticky="w")
p5 = BooleanVar(inicio, False)
servicios = Checkbutton(inicio, text="4 PUERTAS", font=("Arial", 12), variable=p5)
servicios.grid(row=5, column=2, sticky="w")
Label(inicio, text="Origen de uso", font=("Arial", 12, "italic")).grid(row=4, column=3)
Label(inicio, text="Esquema noimoirrta", font=("Arial", 12, "italic")).grid(row=4, column=4)
suuso = StringVar(inicio)
e5 = ttk.Combobox(inicio, justify="center", values=uso, textvariable=suuso)
nomeiporrrta = StringVar(inicio)
e6 = ttk.Combobox(inicio, justify="center", values=noimoirrta, textvariable=nomeiporrrta)
e5.grid(row=5, column=3)
e6.grid(row=5, column=4)
c4 = Label(inicio, text="qure es esto", font=("Helvetica", 10), foreground="#ff0000")
c5 = Label(inicio, text="", font=("Helvetica", 10), foreground="#ff0000")
c6 = Label(inicio, text="", font=("Helvetica", 10), foreground="#ff0000")
c4.grid(row=6, column=2)
c5.grid(row=6, column=3)
c6.grid(row=6, column=4)
b1 = Button(inicio, text='Agregar', command=agregar, background="#00ff00", foreground="#ffffff", font=("Unicode", 14, "roman"))
b2 = Button(inicio, text='Modificar', command=modificar, background="#0000ff", foreground="#ffffff", font=("Unicode", 14, "roman"))
b3 = Button(inicio, text='Quitar', command=quitar, background="#ff0000", foreground="#ffffff", font=("Unicode", 14, "roman"))
b1.grid(row=7, column=2)
b2.grid(row=7, column=3)
b3.grid(row=7, column=4)
mainloop()