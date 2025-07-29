from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json

def buscar_por_titulo(termino):
    """Versión corregida que mantiene el parámetro obligatorio"""
    resultados = []
    
    try:
        # Buscar en libros
        libros = leer_json(archivo_libros) or []
        for libro in libros:
            if isinstance(libro, dict) and 'nombre' in libro:
                if termino.lower() in libro['nombre'].lower():
                    libro['tipo'] = 'Libro'
                    resultados.append(libro)
        
        # Buscar en música
        canciones = leer_json(archivo_musica) or []
        for cancion in canciones:
            if isinstance(cancion, dict) and 'nombre' in cancion:
                if termino.lower() in cancion['nombre'].lower():
                    cancion['tipo'] = 'Canción'
                    resultados.append(cancion)
        
        # Buscar en películas
        peliculas = leer_json(archivo_peliculas) or []
        for pelicula in peliculas:
            if isinstance(pelicula, dict) and 'titulo' in pelicula:
                if termino.lower() in pelicula['titulo'].lower():
                    pelicula['tipo'] = 'Película'
                    resultados.append(pelicula)
    
    except Exception as e:
        print(f"\nError en la búsqueda: {str(e)}")
    
    return resultados

def buscar_por_creador(termino):
    """Versión corregida para búsqueda por creador"""
    resultados = []
    
    try:
        # Buscar en libros (autores)
        libros = leer_json(archivo_libros) or []
        for libro in libros:
            if isinstance(libro, dict) and 'autor' in libro:
                if termino.lower() in libro['autor'].lower():
                    libro['tipo'] = 'Libro'
                    resultados.append(libro)
        
        # Buscar en música (artistas)
        canciones = leer_json(archivo_musica) or []
        for cancion in canciones:
            if isinstance(cancion, dict) and 'artista' in cancion:
                if termino.lower() in cancion['artista'].lower():
                    cancion['tipo'] = 'Canción'
                    resultados.append(cancion)
        
        # Buscar en películas (directores)
        peliculas = leer_json(archivo_peliculas) or []
        for pelicula in peliculas:
            if isinstance(pelicula, dict) and 'director' in pelicula:
                if termino.lower() in pelicula['director'].lower():
                    pelicula['tipo'] = 'Película'
                    resultados.append(pelicula)
    
    except Exception as e:
        print(f"\nError en la búsqueda: {str(e)}")
    
    return resultados

def buscar_por_genero(termino):
    """Versión corregida para búsqueda por género"""
    resultados = []
    
    try:
        # Buscar en libros
        libros = leer_json(archivo_libros) or []
        for libro in libros:
            if isinstance(libro, dict) and 'genero' in libro:
                if termino.lower() in libro['genero'].lower():
                    libro['tipo'] = 'Libro'
                    resultados.append(libro)
        
        # Buscar en música
        canciones = leer_json(archivo_musica) or []
        for cancion in canciones:
            if isinstance(cancion, dict) and 'genero' in cancion:
                if termino.lower() in cancion['genero'].lower():
                    cancion['tipo'] = 'Canción'
                    resultados.append(cancion)
        
        # Buscar en películas
        peliculas = leer_json(archivo_peliculas) or []
        for pelicula in peliculas:
            if isinstance(pelicula, dict) and 'genero' in pelicula:
                if termino.lower() in pelicula['genero'].lower():
                    pelicula['tipo'] = 'Película'
                    resultados.append(pelicula)
    
    except Exception as e:
        print(f"\nError en la búsqueda: {str(e)}")
    
    return resultados