from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from controllers.libros import (
    registrar_libro,
    mostrar_libros,
)
from controllers.musica import (
    registrar_cancion,
    mostrar_canciones,
)
from controllers.peliculas import (
    registrar_pelicula,
    mostrar_peliculas,
)
from controllers.buscar import (
    buscar_por_creador,
    buscar_por_genero,
    buscar_por_titulo,
)
from controllers.editar import(
    editar_por_titulo,
    editar_por_autor,
    editar_por_genero,
)
from controllers.eliminar import(
    eliminar_por_titulo,
    eliminar_por_autor,
    _eliminar_elementos,
)
from utils.menus import (
    menu_principal,
    nuevo_elemento,
    menu_ver_elementos,
    menu_buscar,
    menu_editar,
    ver_elementos_categoria,
    guardar_cargar,

)

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
                    registrar_cancion()
                elif opcion == "3":
                    registrar_pelicula()
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
                    mostrar_canciones()
                elif opcion == "3":
                    mostrar_peliculas()
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
                    termino = input("Ingrese el termino a buscar")
                    buscar_por_titulo(termino)
                elif opcion == "2":
                    termino = input("Ingrese el termino a buscar")
                    buscar_por_creador(termino)
                elif opcion == "3":
                    termino = input("Ingrese el termino a buscar")
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
                    termino= str(input("Ingrese el termino a buscar "))
                    nuevo_dato=str(input("ingresa el nuevo termino"))
                    editar_por_titulo(termino, nuevo_dato)
                elif opcion == "2":
                    termino= str(input("Ingrese el termino a buscar "))
                    nuevo_dato=str(input("ingresa el nuevo termino"))
                    editar_por_autor(termino, nuevo_dato)
                elif opcion == "3":
                    termino= str(input("Ingrese el termino a buscar "))
                    nuevo_dato=str(input("ingresa el nuevo termino"))
                    editar_por_genero(termino, nuevo_dato)
                elif opcion == "4":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "5":  # eliminar los elementos
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
                    pass
                elif opcion == "5":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
                pausar_pantalla()

        elif opcion == "6":  # Menú transferencias
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