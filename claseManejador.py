from claseGenero import Genero
from clasePelicula import Pelicula
import json
import requests

API_KEY = "32963cdc4b2e1ce4c52a0db1e7683037"

class Manejador:
    def __init__(self):
        self.__gen = []
        self.__pel = []
    def mostrarG(self):
        for i in self.__gen:
            print(f"Id {i.getId()}, Name {i.getName()}")
    def cargaP(self):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        pel = data["results"]
        for i in pel:
            titulo = i["original_title"]
            resumen = i["overview"]
            lenguaje = i["original_language"]
            fecha = i["release_date"]
            generos = i["genre_ids"]
            ab = Pelicula(titulo, resumen, lenguaje, fecha, generos)
            self.__pel.append(ab)
    def mostrarP(self):
        for i in self.__pel:
            print(f"Titulo: {i.getTitulo()}")
    def getListap(self):
        return self.__pel
    def obtenerGeneros(self, ids):
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        generos = data["genres"]
        nombres_generos = [genero["name"] for genero in generos if genero["id"] in ids]
        return nombres_generos
    def buscarGenero(self, gene):
        i = 0
        band = False
        while band is False and i < len(self.__gen):
            if self.__gen[i].getId() == gene:
                gg = self.__gen[i].getName()
                band = True
            i += 1
        return gg