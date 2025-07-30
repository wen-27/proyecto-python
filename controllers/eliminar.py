from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json
import json

#eliminar por el titulo 
def eliminar_por_titulo(termino):
    """Versión corregida que mantiene el parámetro obligatorio"""
    
    resultados = []
    
    try:
        # Eliminar libros por título
        libros = leer_json(archivo_libros) or []
        for libro in libros:
            if libro.get("titulo") == termino:
                resultados.append(libro)
        libros = [libro for libro in libros if libro.get("titulo") != termino]
        with open(archivo_libros, "w") as f:
            json.dump(libros, f)
        
        # Eliminar música por título
        musicas = leer_json(archivo_musica) or []
        for musica in musicas:
            if musica.get("titulo") == termino:
                resultados.append(musica)
        musicas = [musica for musica in musicas if musica.get("titulo") != termino]
        with open(archivo_musica, "w") as f:
            json.dump(musicas, f)
        
        # Eliminar películas por título
        peliculas = leer_json(archivo_peliculas) or []
        for pelicula in peliculas:
            if pelicula.get("titulo") == termino:
                resultados.append(pelicula)
        peliculas = [pelicula for pelicula in peliculas if pelicula.get("titulo") != termino]
        with open(archivo_peliculas, "w") as f:
            json.dump(peliculas, f)

    except Exception as e:
        print(f"\nError en la eliminación: {str(e)}")
    
    return resultados


def eliminar_por_autor(termino):
    """"""