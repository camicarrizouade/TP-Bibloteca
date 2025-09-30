from Biblioteca import storage as ST
from Biblioteca import constantes as C
from Biblioteca.socios import crear_socio
from Biblioteca.prestamos import crear_prestamo, listar_prestamos, actualizar_prestamo
from Biblioteca.consultas import mostrar_tabla

def preparar_datos_para_prestamos():
    """Asegura 1 socio activo y 1 libro activo con stock. Devuelve (socio_id, libro_id)."""
    # socio: si no hay, creo uno
    if not any(f[C.SOCIO_ACTIVO] for f in ST.M_SOCIOS):
        crear_socio("Socio Demo", "30000001")

    socio_id = next((f[C.SOCIO_ID] for f in ST.M_SOCIOS if f[C.SOCIO_ACTIVO]), None)
    libro_id = next((f[C.LIBRO_ID] for f in ST.M_LIBROS
                     if f[C.LIBRO_ACTIVO] and int(f[C.LIBRO_DISPONIBLE]) > 0), None)
    return socio_id, libro_id

def probar_prestamos():
    HEAD = C.ENCABEZADOS_PRESTAMOS
    NUMS = {C.PRESTAMO_ID, C.PRESTAMO_SOCIO_ID, C.PRESTAMO_LIBRO_ID}
    BOOL = {C.PRESTAMO_ACTIVO}

    socio_id, libro_id = preparar_datos_para_prestamos()
    print("Usando socio_id=", socio_id, "libro_id=", libro_id)

    ok, dato = crear_prestamo(socio_id, libro_id, "2025-10-01")
    print("crear_prestamo:", (ok, dato))

    print("\nPréstamos activos:")
    mostrar_tabla(HEAD, listar_prestamos(), bool_cols=BOOL, num_cols=NUMS)

    if ok:
        print("\nDevolver el préstamo recien creado:")
        print(actualizar_prestamo(dato, "2025-10-03"))

    print("\nTodos (incluye bajas):")
    mostrar_tabla(HEAD, listar_prestamos(True), bool_cols=BOOL, num_cols=NUMS)

if __name__ == "__main__":
    probar_prestamos()