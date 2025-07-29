import os
import json
def leer_json(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as arch:
            return json.load(arch)
#-------------------------------------------Escribir en el JSON-------------------------------------------
def escribir_json(nombre_archivo, diccionario):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(diccionario, archivo, indent=4)
#-----------------------------------Agregar diccionarios---------------------------------------------------
def agregar_diccionario_a_json(nombre_archivo, nuevo_diccionario):
    datos_existentes = leer_json(nombre_archivo)
    datos_existentes.append(nuevo_diccionario)
    escribir_json(nombre_archivo, datos_existentes)
#---------------------------------Funcion limpiar terminal----------------------------------------------
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')