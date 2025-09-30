from Biblioteca import constantes as C
import Biblioteca.storage as ST
import Biblioteca.validaciones as V
from .prestamos import _idx_libro, _idx_socio

def crear_prestamo(socio_id, libro_id, fecha_salida):
    """Crea préstamo activo y actualiza stock del libro. Retorna (True,id) o (False,msg)."""
    # validar existencia y estado
    i_s = _idx_socio(socio_id)
    if i_s == -1 or not ST.M_SOCIOS[i_s][C.SOCIO_ACTIVO]:
        return (False, "Socio inexistente o inactivo.")

    i_l = _idx_libro(libro_id)
    if i_l == -1 or not ST.M_LIBROS[i_l][C.LIBRO_ACTIVO]:
        return (False, "Libro inexistente o inactivo.")

    # validar fecha y stock
    f = V.normalizar_texto(fecha_salida)
    if not V.validar_fecha_ymd(f):
        return (False, "Fecha inválida (AAAA-MM-DD).")

    disp = ST.M_LIBROS[i_l][C.LIBRO_DISPONIBLE]
    if str(disp).isdigit() and int(disp) <= 0:
        return (False, "No hay ejemplares disponibles.")

    # OK: ajusto stock y creo fila
    ST.M_LIBROS[i_l][C.LIBRO_DISPONIBLE] = int(disp) - 1
    ST.M_LIBROS[i_l][C.LIBRO_PRESTADOS]  = ST.M_LIBROS[i_l][C.LIBRO_PRESTADOS] + 1

    nuevo_id = ST.SIGUIENTE_PRESTAMO_ID
    ST.SIGUIENTE_PRESTAMO_ID += 1

    fila = [None] * (C.PRESTAMO_ACTIVO + 1)
    fila[C.PRESTAMO_ID]           = nuevo_id
    fila[C.PRESTAMO_SOCIO_ID]     = int(socio_id)
    fila[C.PRESTAMO_LIBRO_ID]     = int(libro_id)
    fila[C.PRESTAMO_FECHA_SALIDA] = f
    fila[C.PRESTAMO_FECHA_DEVOL]  = ""      # aún no devuelto
    fila[C.PRESTAMO_ACTIVO]       = True

    ST.M_PRESTAMOS.append(fila)
    return (True, nuevo_id)
