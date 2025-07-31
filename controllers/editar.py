from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json
import json

def editar(termino, nuevo_dato, tipo):
    resultados = []
    try:
        libros = leer_json(archivo_libros)
        editado = False
        for libro in libros:
            if libro[tipo] == termino:
                libro[tipo] = nuevo_dato
                resultados.append(libro)
                editado = True
        if editado:
            with open(archivo_libros, "w") as f:
                json.dump(libros, f, indent=4)
        musicas = leer_json(archivo_musica)
        editado = False
        for musica in musicas:
            if musica[tipo] == termino:
                musica[tipo] = nuevo_dato
                resultados.append(musica)
                editado = True
        if editado:
            with open(archivo_musica, "w") as f:
                json.dump(musicas, f, indent=4)

        peliculas = leer_json(archivo_peliculas)
        editado = False
        for pelicula in peliculas:
            if pelicula[tipo] == termino:
                pelicula[tipo] = nuevo_dato
                resultados.append(pelicula)
                editado = True
        if editado:
            with open(archivo_peliculas, "w") as f:
                json.dump(peliculas, f, indent=4)

    except Exception as e:
        print(f"\nError en la edición: {str(e)}")
    return resultados
