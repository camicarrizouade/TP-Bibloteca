from Biblioteca.libros import (
    crear_libro, listar_libros, buscar_libro_por_id,
    actualizar_libro, bajar_libro
)
from Biblioteca import storage as ST
from Biblioteca import constantes as C
from Biblioteca.consultas import mostrar_tabla


if __name__ == "__main__":
    print("\nActivos:")
    mostrar_tabla(C.ENCABEZADOS_LIBROS, listar_libros(), bool_cols={C.LIBRO_ACTIVO})

    print("\nTodos (incluye bajas):")
    mostrar_tabla(C.ENCABEZADOS_LIBROS, listar_libros(incluir_bajas=True), bool_cols={C.LIBRO_ACTIVO})
