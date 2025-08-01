from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json


def buscar(termino, tipo):
    bander = True
    try:
        # Libros
        libros = leer_json(archivo_libros)
        for libro in libros:
            if libro[tipo] == termino:
                bander = False
                print("="*20, "Libro encontrado", "="*20)
                print(libro)

        # Música
        musicas = leer_json(archivo_musica)
        for musica in musicas:
            if musica[tipo] == termino:
                bander = False
                print("="*20, "Música encontrado", "="*20)
                print(musica)

        # Películas
        peliculas = leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula[tipo] == termino:
                bander = False
                print("="*20, "Película encontrado", "="*20)
                print(pelicula)
        if bander:
            print("No se encontraron resultados.")
    except Exception as e:
        print(f"\nError en la edición: {str(e)}")