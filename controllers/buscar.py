from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json

def buscar_por_titulo(termino):
    """Busca en libros, música y películas por título/título/nombre"""
    if not termino or not isinstance(termino, str):
        return []
    
    resultados = []
    
    try:
        # Buscar en libros
        libros = leer_json(archivo_libros) or []
        for libro in libros:
            if isinstance(libro, dict) and libro.get('nombre'):
                if termino.lower() in libro['nombre'].lower():
                    resultados.append({**libro, 'tipo': 'Libro'})
        
        # Buscar en música
        canciones = leer_json(archivo_musica) or []
        for cancion in canciones:
            if isinstance(cancion, dict) and cancion.get('nombre'):
                if termino.lower() in cancion['nombre'].lower():
                    resultados.append({**cancion, 'tipo': 'Canción'})
        
        # Buscar en películas
        peliculas = leer_json(archivo_peliculas) or []
        for pelicula in peliculas:
            # Maneja tanto 'titulo' como 'nombre' como clave
            titulo = pelicula.get('titulo') or pelicula.get('nombre')
            if isinstance(pelicula, dict) and titulo:
                if termino.lower() in titulo.lower():
                    resultados.append({**pelicula, 'tipo': 'Película'})
    
    except Exception as e:
        print(f"\nError en la búsqueda por título: {str(e)}")
    
    return resultados

def buscar_por_creador(termino):
    """Busca por autor/artista/director"""
    if not termino or not isinstance(termino, str):
        return []
    
    resultados = []
    
    try:
        # Buscar en libros (autores)
        libros = leer_json(archivo_libros) or []
        for libro in libros:
            if isinstance(libro, dict) and libro.get('autor'):
                if termino.lower() in libro['autor'].lower():
                    resultados.append({**libro, 'tipo': 'Libro'})
        
        # Buscar en música (artistas)
        canciones = leer_json(archivo_musica) or []
        for cancion in canciones:
            if isinstance(cancion, dict) and cancion.get('artista'):
                if termino.lower() in cancion['artista'].lower():
                    resultados.append({**cancion, 'tipo': 'Canción'})
        
        # Buscar en películas (directores)
        peliculas = leer_json(archivo_peliculas) or []
        for pelicula in peliculas:
            if isinstance(pelicula, dict) and pelicula.get('director'):
                if termino.lower() in pelicula['director'].lower():
                    resultados.append({**pelicula, 'tipo': 'Película'})
    
    except Exception as e:
        print(f"\nError en la búsqueda por creador: {str(e)}")
    
    return resultados

def buscar_por_genero(termino):
    """Busca por género en todos los tipos de medios"""
    if not termino or not isinstance(termino, str):
        return []
    
    resultados = []
    
    try:
        # Buscar en libros
        libros = leer_json(archivo_libros) or []
        for libro in libros:
            if isinstance(libro, dict) and libro.get('genero'):
                if termino.lower() in libro['genero'].lower():
                    resultados.append({**libro, 'tipo': 'Libro'})
        
        # Buscar en música
        canciones = leer_json(archivo_musica) or []
        for cancion in canciones:
            if isinstance(cancion, dict) and cancion.get('genero'):
                if termino.lower() in cancion['genero'].lower():
                    resultados.append({**cancion, 'tipo': 'Canción'})
        
        # Buscar en películas
        peliculas = leer_json(archivo_peliculas) or []
        for pelicula in peliculas:
            if isinstance(pelicula, dict) and pelicula.get('genero'):
                if termino.lower() in pelicula['genero'].lower():
                    resultados.append({**pelicula, 'tipo': 'Película'})
    
    except Exception as e:
        print(f"\nError en la búsqueda por género: {str(e)}")
    
    return resultados