from Biblioteca.constantes import *
import Biblioteca.storage as ST

def bajar_libro(libro_id: int):
    """Baja lógica del libro:
    - Si existe, marca LIBRO_ACTIVO=False (no borra la fila) y devuelve (True, "Baja OK").
    - Si no existe, devuelve (False, "Libro no encontrado.").
"""
    for i, f in enumerate(ST.M_LIBROS):
        if f[LIBRO_ID] == libro_id:
            ST.M_LIBROS[i][LIBRO_ACTIVO] = False
            return (True, "Baja OK")
    return (False, "Libro no encontrado.")