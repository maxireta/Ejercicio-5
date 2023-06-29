class Pelicula:
    def __init__(self, titulo, resumen, lenguaje, fecha, generos):
        self.__tit = titulo
        self.__res = resumen
        self.__len = lenguaje
        self.__fec = fecha
        self.__gen = generos
    def getTitulo(self):
        return self.__tit
    def getResumen(self):
        return self.__res
    def getLenguaje(self):
        return self.__len
    def getFecha(self):
        return self.__fec
    def getGeneros(self):
        return self.__gen