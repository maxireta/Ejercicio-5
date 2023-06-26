from tkinter import messagebox
import tkinter as tk
import requests
import json

API_KEY = "32963cdc4b2e1ce4c52a0db1e7683037"

def obtener_peliculas():
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["results"]

def mostrar_detalles(event):
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        pelicula = peliculas[indice]
        mensaje = f"Título: {pelicula['title']}\n\nResumen: {pelicula['overview']}\n\nLenguaje original: {pelicula['original_language']}\n\nFecha de lanzamiento: {pelicula['release_date']}\n\nGéneros: {', '.join(obtener_nombres_generos(pelicula['genre_ids']))}"
        messagebox.showinfo("Detalles de la película", mensaje)

def obtener_nombres_generos(ids):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    generos = data["genres"]
    nombres_generos = [genero["name"] for genero in generos if genero["id"] in ids]
    return nombres_generos

peliculas = obtener_peliculas()

ventana = tk.Tk()
ventana.title("Cinéfilos Argentinos")
ventana.geometry("400x400")

listbox = tk.Listbox(ventana,width=100,height=100)
listbox.pack(pady=10)

for pelicula in peliculas:
    listbox.insert(tk.END, pelicula["title"])

listbox.bind("<Double-Button-1>", mostrar_detalles)

ventana.mainloop()