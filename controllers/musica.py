from utils.screenControllers import *
from utils.helpers import *
import time

ARCHIVO_MUSICA = "./data/musica.json"
def cargar_musica():
    if not os.path.exists(ARCHIVO_MUSICA):
        return []

    with open(ARCHIVO_MUSICA, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            return []
        try:
            return json.loads(contenido)
        except json.JSONDecodeError:
            print("⚠️ Error: el archivo de libros no contiene un JSON válido.")
            return []
        
def obtener_ultimo_id():
    """Obtiene el último ID de una lista de diccionarios con clave 'id'"""
    datos = cargar_musica()
    return max(item['id'] for item in datos) if datos else 0


def registrar_cancion():
    """Registra una nueva canción con validaciones e ID incremental."""
    canciones = leer_json(ARCHIVO_MUSICA)

    print("\n=== REGISTRAR NUEVA CANCIÓN ===")
    
    # Generar nuevo ID incremental
    nuevo_id = obtener_ultimo_id() + 1
    print(f"\nID asignado a esta canción: {nuevo_id}\n")

    while True:
        # Validación del nombre de la canción
        nombre_cancion = input("Ingresa el nombre de la canción: ").strip()
        if not nombre_cancion:
            print("Error: El nombre no puede estar vacío")
            continue
        if any(cancion["nombre"].lower() == nombre_cancion.lower() for cancion in canciones):
            print("Error: Esta canción ya existe. Ingrese una nueva.")
            continue

        # Validación del artista
        nombre_artista = input("Ingresa el nombre del artista: ").strip()
        if not nombre_artista:
            print("Error: El nombre no puede estar vacío")
            continue
        elif any(caracter.isdigit() for caracter in nombre_artista):
            print("Error: El nombre no puede contener números")
            continue
        elif not all(caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in nombre_artista):
            print("Error: Solo se permiten letras, espacios, apóstrofes o guiones")
            continue

        # Validación del género musical
        generos_validos = ["Pop", "Rock", "Hip Hop", "Electrónica", "R&B", "Clásica", "Jazz", "Reggaetón"]
        genero = input(f"Ingresa el género musical (opciones: {', '.join(generos_validos)}): ").strip().title()
        if not genero:
            print("Error: El género no puede estar vacío")
            continue
        elif genero not in generos_validos:
            print(f"Error: Género no válido. Opciones: {', '.join(generos_validos)}")
            continue

        # Validación del año
        while True:
            año = input("Ingresa el año de lanzamiento (1900-2023): ").strip()
            if not año:
                print("Error: El año no puede estar vacío")
                continue
            try:
                año = int(año)
                if 1900 <= año <= 2023:
                    break
                else:
                    print("Error: El año debe estar entre 1900 y 2023")
            except ValueError:
                print("Error: Debes ingresar un número válido")

        # Validación de la valoración
        while True:
            try:
                valoracion = input("Ingresa la valoración de la canción (1-5 estrellas): ").strip()
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

        # Validación de duración
        while True:
            duracion = input("Ingresa la duración (formato MM:SS): ").strip()
            if not duracion:
                print("Error: La duración no puede estar vacía")
                continue
            try:
                minutos, segundos = map(int, duracion.split(':'))
                if 0 <= minutos < 60 and 0 <= segundos < 60:
                    break
                else:
                    print("Error: Formato inválido (MM:SS donde MM y SS entre 00-59)")
            except:
                print("Error: Formato inválido. Use MM:SS (ej: 03:45)")

        # Guardar la canción
        nueva_cancion = {
            "id": nuevo_id,
            "nombre": nombre_cancion,
            "artista": nombre_artista,
            "genero": genero,
            "año": año,
            "duracion": duracion,
            "valoracion": valoracion,
            "fecha_registro": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        agregar_diccionario_a_json(ARCHIVO_MUSICA, nueva_cancion)
        print(f"\nCanción '{nombre_cancion}' registrada exitosamente!")
        print(f"ID: {nuevo_id} | Valoración: {valoracion} | Fecha registro: {nueva_cancion['fecha_registro']}")
        break

def mostrar_canciones():
    """Muestra todas las canciones en formato de tabla con ID único."""
    canciones = leer_json(ARCHIVO_MUSICA)
    
    if not canciones:
        print("\nNo hay canciones registradas.")
        return
    
    # Ordenar canciones por ID (opcional)
    canciones_ordenadas = sorted(canciones, key=lambda x: x['id'])
    
    print("\n=== LISTA DE CANCIONES ===")
    print(f"{'ID':<6} {'Canción':<20} {'Artista':<20} {'Género':<12} {'Año':<6} {'Duración':<8} {'Valoración':<10} {'Registro':<20}")
    print("-" * 110)
    
    for cancion in canciones_ordenadas:
        print(f"{cancion['id']:<6} {cancion['nombre']:<20} {cancion['artista']:<20} {cancion['genero']:<12} "
              f"{cancion['año']:<6} {cancion.get('duracion', 'N/A'):<8} "
              f"{cancion.get('valoracion', 'Sin valorar'):<10} {cancion.get('fecha_registro', 'N/A'):<20}")
    
    print(f"\nTotal de canciones: {len(canciones)}")

def ver_categoria_por_musica():
    """Muestra canciones filtradas por género"""
    canciones = leer_json(ARCHIVO_MUSICA)

    if not canciones:
        print("\nNo hay canciones registradas")
        return
        
    # Obtenemos todos los géneros disponibles
    generos_disponibles = sorted({cancion["genero"] for cancion in canciones})
        
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
        canciones_filtradas = [c for c in canciones if c["genero"].lower() == genero.lower()]
        
        if not canciones_filtradas:
            print(f"\nNo se encontraron canciones del género '{genero}'. Intente con otro.")
            continue
        
        # Mostramos resultados
        print(f"\n=== CANCIONES DEL GÉNERO {genero.upper()} ===")
        print(f"{'Canción':<25} {'Artista':<25}")
        print("-" * 50)
        for cancion in canciones_filtradas:
            print(f"{cancion['nombre']:<25} {cancion['artista']:<25}")
        print(f"\nTotal encontrados: {len(canciones_filtradas)}")
        break