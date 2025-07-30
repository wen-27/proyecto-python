from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from controllers.libros import *
from controllers.musica import *
from controllers.peliculas import *
from controllers.buscar import *
from controllers.editar import *
from utils.menus import *

def main():
    while True:
        limpiar_pantalla()
        print(menu_principal)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":  # Menú equipos
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
                    pass
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "2":  
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

        elif opcion == "3":  # Menú técnicos
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
        
        elif opcion == "4":  # Menú transferencias
            while True:
                limpiar_pantalla()
                print(menu_editar)
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    editar_por_titulo(termino, nuevo_dato)
                elif opcion == "2":
                    editar_por_autor(termino, nuevo_dato)
                elif opcion == "3":
                    editar_por_genero(termino, nuevo_dato)
                elif opcion == "4":
                    pass
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "5":  # Menú transferencias
            while True:
                limpiar_pantalla()
                print(ver_elementos_categoria)
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    pass
                elif opcion == "2":
                    pass
                elif opcion == "3":
                    pass
                elif opcion == "4":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "6":  # Menú transferencias
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

        elif opcion == "7":  # Menú transferencias
            while True:
                limpiar_pantalla()
                print(guardar_cargar)
                opcion = input("Seleccione una opción: ").strip()

                if opcion == "1":
                    pass
                elif opcion == "2":
                    pass
                elif opcion == "3":
                    pass
                elif opcion == "4":
                    pass
                elif opcion == "5":
                    pass
                elif opcion == "6":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            pausar_pantalla()

if __name__ == "__main__":
    main()