from tkinter import *
from tkinter import ttk

class PeliLista(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.__lb = Listbox(self, **kwargs)
        scroll = Scrollbar(self, command= self.__lb.yview)
        self.__lb.config(yscrollcommand=scroll.set)
        scroll.pack(side= RIGHT, fill= Y)
        self.__lb.pack(expand= True, fill = BOTH)
    def agregar(self, pel, index=END):
        text = f"{pel.getTitulo()}"
        self.__lb.insert(index, text)
    def dobleclick(self, callback):
        handler = lambda ev: callback(self.__lb.curselection()[0])
        self.__lb.bind("<Double-Button-1>", handler)

class Mostrador(LabelFrame):
    def __init__(self, master, **kwargs):
        self.__tit = StringVar()
        self.__res = StringVar()
        self.__len = StringVar()
        self.__fec = StringVar()
        self.__gen = StringVar()
        super().__init__(master, text="Película", **kwargs)
        fields = ("Titulo", "resumen", "lenguaje", "fecha", "generos")
        ttk.Label(self, text= "Titulo").place(x=5, y=10)
        ttk.Label(self, textvariable= self.__tit).place(x=60, y=10)
        ttk.Label(self, text= "Lenguaje").place(x=5, y= 30)
        ttk.Label(self, textvariable= self.__len).place(x=60, y=30)
        ttk.Label(self, text= "Fecha").place(x=5, y=50)
        ttk.Label(self, textvariable= self.__fec).place(x=60, y=50)
        ttk.Label(self, text= "Generos").place(x=5, y=70)
        ttk.Label(self, textvariable= self.__gen).place(x=60, y=70)
        ttk.Label(self, text= "Resumen").place(x=5, y=90)
        ttk.Label(self, textvariable= self.__res, width=300, wraplength=250).place(x=60, y=90)
    def mostrarpeli(self, peli, gen):
        self.__tit.set(peli.getTitulo())
        self.__len.set(peli.getLenguaje())
        self.__fec.set(peli.getFecha())
        self.__gen.set(gen)
        self.__res.set(peli.getResumen())

class Ventana:
    def __init__(self):
        self.__a = Tk()
        self.__a.title("Cinéfilos Argentinos")
        self.__a.geometry("500x250")
        self.__list = PeliLista(self.__a, height = 14, borderwidth = 2, relief = "sunken")
        self.__list.place(x=5, y=6)
        self.__peli = Mostrador(self.__a, width = 340, height = 240)
        self.__peli.place(x= 150, y=5)
    def agregarPeli(self, peli):
        self.__list.agregar(peli)
    def setControlador(self, ctrl):
        self.__list.dobleclick(lambda index:ctrl.seleccionarPeli(index))
    def verPeli(self, peli, gen):
        self.__peli.mostrarpeli(peli, gen)
    def mainloop(self):
        self.__a.mainloop()