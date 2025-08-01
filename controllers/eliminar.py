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

def eliminar(termino, tipo, archivo):
    resultados = []
    try:
        _eliminar_elementos(archivo, tipo, termino, resultados)
        print(f"El {tipo} {termino} fue eliminado exitosamente")
    except Exception as e:
        print(f"\nError en la eliminación: {str(e)}")
    return resultados


