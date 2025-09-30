from Biblioteca import constantes as C
import Biblioteca.storage as ST
import Biblioteca.validaciones as V
from .prestamos import buscar_prestamo_por_id, _idx_libro

def actualizar_prestamo(prestamo_id, fecha_devolucion=None):
    """Registra devolución (cierra el préstamo). Retorna (True,'OK') o (False,msg)."""
    i, p = buscar_prestamo_por_id(prestamo_id, incluir_bajas=True)
    if i == -1: return (False, "Préstamo no encontrado.")
    if not p[C.PRESTAMO_ACTIVO]:
        return (False, "El préstamo ya está cerrado.")

    if fecha_devolucion is None:
        return (False, "Falta fecha de devolución.")

    fd = V.normalizar_texto(fecha_devolucion)
    if not V.validar_fecha_ymd(fd):
        return (False, "Fecha devolución inválida (AAAA-MM-DD).")

    # ajustar stock del libro
    i_l = _idx_libro(p[C.PRESTAMO_LIBRO_ID])
    if i_l == -1:
        return (False, "Libro del préstamo no existe.")

    ST.M_LIBROS[i_l][C.LIBRO_DISPONIBLE] = ST.M_LIBROS[i_l][C.LIBRO_DISPONIBLE] + 1
    ST.M_LIBROS[i_l][C.LIBRO_PRESTADOS]  = ST.M_LIBROS[i_l][C.LIBRO_PRESTADOS] - 1

    # cerrar préstamo
    ST.M_PRESTAMOS[i][C.PRESTAMO_FECHA_DEVOL] = fd
    ST.M_PRESTAMOS[i][C.PRESTAMO_ACTIVO]      = False
    return (True, "OK")