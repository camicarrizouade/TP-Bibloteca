from Biblioteca.libros import (
    crear_libro, listar_libros, buscar_libro_por_id,
    actualizar_libro, bajar_libro
)
from Biblioteca import storage as ST
from Biblioteca import constantes as C
from Biblioteca.consultas import mostrar_tabla


if __name__ == "__main__":
    HEADERS = C.ENCABEZADOS_LIBROS
    NUM_COLS  = {C.LIBRO_ID, C.LIBRO_ANIO, C.LIBRO_TOTALES, C.LIBRO_DISPONIBLE, C.LIBRO_PRESTADOS}
    BOOL_COLS = {C.LIBRO_ACTIVO}

    mostrar_tabla(HEADERS, listar_libros(), bool_cols=BOOL_COLS, num_cols=NUM_COLS)
