from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json
import json
#editar por el titulo 
def editar_por_titulo(termino, nuevo_dato):  
    """version corregida que mantiene el parametro obligatorio"""

    resultados = []
    try: 
        # editar libros por titulo
        libros = leer_json(archivo_libros)
        for libro in libros:
            if libro["titulo"] == termino:
                libro["titulo"] = nuevo_dato
            with open(archivo_libros, "w") as f:
                json.dump(libros, f)
                resultados.append(libro)
        # editar musica por tirulo
        musicas= leer_json(archivo_musica)
        for musica in musicas:
            if musica["titulo"] == termino:
                musica["titulo"] = nuevo_dato
            with open(archivo_musica, "w") as f:
                json.dump(musicas, f)
                resultados.append(musica)
        
        # editar peliculas por titulo
        peliculas= leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula ["titulo"] == termino:
                pelicula["titulo"] = nuevo_dato
            with open(archivo_peliculas, "w") as f:
                json.dump(peliculas, f)
                resultados.append(pelicula)
        

    except Exception as e:
        print(f"\nError en la edicion: {str(e)}")
    
    return resultados
# editar por el autor 
def editar_por_autor(termino, nuevo_dato):
    """version corregida para editar por autor"""
    
    resultados = []
    try: 
        #editar libros por autor 
        libros = leer_json(archivo_libros)
        for libro in libros:
            if libro["autor"] == termino:
                libro["autor"] = nuevo_dato 
            with open(archivo_libros, "w") as f:
                json.dump(libro, f)
                resultados.append(libros)
    
        #editar musica por autor 
        musicas= leer_json(archivo_musica)
        for musica  in musicas:
            if musica["autor"] == termino:
                musica["autor"]= nuevo_dato
            with open (archivo_musica, "w") as f:
                json.dump(musica, f)
                resultados.append(musicas)
        
        #editar peliculas por titulo
        peliculas= leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula["autor"]== termino:
                pelicula["autor"] = nuevo_dato
            with open(archivo_peliculas, "w") as f:
                json.dump(peliculas, f)
                resultados.append(pelicula)
            
    except Exception as e:
        print(f"\nError en la edicion: {str(e)}")
    return resultados

#editar por genero
def editar_por_genero(termino, nuevo_dato):
    """version corregida para editar por autor"""
    
    resultados = []
    try:
        #editar libros por genero
        libros=leer_json(archivo_libros)
        for libro in libros:
            if libro ["genero"]== termino:
                libro["genero"] = nuevo_dato
            with open(archivo_libros, "w") as f:
                json.dump(libro, f)
                resultados.append(libros)
        #editar musica por genero 
        musicas= leer_json(archivo_musica)
        for musica in musicas:
            if musica["genero"] == termino:
                musica["genero"] = nuevo_dato
            with open (archivo_musica, "w") as f:
                json.dump(musica,f)
                resultados.append(musicas)
        #editar pelicula por genero
        peliculas=leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula["genero"]== termino:
                pelicula["genero"] = nuevo_dato
        with open(archivo_peliculas, "w") as f:
                json.dump(peliculas, f)
                resultados.append(pelicula)   
            
    except Exception as e:
        print(f"\nError en la edicion: {str(e)}")
    return resultados