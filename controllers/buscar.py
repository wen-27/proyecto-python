from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json
import tabulate 

def buscar(termino, tipo):
    resultados = []
    try:
        # Libros
        libros = leer_json(archivo_libros)
        for libro in libros:
            if libro[tipo] == termino:
                for i in libros:
                    print(i)
                    #print(tabulate.tabulate(libros, headers="keys", tablefmt="fancy_grid"))

        # Música
        musicas = leer_json(archivo_musica)
        for musica in musicas:
            if musica[tipo] == termino:
                for i in musicas:
                    print(i)

        # Películas
        peliculas = leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula[tipo] == termino:
                for i in peliculas:
                    print(i)

    except Exception as e:
        print(f"\nError en la edición: {str(e)}")
    
    return resultados