def listar_libros(incluir_bajas: bool = False):
    """Lista libros: todos si incluir_bajas=True; si no, solo activos."""
    return ST.M_LIBROS if incluir_bajas else [f for f in ST.M_LIBROS if f[LIBRO_ACTIVO]]

def buscar_libro_por_id(libro_id: int, incluir_bajas: bool = False):
    """Retorna (indice, fila) si existe (y activo salvo incluir_bajas=True); si no, (-1, None)."""
    i = _idx_por_id(libro_id)
    if i == -1: return (-1, None)
    f = ST.M_LIBROS[i]
    return (i, f) if (incluir_bajas or f[LIBRO_ACTIVO]) else (-1, None)
