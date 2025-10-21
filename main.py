from Biblioteca import storage as ST
from Biblioteca import constantes as C
from Biblioteca.libros import crear_libro, buscar_libro_por_id, actualizar_libro, listar_libros, bajar_libro 
from Biblioteca.socios import crear_socio, buscar_socio_por_id , actualizar_socio, listar_socios , bajar_socio
from Biblioteca.prestamos import crear_prestamo, listar_prestamos, actualizar_prestamo, bajar_prestamo  
from Biblioteca.consultas import mostrar_tabla
from Biblioteca.validaciones import normalizar_texto, entero_positivo, validar_dni, texto_no_vacio

#Funciones lambda
creacion_de_libro= crear_libro(normalizar_texto(input("Titulo:"), normalizar_texto(input("Autor:")), normalizar_texto(input("Género:")), entero_positivo(input("Anio:"),entero_positivo("Cantidad de libros a ingresar:"))))
mostrar_libros= mostrar_tabla(C.ENCABEZADOS_LIBROS,ST.M_LIBROS)
actualizacion_libro= actualizar_libro(input("Ingrese el id del libro a modificar:"))
dar_de_baja_libros=bajar_libro(input("Ingrese el id del libro a dar de baja:"))


#Funciones mas complejas en si
def mostrar_menu(titulo, opciones_dict):
    """Imprime el menu de forma legible para el usuario."""
    print("\n================================")
    print(f"     MENÚ DE {titulo.upper()}")
    print("==================================")
    for clave, valor_tup in opciones_dict.items():
        descripcion = valor_tup[0]

        print(f"[{clave}]{descripcion}")

    print("-----------------------------------")


def gestion_libros():
    """Sub menu de gestion de libros con excepciones para evitar usar muchos if anidados"""
    while True:
        opciones={
            "1": ("Crear libro", creacion_de_libro),
            "2": ("Mostrar libros", mostrar_libros),
            "3": ("Actualizar libros", actualizacion_libro),
            "4": ("Dar de baja libros", dar_de_baja_libros),
            "5": ("Volver al menú anterior.", "VOLVER."), 
        }

        mostrar_menu("Libros", opciones)
        opcion=input("Ingrese una opcion:").strip()
        try: 
            accion_tupla= opciones[opcion]
            
            if accion_tupla[1] == "VOLVER.":
                print("Volviendo al menu principal...")
                break
            
            accion_a_ejecutar= accion_tupla[1]
            accion_a_ejecutar()

        except KeyError:
            print("Error: opcion invalida. Por favor, ingrese un numero del 1 al 5.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

def gestion_socios():
    """Sub menu de gestion de socios con excepciones para evitar usar muchos if anidados"""
    while True:
        opciones={
            "1": ("Crear socio", creacion_de_socio ),
            "2": ("Mostrar socios", mostrar_socios ),
            "3": ("Actualizar socio", actualizar_socio ),
            "4": ("Dar de baja socios", bajar_socio ),
            "5": ("Volver al menú anterior.", "VOLVER."), 
        }

        mostrar_menu("Socios", opciones)
        opcion=input("Ingrese una opcion:").strip()

        try: 
            accion_tupla= opciones[opcion]
            
            if accion_tupla[1] == "VOLVER.":
                print("Volviendo al menu principal...")
                break
            
            accion_a_ejecutar= accion_tupla[1]
            accion_a_ejecutar()

        except KeyError:
            print("Error: opcion invalida. Por favor, ingrese un numero del 1 al 5.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

def gestion_prestamos():
    """Sub menu de gestion de prestamos con excepciones para evitar usar muchos if anidados"""
    while True:
        opciones={
            "1": ("Crear prestamo", creacion_prestamos ),
            "2": ("Mostrar prestamos", mostrar_prestamos ),
            "3": ("Actualizar prestamo", actualizar_prestamo),
            "4": ("Dar de baja prestamos", dar_de_baja_prestamo),
            "5": ("Volver al menú anterior.", "VOLVER."), 
        }

        mostrar_menu("Prestamos", opciones)
        opcion=input("Ingrese una opcion:").strip()
        try: 
            accion_tupla= opciones[opcion]
            
            if accion_tupla[1] == "VOLVER.":
                print("Volviendo al menu principal...")
                break
            
            accion_a_ejecutar= accion_tupla[1]
            accion_a_ejecutar()

        except KeyError:
            print("Error: opcion invalida. Por favor, ingrese un numero del 1 al 5.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

def menu_principal(gestion_libros, gestion_prestamos, gestion_socios):
    while True: 
        menu_opciones={
            "1":("Gestion de libros",gestion_libros),
            "2":("Gestion de socios",gestion_socios),
            "3":("Gestion de prestamos",gestion_prestamos),
            "4":("Salir del programa", "SALIR"), 
        }

        mostrar_menu("Principal", menu_opciones)
        opcion = input("Ingrese una opción:").strip()

        try:

            accion_a_ejecutar= menu_opciones[opcion]

            if accion == "SALIR":
                print("Finalizando el sistema...")
                break
                
            accion_a_ejecutar()
        
        except KeyError:
            print("Error: opción inválida. Ingrese un número válido del menú.")
        
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
    
if __name__ == "__main__":
    menu_principal()