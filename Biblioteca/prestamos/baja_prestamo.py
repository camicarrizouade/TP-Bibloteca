from Biblioteca import constantes as C
import Biblioteca.storage as ST
from .prestamos import buscar_prestamo_por_id, _idx_libro

def bajar_prestamo(prestamo_id: int):
    """
    Baja lógica: anula/cierra el préstamo y repone el stock si aún estaba activo.
    Retorna (True,'Baja OK') o (False,msg).
    """
    i, p = buscar_prestamo_por_id(prestamo_id, incluir_bajas=True)
    if i == -1: return (False, "Préstamo no encontrado.")
    if not p[C.PRESTAMO_ACTIVO]:
        return (False, "El préstamo ya estaba cerrado.")

    i_l = _idx_libro(p[C.PRESTAMO_LIBRO_ID])
    if i_l == -1:
        return (False, "Libro del préstamo no existe.")

    # reponer stock porque se cancela sin devolución registrada
    ST.M_LIBROS[i_l][C.LIBRO_DISPONIBLE] = ST.M_LIBROS[i_l][C.LIBRO_DISPONIBLE] + 1
    ST.M_LIBROS[i_l][C.LIBRO_PRESTADOS]  = ST.M_LIBROS[i_l][C.LIBRO_PRESTADOS] - 1

    ST.M_PRESTAMOS[i][C.PRESTAMO_ACTIVO] = False
    return (True, "Baja OK")