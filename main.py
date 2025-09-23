from Biblioteca.libros import (
    crear_libro, listar_libros, buscar_libro_por_id,
    actualizar_libro, bajar_libro
)
from Biblioteca import constantes as C

def mostrar(filas):
    headers = ["ID","Título","Autor","Género","Año","Totales","Disp.","Prest.","Activo"]
    print(" | ".join(headers))
    for f in filas:
        print(f"{f[C.LIBRO_ID]} | {f[C.LIBRO_TITULO]} | {f[C.LIBRO_AUTOR]} | "
              f"{f[C.LIBRO_GENERO]} | {f[C.LIBRO_ANIO]} | {f[C.LIBRO_TOTALES]} | "
              f"{f[C.LIBRO_DISPONIBLE]} | {f[C.LIBRO_PRESTADOS]} | "
              f"{'Sí' if f[C.LIBRO_ACTIVO] else 'No'}")

if __name__ == "__main__":
   
    print("\nListado activos:")
    mostrar(listar_libros())

    # Buscar por id
    idx, fila = buscar_libro_por_id(1)
    print("\nbuscar id=1:", (idx, fila is not None))

    print("\nListado activos (después de update):")
    mostrar(listar_libros())

    # Dar de baja id=2
    print("\nbaja id=2:", bajar_libro(2))

    print("\nActivos:")
    mostrar(listar_libros())

    print("\nTodos (incluye bajas):")
    mostrar(listar_libros(incluir_bajas=True))
