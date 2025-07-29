from utils.screenControllers import *
from utils.helpers import *
import time

ARCHIVO_PELICULAS = "data/peliculas.json"
if not os.path.exists(ARCHIVO_PELICULAS):
    os.makedirs(os.path.dirname(ARCHIVO_PELICULAS), exist_ok=True)
    with open(ARCHIVO_PELICULAS, 'w', encoding='utf-8') as f:
        f.write('[]')  # Archivo JSON vacío
        
def obtener_ultimo_id_peliculas():
    """Obtiene el último ID de las películas existentes"""
    peliculas = leer_json(ARCHIVO_PELICULAS)
    return max(pelicula['id'] for pelicula in peliculas) if peliculas else 0

def registrar_pelicula():
    """Registra una nueva película con validaciones e ID único."""
    peliculas = leer_json(ARCHIVO_PELICULAS)
    
    print("\n=== REGISTRAR NUEVA PELÍCULA ===")
    
    # Generar ID único incremental
    nuevo_id = obtener_ultimo_id_peliculas() + 1
    print(f"\nID asignado a esta película: {nuevo_id}\n")

    while True:
        # Validación del título
        titulo = input("Ingresa el título de la película: ").strip()
        if not titulo:
            print("Error: El título no puede estar vacío")
            continue
        if any(pelicula["titulo"].lower() == titulo.lower() for pelicula in peliculas):
            print("Error: Este título ya existe. Ingrese uno nuevo.")
            continue

        # Validación del director
        director = input("Ingresa el nombre del director: ").strip()
        if not director:
            print("Error: El nombre no puede estar vacío")
            continue
        elif any(caracter.isdigit() for caracter in director):
            print("Error: El nombre no puede contener números")
            continue
        elif not all(caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in director):
            print("Error: Solo se permiten letras, espacios, apóstrofes o guiones")
            continue

        # Validación del género
        generos_validos = ["Acción", "Aventura", "Comedia", "Drama", "Ciencia ficción", 
                         "Fantasía", "Terror", "Romance", "Misterio", "Animación"]
        genero = input(f"Ingresa el género (opciones: {', '.join(generos_validos)}): ").strip().title()
        if not genero:
            print("Error: El género no puede estar vacío")
            continue
        elif genero not in generos_validos:
            print(f"Error: Género no válido. Opciones: {', '.join(generos_validos)}")
            continue

        # Validación del año
        while True:
            año = input("Ingresa el año de estreno (1895-2023): ").strip()
            if not año:
                print("Error: El año no puede estar vacío")
                continue
            try:
                año = int(año)
                if 1895 <= año <= 2023:  # Primera película en 1895
                    break
                else:
                    print("Error: El año debe estar entre 1895 y 2023")
            except ValueError:
                print("Error: Debes ingresar un número válido")

        # Validación de la valoración
        while True:
            try:
                valoracion = input("Ingresa la valoración (1-5 estrellas): ").strip()
                if not valoracion:
                    valoracion = "Sin valorar"
                    break
                valoracion = int(valoracion)
                if 1 <= valoracion <= 5:
                    valoracion = f"{valoracion}★"
                    break
                else:
                    print("Error: La valoración debe estar entre 1 y 5")
            except ValueError:
                print("Error: Debes ingresar un número entero")

        # Guardar la película 
        nueva_pelicula = {
            "id": nuevo_id,
            "titulo": titulo,
            "director": director,
            "genero": genero,
            "año": año,
            "valoracion": valoracion,
            "fecha_registro": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        peliculas.append(nueva_pelicula)
        agregar_diccionario_a_json(ARCHIVO_PELICULAS, peliculas)
        print(f"\nPelícula '{titulo}' registrada exitosamente con ID {nuevo_id}.")
        break

def mostrar_peliculas():
    """Muestra todas las películas en formato de tabla con ID."""
    peliculas = leer_json(ARCHIVO_PELICULAS)
    
    if not peliculas:
        print("\nNo hay películas registradas.")
        return
    
    # Ordenar por ID
    peliculas_ordenadas = sorted(peliculas, key=lambda x: x['id'])
    
    print("\n=== LISTA DE PELÍCULAS ===")
    print(f"{'ID':<5} {'Título':<25} {'Director':<20} {'Género':<15} {'Año':<6} {'Valoración':<10} {'Registro':<20}")
    print("-" * 100)
    
    for pelicula in peliculas_ordenadas:
        print(f"{pelicula['id']:<5} {pelicula['titulo']:<25} {pelicula['director']:<20} "
              f"{pelicula['genero']:<15} {pelicula['año']:<6} "
              f"{pelicula.get('valoracion', 'Sin valorar'):<10} {pelicula.get('fecha_registro', 'N/A'):<20}")
    
    print(f"\nTotal de películas: {len(peliculas)}")