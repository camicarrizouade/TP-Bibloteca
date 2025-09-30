from Biblioteca import constantes as C
import Biblioteca.storage as ST

# --- helpers internos (compartidos en módulo) -------------------------------

def _idx_por_id(prestamo_id: int):
    """Índice del préstamo por ID o -1."""
    for i, f in enumerate(ST.M_PRESTAMOS):
        if f[C.PRESTAMO_ID] == prestamo_id:
            return i
    return -1

def _idx_libro(libro_id: int):
    """Devuelve el índice de la fila en M_LIBROS cuyo LIBRO_ID == libro_id; si no existe, -1."""
    for i, f in enumerate(ST.M_LIBROS):
        if f[C.LIBRO_ID] == libro_id:
            return i
    return -1

def _idx_socio(socio_id: int):
    """Devuelve el índice de la fila en M_SOCIOS cuyo SOCIO_ID == socio_id; si no existe, -1."""
    for i, f in enumerate(ST.M_SOCIOS):
        if f[C.SOCIO_ID] == socio_id:
            return i
    return -1

# --- lectura -----------------------------------------------------------------

def listar_prestamos(incluir_bajas: bool = False):
    """Todos si incluir_bajas=True; si no, solo activos."""
    return ST.M_PRESTAMOS if incluir_bajas else [f for f in ST.M_PRESTAMOS if f[C.PRESTAMO_ACTIVO]]

def buscar_prestamo_por_id(prestamo_id: int, incluir_bajas: bool = False):
    """(índice, fila) si existe (respeta incluir_bajas); si no, (-1, None)."""
    i = _idx_por_id(prestamo_id)
    if i == -1: return -1, None
    f = ST.M_PRESTAMOS[i]
    return (i, f) if (incluir_bajas or f[C.PRESTAMO_ACTIVO]) else (-1, None)
