from claseVentana import Ventana
from claseManejador import Manejador
from claseControlador import Control

if __name__ == '__main__':
    a = Manejador()
    a.cargaP()
    b = Ventana()
    c = Control(a, b)
    b.setControlador(c)
    c.start()