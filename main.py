from utils.screenControllers import limpiar_pantalla, pausar_pantalla
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
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":  # Menú registrar elementos
            while True:
                limpiar_pantalla()
                print(nuevo_elemento)
                opcion = input("Seleccione una opción: ").strip()

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
                opcion = input("Seleccione una opción: ").strip()

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
                    termino = input("Ingrese el termino a buscar :")
                    buscar_por_titulo(termino)
                elif opcion == "2":
                    termino = input("Ingrese el termino a buscar :")
                    buscar_por_creador(termino)
                elif opcion == "3":
                    termino = input("Ingrese el termino a buscar :")
                    buscar_por_genero(termino)
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()
        
        elif opcion == "4":  # editar los elementos
            while True:
                limpiar_pantalla()
                print(menu_editar)
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    tipo = "nombre"
                    termino= str(input(f"Ingrese el {tipo} a editar "))
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}"))
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "2":
                    tipo= "autor"
                    termino= str(input(f"Ingrese el {tipo} a editar "))
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}"))
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "3":
                    tipo= "genero"
                    termino= str(input(f"Ingrese el {tipo} a editar "))
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}"))
                    editar(termino, nuevo_dato, tipo)
                elif opcion == "4":
                    tipo= "valoracion"
                    termino= str(input(f"Ingrese el {tipo} a editar "))
                    nuevo_dato=str(input(f"ingresa el nuevo {tipo}"))
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
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    mostrar_libros()
                    mostrar_peliculas()
                    mostrar_canciones()
                    termino= input("Ingrese el termino que quieras eliminar ")
                    eliminar_por_titulo(termino)
                elif opcion == "2":
                    mostrar_libros()
                    mostrar_peliculas()
                    mostrar_canciones()
                    termino= input("Ingrese el termino que quieras eliminar ")
                    eliminar_por_id(termino)
                elif opcion == "3":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "6":  #ver elementos por categoria
            while True:
                limpiar_pantalla()
                print(ver_elementos_categoria)
                opcion = input("Seleccione una opción: ").strip()

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