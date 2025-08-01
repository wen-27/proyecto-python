from utils.screenControllers import *
from utils.helpers import *
import time

ARCHIVO_PELICULAS = "./data/peliculas.json"

def cargar_peliculas():
    if not os.path.exists(ARCHIVO_PELICULAS):
        return []

    with open(ARCHIVO_PELICULAS, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            return []
        try:
            return json.loads(contenido)
        except json.JSONDecodeError:
            print("⚠️ Error: el archivo de libros no contiene un JSON válido.")
            return []
    
def obtener_ultimo_id_peliculas():
    """Obtiene el último ID de las películas existentes"""
    peliculas = cargar_peliculas()
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
            "nombre": titulo,
            "autor": director,
            "genero": genero,
            "año": año,
            "valoracion": valoracion,
            "fecha_registro": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        agregar_diccionario_a_json(ARCHIVO_PELICULAS, nueva_pelicula)
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
    print(f"{'ID':<6} {'Título':<20} {'Director':<20} {'Género':<12} {'Año':<10} {'Valoración':<15} {'Registro':<20}")
    print("-" * 100)
    
    for pelicula in peliculas_ordenadas:
        print(f"{pelicula['id']:<6} {pelicula['nombre']:<20} {pelicula['autor']:<20} "
              f"{pelicula['genero']:<12} {pelicula['año']:<10} "
              f"{pelicula.get('valoracion', 'Sin valorar'):<10} {pelicula.get('fecha_registro', 'N/A'):<20}")
    
    print(f"\nTotal de películas: {len(peliculas)}")

def ver_categoria_por_peliculas():
    """Muestra películas filtradas por un género específico"""
    peliculas = leer_json(ARCHIVO_PELICULAS)

    if not peliculas:
        print("\nNo hay películas registradas")
        return
        
    # Obtenemos todos los géneros disponibles (sin repetir)
    generos_disponibles = sorted({pelicula["genero"] for pelicula in peliculas})
        
    print("\n=== FILTRAR POR GÉNERO ===")
    print(f"Géneros disponibles: {', '.join(generos_disponibles)}")
        
    while True:
        genero = input("\nIngrese el género que desea ver (o '0' para cancelar): ").strip().title()
        
        if genero == "0":
            return
        if not genero:
            print("Error: Debe ingresar un género")
            continue
        
        # Buscamos coincidencias
        peliculas_filtradas = [p for p in peliculas if p["genero"].lower() == genero.lower()]
        
        if not peliculas_filtradas:
            print(f"\nNo se encontraron películas del género '{genero}'. Intente con otro.")
            continue
        
        # Mostramos resultados
        print(f"\n=== PELÍCULAS DEL GÉNERO {genero.upper()} ===")
        print(f"{'Título':<25} {'Director':<25}")
        print("-" * 50)
        for pelicula in peliculas_filtradas:
            print(f"{pelicula['titulo']:<25} {pelicula['director']:<25}")
        print(f"\nTotal encontrados: {len(peliculas_filtradas)}")
        break