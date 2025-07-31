from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json


def editar_por_titulo(termino):
    resultados = []
    try:
        # Libros
        libros = leer_json(archivo_libros)
        for libro in libros:
            if libro["nombre"] == termino:
                resultados.append(libro)

        # Música
        musicas = leer_json(archivo_musica)
        for musica in musicas:
            if musica["nombre"] == termino:
                resultados.append(musica)

        # Películas
        peliculas = leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula["nombre"] == termino:
                resultados.append(pelicula)
    except Exception as e:
        print(f"\nError en la edición: {str(e)}")
    
    return resultados

def editar_por_autor(termino):
    resultados = []
    try:
        libros = leer_json(archivo_libros)
        for libro in libros:
            if libro["autor"] == termino:
                resultados(libro)

        musicas = leer_json(archivo_musica)
        for musica in musicas:
            if musica["autor"] == termino:
                resultados(musica)

        peliculas = leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula["autor"] == termino:
                resultados(pelicula)
    except Exception as e:
        print(f"\nError en la edición: {str(e)}")
    
    return resultados

def editar_por_genero(termino):
    resultados = []
    try:
        libros = leer_json(archivo_libros)
        for libro in libros:
            if libro["genero"] == termino:
                resultados.append(libro)

        musicas = leer_json(archivo_musica)
        for musica in musicas:
            if musica["genero"] == termino:
                resultados.append(musica)

        peliculas = leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula["genero"] == termino:
                resultados.append(pelicula)

    except Exception as e:
        print(f"\nError en la edición: {str(e)}")
    
    return resultados
