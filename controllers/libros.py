from utils.screenControllers import *
from utils.helpers import *

ARCHIVO_LIBROS = "./data/libros.json"

def cargar_libros():
    if not os.path.exists(ARCHIVO_LIBROS):
        return []

    with open(ARCHIVO_LIBROS, 'r', encoding='utf-8') as f:
        contenido = f.read().strip()
        if not contenido:
            return []
        try:
            return json.loads(contenido)
        except json.JSONDecodeError:
            print("⚠️ Error: el archivo de libros no contiene un JSON válido.")
            return []

def obtener_ultimo_id():
    """Obtiene el último ID de los libros existentes"""
    libros = cargar_libros()
    return max(libro['id'] for libro in libros) if libros else 0

def registrar_libro():
    """Registra un nuevo libro con validaciones e ID único."""
    libros = leer_json(ARCHIVO_LIBROS)
    
    print("\n=== REGISTRAR NUEVO LIBRO ===")
    
    # Generar ID único incremental
    nuevo_id = obtener_ultimo_id() + 1
    print(f"\nID asignado a este libro: {nuevo_id}\n")

    while True:
        # Validación del nombre del libro
        nombre_libro = input("Ingresa el nombre del libro: ").strip()
        if not nombre_libro:
            print("Error: El nombre no puede estar vacío")
            continue
        if any(libro["nombre"].lower() == nombre_libro.lower() for libro in libros):            
            print("Error: Este título ya existe. Ingrese uno nuevo.")
            continue

        # Validación del autor
        nombre_autor = input("Ingresa el nombre del autor: ").strip()
        if not nombre_autor:
            print("Error: El nombre no puede estar vacío")
            continue
        elif any(caracter.isdigit() for caracter in nombre_autor):
            print("Error: El nombre no puede contener números")
            continue
        elif not all(caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in nombre_autor):
            print("Error: Solo se permiten letras, espacios, apóstrofes o guiones")
            continue

        # Validación del género
        generos_validos = ["Novela", "Ciencia ficción", "Fantasía", "Terror", "Romance", "Misterio"]
        genero = input(f"Ingresa el género del libro (opciones: {', '.join(generos_validos)}): ").strip().title()
        if not genero:
            print("Error: El género no puede estar vacío")
            continue
        elif genero not in generos_validos:
            print(f"Error: Género no válido. Opciones: {', '.join(generos_validos)}")
            continue

        # Validación del año de publicación (nuevo campo)
        while True:
            año = input("Ingresa el año de publicación: ").strip()
            if not año:
                print("Error: El año no puede estar vacío")
                continue
            try:
                año = int(año)
                if 1000 <= año <= 2023:  # Rango razonable para libros
                    break
                else:
                    print("Error: El año debe estar entre 1000 y 2023")
            except ValueError:
                print("Error: Debes ingresar un número válido")

        # Validación de la valoración
        while True:
            try:
                valoracion = input("Ingresa la valoración del libro (1-5 estrellas): ").strip()
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

        # Guardar el libro con ID
        nuevo_libro = {
            "id": nuevo_id,
            "nombre": nombre_libro,
            "autor": nombre_autor,
            "genero": genero,
            "año": año,
            "valoracion": valoracion,
            "fecha_registro": obtener_fecha_actual()
        }
        agregar_diccionario_a_json(ARCHIVO_LIBROS, nuevo_libro)
        print(f"\nLibro '{nombre_libro}' registrado exitosamente con ID {nuevo_id}.")
        break

def mostrar_libros():
    """Muestra todos los libros en formato de tabla con ID."""
    libros = leer_json(ARCHIVO_LIBROS)
    
    if not libros:
        print("\nNo hay libros registrados.")
        return
    
    # Ordenar libros por ID
    libros_ordenados = sorted(libros, key=lambda x: x['id'])
    
    print("\n=== LISTA DE LIBROS ===")
    print(f"{'ID':<5} {'Título':<15} {'Autor':<15} {'Género':<15} {'Año':<10} {'Valoración':<10}")
    print("-" * 95)
    
    for libro in libros_ordenados:
        print(f"{libro['id']:<5} {libro['nombre']:<15} {libro['autor']:<15} "
            f"{libro['genero']:<15} {libro.get('año', 'N/A'):<10} "
            f"{libro.get('valoracion', 'Sin valorar'):<10}")
    
    print(f"\nTotal de libros: {len(libros)}")

def buscar_por_id():
    """Busca un libro por su ID único."""
    libros = leer_json(ARCHIVO_LIBROS)
    
    id_buscar = input("\nIngresa el ID del libro a buscar: ").strip()
    if not id_buscar:
        print("Error: Debes ingresar un ID")
        return
    
    try:
        id_buscar = int(id_buscar)
    except ValueError:
        print("Error: El ID debe ser un número")
        return
    
    for libro in libros:
        if libro['id'] == id_buscar:
            print("\n=== LIBRO ENCONTRADO ===")
            print(f"ID: {libro['id']}")
            print(f"Título: {libro['nombre']}")
            print(f"Autor: {libro['autor']}")
            print(f"Género: {libro['genero']}")
            print(f"Año: {libro.get('año', 'No especificado')}")
            print(f"Valoración: {libro.get('valoracion', 'Sin valorar')}")
            print(f"Fecha registro: {libro.get('fecha_registro', 'N/A')}")
            return
    
    print(f"\nNo se encontró ningún libro con ID: {id_buscar}")

def ver_por_categoria_libros():
    """Muestra libros por género con mejor formato."""
    try:
        libros = leer_json(ARCHIVO_LIBROS)
    except Exception as e:
        print(f"\n⚠️ Error al cargar libros: {str(e)}")
        return
    
    if not libros:
        print("\nNo hay libros registrados.")
        return
        
    # Obtenemos géneros disponibles (manejando posibles errores)
    try:
        generos_disponibles = sorted({libro.get('genero', '') for libro in libros if libro.get('genero')})
    except Exception as e:
        print(f"⚠️ Error al obtener géneros: {str(e)}")
        return
    
    if not generos_disponibles:
        print("\nNo hay géneros registrados.")
        return
        
    print("\n=== FILTRAR POR GÉNERO ===")
    print(f"📚 Géneros disponibles: {', '.join(generos_disponibles)}")
        
    while True:
        genero = input("\nIngrese el género que desea ver (o '0' para cancelar): ").strip().title()
        
        if genero == "0":
            return
        if not genero:
            print("Error: Debe ingresar un género")
            continue
        
        # Buscar coincidencias (case insensitive)
        libros_filtrados = [
            libro for libro in libros 
            if str(libro.get('genero', '')).lower() == genero.lower()
        ]
        
        if not libros_filtrados:
            print(f"\n❌ No se encontraron libros del género '{genero}'")
            continue
        
        # Mostrar resultados
        print(f"\n📚 LIBROS DEL GÉNERO: {genero.upper()}")
        print("=" * 70)
        print(f"{'Título':<30} | {'Autor':<25} | {'Año':<6}")
        print("-" * 70)
        
        for libro in libros_filtrados:
            print(
                f"{libro.get('nombre', 'Desconocido')[:28]:<30} | "
                f"{libro.get('autor', 'Desconocido')[:22]:<25} | "
                f"{libro.get('año', 'N/A'):<6}"
            )
        
        print(f"\nTotal encontrados: {len(libros_filtrados)}")
        break