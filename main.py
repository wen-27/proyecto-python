from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from controllers.libros import ARCHIVO_LIBROS as archivo_libros
from controllers.musica import ARCHIVO_MUSICA as archivo_musica
from controllers.peliculas import ARCHIVO_PELICULAS as archivo_peliculas
from controllers.libros import *
from controllers.musica import *
from controllers.peliculas import *
from controllers.buscar import *
from controllers.editar import *
from controllers.eliminar import *
from utils.menus import *

def main():
    while True:
        limpiar_pantalla()
        print(menu_principal)
        opcion = input("Seleccione una opción: ").strip().lower()

        if opcion == "1":  # Menú registrar elementos
            while True:
                limpiar_pantalla()
                print(nuevo_elemento)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    registrar_libro()
                elif opcion == "2":
                    registrar_pelicula()
                elif opcion == "3":
                    registrar_cancion()
                elif opcion == "4":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "2":  # mostrar elementos
            while True:
                limpiar_pantalla()
                print(menu_ver_elementos)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    mostrar_libros()
                elif opcion == "2":
                    mostrar_peliculas()
                elif opcion == "3":
                    mostrar_canciones()
                elif opcion == "4":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "3":  # buscar elementos
            while True:
                limpiar_pantalla()
                print(menu_buscar)
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    tipo = "nombre"
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()    
                    buscar(termino, tipo)
                elif opcion == "2":
                    tipo = "autor"
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()            
                    buscar(termino, tipo)
                elif opcion == "3":
                    tipo = "genero"
                    termino = input(f"Ingrese el {tipo} a buscar: ").lower().strip()
                    buscar(termino, tipo)
                elif opcion == "4":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()
        
        elif opcion == "4":  # editar los elementos
            while True:
                limpiar_pantalla()
                print(menu_editar)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    tipo = "nombre"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "2":
                    tipo= "autor"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "3":
                    tipo= "genero"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "4":
                    tipo= "valoracion"
                    termino= str(input(f"Ingrese el {tipo} a editar:  ")).lower().strip()
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}: ")).lower().strip()
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "5":  # eliminar los elementos
            while True:
                limpiar_pantalla()
                print(menu_eliminar)
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    mostrar_libros()
                    mostrar_peliculas()
                    mostrar_canciones()
                    print("1. Para libro\n2. Para pelicula\n3. Para cancion")
                    opcionTipo = input("Seleccione si es pelicula, libro o musica: ").strip()
                    if opcionTipo == "1":
                        tipo = "nombre"
                        archivo = archivo_libros
                        termino= input("Ingrese el titulo que quieras eliminar: ").lower().strip()
                        eliminar(termino, tipo, archivo)
                    elif opcionTipo == "2":
                        tipo = "nombre"
                        archivo = archivo_peliculas
                        termino= input("Ingrese el titulo que quieras eliminar: ").lower().strip()
                        eliminar(termino, tipo, archivo)
                    elif opcionTipo == "3":
                        tipo = "nombre"
                        archivo = archivo_musica
                        termino= input("Ingrese el titulo que quieras eliminar: ").lower().strip()
                        print(termino)
                        eliminar(termino, tipo, archivo)
                    else:
                        print("Ingrese una opción valida")
                elif opcion == "2":
                    tipo = "id"
                    mostrar_libros()
                    mostrar_peliculas()
                    mostrar_canciones()
                    print("1. Para pelicula\n2. Para libro\n3. Para cancion")
                    opcionTipo = input("Seleccione si es pelicula, libro o musica: ").strip()
                    if opcionTipo == "1":
                        archivo = archivo_peliculas
                        termino= int(input("Ingrese el id que quieras eliminar: "))
                        eliminar(termino, tipo, archivo)
                    elif opcionTipo == "2":
                        archivo = archivo_libros
                        termino= int(input("Ingrese el id que quieras eliminar: "))
                        eliminar(termino, tipo, archivo)
                    elif opcionTipo == "3":
                        archivo = archivo_musica
                        termino= int(input("Ingrese el id que quieras eliminar: "))
                        eliminar(termino, tipo, archivo)
                    else:
                        print("Ingrese una opción valida")
                elif opcion == "3":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "6":  #ver elementos por categoria
            while True:
                limpiar_pantalla()
                print(ver_elementos_categoria)
                opcion = input("Seleccione una opción: ").strip().lower()

                if opcion == "1":
                    ver_por_categoria_libros()
                    
                elif opcion == "2":
                    ver_categoria_por_peliculas()
                elif opcion == "3":
                    ver_categoria_por_musica()
                elif opcion == "4":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()
        elif opcion == "7":  # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            pausar_pantalla()

if __name__ == "__main__":
    main()