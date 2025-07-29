from utils.screenControllers import limpiar_pantalla, pausar_pantalla
from controllers.libros import (
    listar_equipos,
    crear_equipo,
    editar_equipo,
    eliminar_equipo
)
from controllers.musica import (
    listar_jugadores,
    crear_jugador,
    editar_jugador,
    eliminar_jugador
)
from controllers.peliculas import (
    ver_estadisticas,
    registrar_transferencia,
    editar_transferencia,
    eliminar_transferencia
)

from utils.menus import (
    menu_principal,
    nuevo_elemento,
    menu_ver_elementos,
    menu_buscar,
    menu_editar,
    ver_elementos_categoria,
    guardar_cargar

)

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

        elif opcion == "2":  # Menú jugadores
            while True:
                limpiar_pantalla()
                print(menu_ver_elementos)
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

        elif opcion == "3":  # Menú técnicos
            while True:
                limpiar_pantalla()
                print(menu_buscar)
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
        
        elif opcion == "4":  # Menú transferencias
            while True:
                limpiar_pantalla()
                print(menu_editar)
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