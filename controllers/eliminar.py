from .libros import ARCHIVO_LIBROS as archivo_libros
from .musica import ARCHIVO_MUSICA as archivo_musica
from .peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from utils.helpers import leer_json
import json

def _eliminar_elementos(archivo, campo, termino, resultados):
    datos = leer_json(archivo) or []
    encontrados = [item for item in datos if item.get(campo) == termino]
    if encontrados:
        resultados.extend(encontrados)
        nuevos_datos = [item for item in datos if item.get(campo) != termino]
        with open(archivo, "w") as f:
            json.dump(nuevos_datos, f, indent=4)

def eliminar_por_titulo(termino):
    resultados = []
    try:
        _eliminar_elementos(archivo_libros, "titulo", termino, resultados)
        _eliminar_elementos(archivo_musica, "titulo", termino, resultados)
        _eliminar_elementos(archivo_peliculas, "titulo", termino, resultados)
    except Exception as e:
        print(f"\nError en la eliminación: {str(e)}")
    return resultados

def eliminar_por_autor(termino):
    resultados = []
    try:
        _eliminar_elementos(archivo_libros, "autor", termino, resultados)
        _eliminar_elementos(archivo_musica, "autor", termino, resultados)
        _eliminar_elementos(archivo_peliculas, "autor", termino, resultados)
    except Exception as e:
        print(f"\nError en la eliminación: {str(e)}")
    return resultados

def eliminar_por_genero(termino):
    resultados = []
    try:
        _eliminar_elementos(archivo_libros, "genero", termino, resultados)
        _eliminar_elementos(archivo_musica, "genero", termino, resultados)
        _eliminar_elementos(archivo_peliculas, "genero", termino, resultados)
    except Exception as e:
        print(f"\nError en la eliminación: {str(e)}")
    return resultados
