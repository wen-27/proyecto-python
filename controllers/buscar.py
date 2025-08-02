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
                print(f"{'ID':<5} {'Título':<15} {'Autor':<15} {'Género':<15} {'Año':<10} {'Valoración':<10}")
                print("-" * 95)

                print(f"{libro['id']:<5} {libro['nombre']:<15} {libro['autor']:<15} "
                        f"{libro['genero']:<15} {libro.get('año', 'N/A'):<10} "
                        f"{libro.get('valoracion', 'Sin valorar'):<10}")

        # Música
        musicas = leer_json(archivo_musica)
        for musica in musicas:
            if musica[tipo] == termino:
                bander = False
                print("="*20, "Música encontrado", "="*20)
                
                print(f"{'ID':<6} {'Canción':<20} {'Artista':<20} {'Género':<12} {'Año':<10} {'Duración':<15} {'Valoración':<15} {'Registro':<25}")
                print("-" * 130)


                print(f"{musica['id']:<6} {musica['nombre']:<20} {musica['autor']:<20} {musica['genero']:<12} "
                    f"{musica['año']:<10} {musica.get('duracion', 'N/A'):<15} "
                    f"{musica.get('valoracion', 'Sin valorar'):<15} {musica.get('fecha_registro', 'N/A'):<25}")

        # Películas
        peliculas = leer_json(archivo_peliculas)
        for pelicula in peliculas:
            if pelicula[tipo] == termino:
                bander = False
                print("="*20, "Película encontrado", "="*20)
                print(f"{'ID':<6} {'Título':<20} {'Director':<20} {'Género':<12} {'Año':<10} {'Valoración':<15} {'Registro':<20}")
                print("-" * 100)
                
                print(f"{pelicula['id']:<6} {pelicula['nombre']:<20} {pelicula['autor']:<20} "
                    f"{pelicula['genero']:<12} {pelicula['año']:<10} "
                    f"{pelicula.get('valoracion', 'Sin valorar'):<10} {pelicula.get('fecha_registro', 'N/A'):<20}")
        if bander:
            print("No se encontraron resultados.")
    except Exception as e:
        print(f"\nError en la edición: {str(e)}")