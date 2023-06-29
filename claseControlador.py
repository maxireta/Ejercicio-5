from claseVentana import Ventana
from claseManejador import Manejador

class Control(object):
    def __init__(self, manejador, ventana):
        self.__man = manejador
        self.__ven = ventana
        self.__pel = self.__man.getListap() 
    def seleccionarPeli(self, index):
        peli = self.__pel[index]
        generos = peli.getGeneros()
        gen = self.__man.obtenerGeneros(generos)
        self.__ven.verPeli(peli, gen)
    def start(self):
        for i in self.__pel:
            self.__ven.agregarPeli(i)
        self.__ven.mainloop()