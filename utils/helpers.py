import os
import json
from datetime import datetime
def leer_json(nombre_archivo):
    if not os.path.exists(nombre_archivo):
            os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write('[]')  # JSON válido, lista vacía

    with open(nombre_archivo, "r", encoding="utf-8") as arch:
        contenido = arch.read().strip()
        if not contenido:
            return []
        return json.loads(contenido)
        
def escribir_json(nombre_archivo, diccionario):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(diccionario, archivo, indent=4)

def agregar_diccionario_a_json(nombre_archivo, nuevo_diccionario):
    datos_existentes = leer_json(nombre_archivo)
    datos_existentes.append(nuevo_diccionario)
    escribir_json(nombre_archivo, datos_existentes)
    
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_fecha_actual():
    """Devuelve la fecha actual en formato DD/MM/YYYY"""
    return datetime.now().strftime("%d/%m/%Y")
