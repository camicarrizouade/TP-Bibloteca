from Biblioteca.constantes import *
import Biblioteca.storage as ST
from .libros import buscar_libro_por_id

def actualizar_libro(libro_id, titulo=None, autor=None, genero=None, anio=None, totales=None):
    i, f = buscar_libro_por_id(libro_id, incluir_bajas=True)
    if i == -1:
        return (False, "Libro no encontrado.")

    if titulo is not None:
        t = str(titulo).strip()
        if not t: return (False, "Título vacío.")
        f[LIBRO_TITULO] = t

    if autor is not None:
        a = str(autor).strip()
        if not a: return (False, "Autor vacío.")
        f[LIBRO_AUTOR] = a

    if genero is not None:
        g = str(genero).strip()
        if not g: return (False, "Género vacío.")
        f[LIBRO_GENERO] = g

    if anio is not None:
        s = str(anio).strip()
        if not (s.isdigit() and int(s) > 0): return (False, "Año inválido.")
        f[LIBRO_ANIO] = int(s)

    if totales is not None:
        s = str(totales).strip()
        if not (s.isdigit() and int(s) > 0): return (False, "Totales inválido.")
        nuevo_tot = int(s)
        prestados = f[LIBRO_PRESTADOS]
        if nuevo_tot < prestados:
            return (False, "Totales no puede ser menor que los prestados.")
        f[LIBRO_TOTALES]     = nuevo_tot
        f[LIBRO_DISPONIBLE]  = nuevo_tot - prestados   # mantiene: TOTALES = DISPONIBLE + PRESTADOS

    return (True, "OK")