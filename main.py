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

def gestion_libros():
    opciones={
        "1. Crear libro": creacion_de_libro,
        "2. Mostrar libros:":mostrar_libros,
        "3. Actualizar libros":actualizacion_libro,
        "4. Dar de baja libros": dar_de_baja_libros,
        "5. Volver al menu anterior": menu(), 
    }
def gestion_socios():

    opciones={
        "1. Crear libro": creacion_de_libro,
        "2. Mostrar libros:":mostrar_libros,
        "3. Actualizar libros":actualizacion_libro,
        "4. Dar de baja libros": dar_de_baja_libros,
        "5. Volver al menu anterior": menu(), 
    }

def gestion_prestamos():
    opciones={
        "1. Crear libro": creacion_de_libro,
        "2. Mostrar libros:":mostrar_libros,
        "3. Actualizar libros":actualizacion_libro,
        "4. Dar de baja libros": dar_de_baja_libros,
        "5. Volver al menu anterior": menu(), 
    }


    def menu(gestion_libros, gestion_prestamos, gestion_socios):
        opciones={
        "1. Crear libro": creacion_de_libro,
        "2. Mostrar libros:":mostrar_libros,
        "3. Actualizar libros":actualizacion_libro,
        "4. Dar de baja libros": dar_de_baja_libros,
        "5. Volver al menu anterior": menu(), 
    }
    