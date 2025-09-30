from Biblioteca.constantes import (
    LIBRO_ID, LIBRO_TITULO, LIBRO_AUTOR, LIBRO_GENERO, LIBRO_ANIO,
    LIBRO_TOTALES, LIBRO_DISPONIBLE, LIBRO_PRESTADOS, LIBRO_ACTIVO
)
import Biblioteca.storage as ST

def _idx_por_id(libro_id: int):
    """
    Busca linealmente en M_LIBROS el libro cuyo LIBRO_ID == libro_id.
    Recorre la matriz de libros (lista de filas) y devuelve la
    posición (índice) de esa fila. Si no lo encuentra, retorna -1. 
    """
    for i, fila in enumerate(ST.M_LIBROS):
        if fila[LIBRO_ID] == libro_id:
            return i
    return -1

def listar_libros(incluir_bajas: bool = False):
    """Lista libros: todos si incluir_bajas=True; si no, solo activos."""
    return ST.M_LIBROS if incluir_bajas else [f for f in ST.M_LIBROS if f[LIBRO_ACTIVO]]

def buscar_libro_por_id(libro_id: int, incluir_bajas: bool = False):
    """Retorna (indice, fila) si existe (y activo salvo incluir_bajas=True); si no, (-1, None)."""
    i = _idx_por_id(libro_id)
    if i == -1: return (-1, None)
    f = ST.M_LIBROS[i]
    return (i, f) if (incluir_bajas or f[LIBRO_ACTIVO]) else (-1, None)
